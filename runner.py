#Author Jesse Erger
import json_extract
# -*- coding: utf-8 -*-
import time
import datetime
import praw
import os
import traceback
import requests
b = "timestamp:"
d = ".."
from threading import Thread, RLock
import threading

#['depression', 'ChangeMyView', 'InsightfulQuestions', 'SRSDiscussion', 'SuicideWatch', 'PTSD', 'humor', 'funny', 'ProgrammerHumor'] 

#**********************_____________________________________________TUNEABLE PARAMETERS_____________________________________________**************************

year_range = [2014,2015] #Left inclusive right exclusive.
month_range = [1,12] #Inclusive
max_threads = 100
b = "timestamp:"
d = ".."

subreddits_of_interest = ['depression', 'ChangeMyView', 'InsightfulQuestions', 'SRSDiscussion', 'SuicideWatch', 'PTSD', 'humor', 'funny', 'ProgrammerHumor'] #['PTSD', 'InsightfulQuestions', 'ChangeMyView']

#(Could add more/ different reddit user apps as it may run faster)
app_secrets = [ "U11Lejz0vUGwskUj17NHRB0y6Mo" , "jokvG1pEvFYbrs0cEfHuwbjqpco", "pNPbUrPn8mq537vXOBa5D-dQ1JY", "bLASZva09euXiNFVqjlnMRKjZnw", "TlaIxjZK6L0bX-U6zSZanAvYguI" , "K12FC8IJ3xF7SACyo-A0CUXR2nQ", "dGWuaPfKaUQp-wgv7jDV2Nu0p84" ,"seAe1eGqTDSfjxtA_7lxeROWzic", "8ueVFhNN2P-Irg2diYsQ8awxHOs"]
app_id= [ "8H3kt43FJR3nGg" , "AelDLFxJ063apA", "V4bkiWGUrZvgWA", "DbcEpdhMkoD4iA",  "6Y-NF5Sx9lKQSQ", "QOjCI9bUHXN-EA", "q-D7XhUPFBiBmQ", "2WCylr6Eae6BaQ", "QTUpz5jwRQ1FBA"]


#Add all subreddits that you want to run this on in the dictionary below. If you would like to change the years or month ranges outside of month_range and year_range above, you can manually do it below. See "FAKE_ENTRY for an example. 
start_months_target_month_year={     
    'SRSDiscussion':[month_range[0],month_range[1],year_range[0],year_range[1]],
    'humor':[month_range[0],month_range[1],year_range[0],year_range[1]],
    'PTSD':[month_range[0],month_range[1],year_range[0],year_range[1]],
    'depression': [month_range[0],month_range[1],year_range[0],year_range[1]],
    'ProgrammerHumor':[month_range[0],month_range[1],year_range[0],year_range[1]],
    'SuicideWatch':[month_range[0],month_range[1],year_range[0],year_range[1]], 
    'ChangeMyView': [month_range[0],month_range[1],year_range[0],year_range[1]],
    'InsightfulQuestions':[month_range[0],month_range[1],year_range[0],year_range[1]],
    'funny':[month_range[0],month_range[1],year_range[0],year_range[1]],
    'FAKE_ENTRY': [1,12,2005,2010],
}

#If you want to look at data for example just the first week of the month you can change it here. Or if you want data for the current month change the second number to todays date.
num_days_in_month={
 '1': [1,31],
 '2': [1,28], #if you want to figure out the data on leap years, you can fix this yourself.
 '3': [1,31],
 '4': [1,30],
 '5': [1,31],
 '6': [1,30],
 '7': [1,31],
 '8': [1,31],
 '9': [1,30],
 '10': [1,31],
 '11': [1,30],
 '12': [1,31],
}

#**************************_________________________________________END TUNEABLE PARAMETERS_____________________________________________******************************


