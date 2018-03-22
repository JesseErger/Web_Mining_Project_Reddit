import praw
import pprint
from praw.models import MoreComments
import time
from threading import Thread



subreddits_of_interest = ['depression', 'ChangeMyView', 'InsightfulQuestions', 'SRSDiscussion', 'SuicideWatch', 'PTSD', 'humor', 'funny', 'programmer humor'] 
reddit = praw.Reddit(client_id='0RdYJQZXJWJd6Q',
                     client_secret='OuTKxmRyDO0uxXbxDsODm7q8BRg',
                     password='Thisisjustatemporarypassword123',
                     user_agent='Web_project /u/Reddit_Research_Proj',
                     username='Reddit_Research_Proj')

submission = reddit.submission(id='5lpt8d') 
#You can use this to figure out all of the available fields from a parameter
pprint.pprint(vars(submission))                     
submission_author = str(submission.author)
print("Author of 5lpt8d -> " +  str(submission.author))                    
print("Top level comments from 5lpt8d , author ")
for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    print(top_level_comment.body)
    #You can use this to figure out all of the available fields from a parameter
    print("_____________________________________COMMENT PARAMETERS_____________________________________")
    pprint.pprint(vars(top_level_comment))
    print("_________________________________END COMMENT PARAMETERS_____________________________________")