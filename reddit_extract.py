import praw
import pprint
from praw.models import MoreComments
import time
from threading import Thread
import threading
import os
import codecs
subreddits_of_interest = ['depression', 'ChangeMyView', 'InsightfulQuestions', 'SRSDiscussion', 'SuicideWatch', 'PTSD', 'humor', 'funny', 'ProgrammerHumor'] 
reddit = praw.Reddit(client_id='0RdYJQZXJWJd6Q',
                     client_secret='OuTKxmRyDO0uxXbxDsODm7q8BRg',
                     password='Thisisjustatemporarypassword123',
                     user_agent='Web_project /u/Reddit_Research_Proj',
                     username='Reddit_Research_Proj')

def get_replies_from_posts(post_ids,subName):
    users_who_respon = threading.local()
    users_who_respon.x = {}
    for post in post_ids:
      reply = reddit.submission(id=post)
      folderName = threading.local()
      folderName.i = str(subName+'/'+str(reply.author))
      if not os.path.exists(folderName.i):
        os.makedirs(folderName.i)
      
      filename=folderName.i+"/"+str(reply.author)+"_"+str(post)+".csv"
      obj=open(filename, 'a') 
      for top_level_comment in reply.comments:
        if isinstance(top_level_comment, MoreComments):
          continue
        obj.write((str(top_level_comment.author) +"," +str(codecs.encode(top_level_comment.body, encoding='utf-8', errors='ignore')) +'\n'))     
def generate_posts_file(subreddit_name, num_posts):
    post_id = threading.local()
    post_id.x = []

    Authors_Dict_Posts = {}
    fp_t = open(subreddit_name+".csv",'a')
    for submission in reddit.subreddit(subreddit_name).hot(limit=num_posts):
       #print("Author ->" + str(submission.author) + "Submission title" + submission.title)
       Authors_Dict_Posts[submission.id]=[submission.subreddit_name_prefixed ,str(submission.author), submission.id, submission.distinguished, submission.ups, submission.downs, submission.mod_reports, submission.num_comments, submission.url]
    header = "Subreddit Name, Posters Username, Post ID, Moderator, Up Votes, Down Votes, Reported Post by Moderator, Number of comments, URL to post\n"
    fp_t.write(header)
    for key in Authors_Dict_Posts:
      post_id.x.append(key)
      entry = ""
      for item in Authors_Dict_Posts[key]:
        entry += str(item)+","
      fp_t.write(entry.strip(',')+'\n')
      get_replies_from_posts(post_id.x,subreddit_name)



if not os.path.exists("Reddit_Replies"):
    os.makedirs("Reddit_Replies")
for i in range(0,len(subreddits_of_interest)):
  t = Thread(target=generate_posts_file, args=(subreddits_of_interest[i],1000))
  t.start()
'''
for sr in subreddits_of_interest:
  generate_posts_file(sr,1000)
#print(reddit.subreddit('depression').stream)

#get a single submission    
print("_____________________________________SUBMISSION PARAMETERS_____________________________________")
submission = reddit.submission(id='5lpt8d') 
#You can use this to figure out all of the available fields from a parameter
pprint.pprint(vars(submission))
print("_________________________________END SUBMISSION PARAMETERS_____________________________________")


submission_author = str(submission.author)
print("Author of 5lpt8d -> " +  str(submission.author))

#Get top level comments in a thread
print("Top level comments from 5lpt8d , author ")
for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    print(top_level_comment.body)
    #You can use this to figure out all of the available fields from a parameter
    print("_____________________________________COMMENT PARAMETERS_____________________________________")
    pprint.pprint(vars(top_level_comment))
    print("_________________________________END COMMENT PARAMETERS_____________________________________")
'''