threads_arr = []
step=350   
def start_threadin(sub,r,my_id):
    
    idd = threading.local()
    sub_1 = threading.local()
    sub_1.i = sub
    idd.i = my_id
    client_id = threading.local()
    client_secret = threading.local()
    r_1 = threading.local() 
    r_1.i = r
    while(True):
        Lock = threading.RLock(blocking=1)
        Lock.acquire()
        month_1 = threading.local()
        month_1.i = start_months_target_month_year[sub_1.i][0]
        new_month = False
        new_sub = False
        new_year = False
        #Get next month for same sub reddit
        if((start_months_target_month_year[sub_1.i][0] < start_months_target_month_year[sub_1.i][1])):
          month_1.i = start_months_target_month_year[sub_1.i][0]
          start_months_target_month_year[sub_1.i][0] += 1
          new_month = True 
          Lock.release()
          break
        #check if other subs need help with their months
        elif(not new_month):        
          for sub in subreddits_of_interest: 
            if((start_months_target_month_year[sub][0] < start_months_target_month_year[sub][1])):
              sub_1.i = sub
              month_1.i = start_months_target_month_year[sub_1.i][0] 
              start_months_target_month_year[sub_1.i][0] += 1
              new_sub = True
              Lock.release()
              break
        #if no help is needed on the other subs, see if there is a year range and update the year for this sub reddit
        elif( (start_months_target_month_year[3] != start_months_target_month_year[4]+1) and not new_month and not new_sub):
          #update the sub information in the start_months_target_month_year discretionary.
          start_months_target_month_year[sub_1.i][0] = month_range[0]
          start_months_target_month_year[sub_1.i][1] = month_range[1]
          start_months_target_month_year[sub_1.i][2] += 1
          new_year = True
          Lock.release()
        else:
          Lock.release()
          threads.remove(t)
          try:
            t.exit()
          except:
            print("Killed thread")         
          
        year = threading.local()
        year.i = start_months_target_month_year[sub_1.i][2]
        start_date = threading.local()
        end_date = threading.local()
        startStamp = threading.local()
        endStamp = threading.local()
        sdate = threading.local() 
        edate = threading.local()
        client_secret = threading.local()
        progress = threading.local()
        folderName = threading.local()
        folderName.i = ""
        end_date.i = num_days_in_month[str(month_1.i)][1]
        start_date.i =str(num_days_in_month[str(month_1.i)][0])+"/"+str(month_1.i).zfill(2)+"/"+str(year.i)
        end_date.i = str(num_days_in_month[str(month_1.i)][1])+"/"+str(month_1.i).zfill(2)+"/"+str(year.i)
        startStamp.i= int(time.mktime(datetime.datetime.strptime(start_date.i, "%d/%m/%Y").timetuple()))
        endStamp.i = int(time.mktime(datetime.datetime.strptime(end_date.i, "%d/%m/%Y").timetuple()))
        try:  
          sdate.i =datetime.datetime.fromtimestamp(int(startStamp.i)).strftime('%d-%m-%Y')
          edate.i =datetime.datetime.fromtimestamp(int(endStamp.i)).strftime('%d-%m-%Y')
          progress.i = endStamp.i-startStamp.i
        except Exception as e:
          print(e)
        try:       
          folderName.i = str(str(year.i)+'/'+sub_1.i+ '/' +sub_1.i+ '_'+str(sdate.i)+'_'+str(edate.i))
        except Exception as e:
          print(e)
          break
          continue
        try:       
          if not os.path.exists(folderName.i):
            os.makedirs(folderName.i)
        except:
           continue
        count = step
        c = threading.local()
        c.i = 1
        for currentStamp in range(startStamp.i,endStamp.i,step):
            e=' --'
            if(c.i%2==0):
                e=' |'
            f = threading.local()
            g = threading.local()
            f.i = str(currentStamp)
            g.i = str(currentStamp+step)
            search_results =threading.local()
            search_results.i = r_1.i.subreddit(sub_1.i).search(b+f.i+d+g.i, syntax='cloudsearch')
            count+=step
            for post in search_results.i:
              try:
            
                url = threading.local()
                url.i = "https://reddit.com" + (post.permalink).replace('?ref=search_posts','')
                data= {'user-agent':'archive by /u/healdb'}
                response = threading.local()
                response.i = requests.get(url.i+'.json',headers=data)
                filename = threading.local()
                filename.i=folderName.i+"/"+post.name+'.json'
                print("File created @ "+filename.i)
                obj_d = threading.local()
                obj_d=open(filename.i, 'w')
                obj_d.write(response.i.text)
                obj_d.close()
                time.sleep(1)
              except:
                continue
            c.i+=1
        #print('Welp, all done here! Stopped at timestamp '+ str(currentStamp))
        filename_f = threading.local()
        filename_f.i= str(folderName.i)+"/"+"___Finished"+'.txt'
        obj_d = threading.local()
        obj_d.i=open(filename_f.i, 'w')
        obj_d.i.write("DONE")
        obj_d.i.close()
num_months_sub = {}
num_months = 0

for sub in subreddits_of_interest:
  num_months_sub[sub] = (start_months_target_month_year[sub][1]-start_months_target_month_year[sub][0]) + 1
  num_months += (start_months_target_month_year[sub][1]-start_months_target_month_year[sub][0])+1
num_years = year_range[1]-year_range[0]
#create a thread for each month we want to process, at most 100
print(num_months)
for subs in subreddits_of_interest:
  for j in range(0,num_months_sub[subs]*num_years):
    my_id = threading.local()
    my_id.i = "Thread_" + str(j) + subs
    sub = threading.local()
    sub.i = subs
    client_id = threading.local()
    client_secret = threading.local()
    r = threading.local()
    client_secret.i = app_secrets[(j+3)%(len(app_secrets)-1)] # spread accross the Reddit apps
    client_id.i = app_id[(j+3)%(len(app_secrets)-1)]
    r.i = praw.Reddit(client_id=client_id.i,
                       client_secret=client_secret.i,
                       user_agent='Thread' +'_'+ str(j) +' /u/Reddit_Research_Proj',
                       username='Reddit_Research_Proj')
    t = Thread(target=start_threadin, args=(sub.i,r.i,my_id.i))
    threads_arr.append(t)
    t.start()
print(len(threads_arr))






