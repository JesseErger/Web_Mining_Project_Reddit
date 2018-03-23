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
from threading import Thread
import threading
start_day = 1
end_day = 31
year = 2017
step=350
subreddits_of_interest = ['depression', 'ChangeMyView', 'InsightfulQuestions', 'SRSDiscussion', 'SuicideWatch', 'PTSD', 'humor', 'funny', 'ProgrammerHumor'] 
app_secrets = [ "U11Lejz0vUGwskUj17NHRB0y6Mo" , "jokvG1pEvFYbrs0cEfHuwbjqpco", "pNPbUrPn8mq537vXOBa5D-dQ1JY", "bLASZva09euXiNFVqjlnMRKjZnw", "TlaIxjZK6L0bX-U6zSZanAvYguI" , "K12FC8IJ3xF7SACyo-A0CUXR2nQ", "dGWuaPfKaUQp-wgv7jDV2Nu0p84" ,"seAe1eGqTDSfjxtA_7lxeROWzic", "8ueVFhNN2P-Irg2diYsQ8awxHOs"]
app_id= [ "8H3kt43FJR3nGg" , "AelDLFxJ063apA", "V4bkiWGUrZvgWA", "DbcEpdhMkoD4iA",  "6Y-NF5Sx9lKQSQ", "QOjCI9bUHXN-EA", "q-D7XhUPFBiBmQ", "2WCylr6Eae6BaQ", "QTUpz5jwRQ1FBA"]

subreddits_of_interest = ['depression', 'ChangeMyView', 'InsightfulQuestions', 'SRSDiscussion', 'SuicideWatch', 'PTSD', 'humor', 'funny', 'ProgrammerHumor'] 
def start(sub,r,i):
    sub_1 = threading.local() 
    r_1 = threading.local() 
    i_1 = threading.local() 
    sub_1.i = sub
    r_1.i = r
    i_1.i = i
    for month in range(1,13):
      month_1 = threading.local()
      month_1.i = month
      start_date = threading.local()
      end_date = threading.local()
      startStamp = threading.local()
      endStamp = threading.local()
      sdate = threading.local() 
      edate = threading.local()
      client_secret = threading.local()
      progress = threading.local()
      folderName = threading.local()
      
      start_date.i = "01"+"/"+str(month_1.i).zfill(2)+"/"+str(year)
      end_date.i = str(end_day)+"/"+str(month_1.i).zfill(2)+"/"+str(year)
      startStamp.i= int(time.mktime(datetime.datetime.strptime(start_date.i, "%d/%m/%Y").timetuple()))
      endStamp.i = int(time.mktime(datetime.datetime.strptime(end_date.i, "%d/%m/%Y").timetuple()))
      sdate.i =datetime.datetime.fromtimestamp(int(startStamp.i)).strftime('%d-%m-%Y')
      edate.i =datetime.datetime.fromtimestamp(int(endStamp.i)).strftime('%d-%m-%Y')
      progress.i = endStamp.i-startStamp.i
      folderName.i =str(sub_1.i+'_'+str(sdate.i)+'_'+str(edate.i))
      if not os.path.exists(folderName.i):
        os.makedirs(folderName.i)
      json_extract.main(startStamp.i,endStamp.i,step,folderName.i,sub_1.i,progress.i,r_1.i,i_1.i)


for i in range(0,len(subreddits_of_interest)):
  client_id = threading.local()
  client_secret = threading.local()
  r = threading.local()
  client_secret.i = app_secrets[i]
  client_id.i = app_id[i]
  r.i = praw.Reddit(client_id=client_id.i,
                     client_secret=client_secret.i,
                     user_agent='Thread' +'_'+ str(i) +' /u/Reddit_Research_Proj',
                     username='Reddit_Research_Proj')
  sub = threading.local()
  sub.i = subreddits_of_interest[i]
  t = Thread(target=start, args=(sub.i,r.i,i))
  t.start()


'''
subreddits_of_interest = ['depression', 'ChangeMyView', 'InsightfulQuestions', 'SRSDiscussion', 'SuicideWatch', 'PTSD', 'humor', 'funny', 'ProgrammerHumor'] 
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




