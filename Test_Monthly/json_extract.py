# -*- coding: utf-8 -*-
import time
import datetime
import praw
import os
import traceback
import requests
b = "timestamp:"
d = ".."

#Config Details-

subreddits_of_interest = ['depression', 'ChangeMyView', 'InsightfulQuestions', 'SRSDiscussion', 'SuicideWatch', 'PTSD', 'humor', 'funny', 'ProgrammerHumor'] 


'''
startStamp= int(time.mktime(datetime.datetime.strptime("01/01/2018", "%d/%m/%Y").timetuple()))
endStamp= int(time.mktime(datetime.datetime.strptime("03/03/2018", "%d/%m/%Y").timetuple()))
sdate=datetime.datetime.fromtimestamp(int(startStamp)).strftime('%d-%m-%Y')
edate=datetime.datetime.fromtimestamp(int(endStamp)).strftime('%d-%m-%Y')

step=350
for month in range(1,13): 
  for sub in subreddits_of_interest:
    start_date = "01"+"/"+str(month).zfill(2)+"/"+str(year)
    end_date = str(end_day)+"/"+str(month).zfill(2)+"/"+str(year)
    startStamp= int(time.mktime(datetime.datetime.strptime(start_date, "%d/%m/%Y").timetuple()))
    endStamp= int(time.mktime(datetime.datetime.strptime(end_date, "%d/%m/%Y").timetuple()))
    sdate=datetime.datetime.fromtimestamp(int(startStamp)).strftime('%d-%m-%Y')
    edate=datetime.datetime.fromtimestamp(int(endStamp)).strftime('%d-%m-%Y')
    progress = endStamp-startStamp
  folderName=str(sub+'_'+str(sdate)+'_'+str(edate))
  if not os.path.exists(folderName):
    os.makedirs(folderName)
  json_extract.main(startStamp,endStamp,step,folderName,sub,progress)
'''
    
def main(startStamp,endStamp,step,folderName,subName,progress,r,tid):
    count=step
    c=1
    for currentStamp in range(startStamp,endStamp,step):
        e=' --'
        if(c%2==0):
            e=' |'
        f = str(currentStamp)
        g = str(currentStamp+step)
        search_results = r.subreddit(subName).search(b+f+d+g, syntax='cloudsearch')
        end=str((int((float(count)/float(progress)*20.0))*10)/2)+'%'
        #print(('\n'*1000)+'Archiving posts and comments...\n['+'*'*int((float(count)/float(progress)*20.0))+'_'*(20-int(float(count)/float(progress)*20.0))+']'+end+e)
        count+=step
        for post in search_results:
          try:
            #print("---I found a post! It\'s called:" + str(post))
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
            print(str(tid) + "Made a file in" + folderName)
          except:
            continue
        obj=open(folderName+"/lastTimestamp.txt", 'w')
        obj.write(str(currentStamp))
        obj.close()
        c+=1
    print('Welp, all done here! Stopped at timestamp '+ str(currentStamp))
    filename=folderName+"/"+"___Finished"+'.txt'
    obj=open(filename, 'w')
    obj.write("DONE")
    obj.close()
'''
progress = endStamp-startStamp
index = 0
folderName=str(subreddits_of_interest[index]+'_'+str(sdate)+'_'+str(edate))
if not os.path.exists(folderName):
  os.makedirs(folderName)
main(startStamp,endStamp,step,folderName,subreddits_of_interest[index],progress)


for i in range(0,len(subreddits_of_interest)):
  folderName=str(subreddits_of_interest[i]+'_'+str(sdate)+'_'+str(edate))
  if not os.path.exists(folderName):
    os.makedirs(folderName)
  main(startStamp,endStamp,step,folderName,subreddits_of_interest[i],progress)
'''