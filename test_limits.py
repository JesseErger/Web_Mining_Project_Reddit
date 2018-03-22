import time
import datetime
import praw
import os
import traceback
import requests
from threading import Thread
import threading
b = "timestamp:"
d = ".."

#Config Details-
r = praw.Reddit(client_id='zvvcHnJcdS2ZKQ',
                     client_secret='tQRoHw56n8bytmblm9YT3WTNl6Q',
                     password='Thisisjustatemporarypassword123',
                     user_agent='Web_project /u/Reddit_Research_Proj',
                     username='Reddit_Research_Proj')
def resume():
	if os.path.exists('config.txt'):
		line = file('config.txt').read()
		startStamp,endStamp,step,subName=line.split(',')
		startStamp,endStamp,step=int(startStamp),int(endStamp),int(step)
		return startStamp,endStamp,step,subName
	else:
		return 0

subreddits_of_interest = ['depression', 'ChangeMyView', 'InsightfulQuestions', 'SRSDiscussion', 'SuicideWatch', 'PTSD', 'humor', 'funny', 'programmer humor'] 



startStamp= int(time.mktime(datetime.datetime.strptime("01/01/2018", "%d/%m/%Y").timetuple()))
endStamp= int(time.mktime(datetime.datetime.strptime("03/03/2018", "%d/%m/%Y").timetuple()))
sdate=datetime.datetime.fromtimestamp(int(startStamp)).strftime('%d-%m-%Y')
edate=datetime.datetime.fromtimestamp(int(endStamp)).strftime('%d-%m-%Y')
step=24000

def getNew(subName,folderName,i):
    obj = open(str(i)+"_config.txt",'w')
    obj.write(str(startStamp)+','+str(endStamp)+','+str(step)+','+str(subName))
    obj.close()
    subreddit_comment = threading.local()
    subreddit_comment.i = r.get_comments(subName, limit=1000)
    subreddit_posts = r.get_submissions(subName, limit=1000)
    for comment in subreddit_comment:
        print(comment)
        url= "https://reddit.com" + comment.permalink
        data= {'user-agent':'archive by /u/healdb'}
        #manually grabbing this file is much faster than loading the individual json files of every single comment, as this json provides all of it
        response = requests.get(url+'.json',headers=data)
        #Create a folder called dogecoinArchive before running the script
        filename=folderName+"/"+comment.name
        obj=open(filename, 'w')
        obj.write(response.text)
        obj.close()
        #print post_json
    for post in subreddit_posts:
        print(post)
        url1= "https://reddit.com" + post.permalink
        #pprint(vars(post))
        data= {'user-agent':'archive by /u/healdb'}
        #manually grabbing this file is much faster than loading the individual json files of every single comment, as this json provides all of it
        if submission.id not in already_done:
            response = requests.get(url1+'.json',headers=data)
            #Create a folder called dogecoinArchive before running the script
            filename=folderName+"/"+post.name
            obj=open(filename, 'w')
            obj.write(response.text)
            obj.close()
            already_done.add(submission.id)
        else:
            continue
def main(startStamp,endStamp,step,folderName,subName,progress):
    if not os.path.exists(folderName):
        os.makedirs(folderName)
    count=step
    try:
        startStamp =open(folderName+"/lastTimestamp.txt").read()
        print("Resuming from timestamp: " + startStamp)
        time.sleep(3)
        startStamp=int(startStamp)
        progress=startStamp
    except: 
        pass
    c=1
    for currentStamp in range(startStamp,endStamp,step):
        e=' --'
        if(c%2==0):
            e=' |'
        f = str(currentStamp)
        g = str(currentStamp+step)
        search_results = r.subreddit(subName).search(b+f+d+g, syntax='cloudsearch')
        end=str((int((float(count)/float(progress)*20.0))*10)/2)+'%'
        print(('\n'*1000)+'Archiving posts and comments...\n['+'*'*int((float(count)/float(progress)*20.0))+'_'*(20-int(float(count)/float(progress)*20.0))+']'+end+e)
        count+=step
        for post in search_results:
            url= "https://reddit.com" + (post.permalink).replace('?ref=search_posts','')
            #pprint(vars(post))
            data= {'user-agent':'archive by /u/healdb'}
            #manually grabbing this file is much faster than loading the individual json files of every single comment, as this json provides all of it
            response = requests.get(url+'.json',headers=data)
            #Create a folder called dogecoinArchive before running the script
            filename=folderName+"/"+post.name+'.json'
            obj=open(filename, 'w')
            obj.write(response.text)
            obj.close()
            #print post_json
            #print("I saved the post and named it " + str(post.name) + " .---")
            time.sleep(1)
        obj=open(folderName+"/lastTimestamp.txt", 'w')
        obj.write(str(currentStamp))
        obj.close()
        c+=1
    print('Welp, all done here! Stopped at timestamp '+ str(currentStamp))
progress = endStamp-startStamp
for i in range(0,len(subreddits_of_interest)):
  t = Thread(target=main, args=(startStamp,endStamp,step,str(subreddits_of_interest[i]+'/'+str(sdate)+'/'+str(edate)),subreddits_of_interest[i],progress))
  t.start()