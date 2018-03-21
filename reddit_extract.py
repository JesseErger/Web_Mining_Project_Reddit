import praw
import pprint
from praw.models import MoreComments

reddit = praw.Reddit(client_id='0RdYJQZXJWJd6Q',
                     client_secret='OuTKxmRyDO0uxXbxDsODm7q8BRg',
                     password='Thisisjustatemporarypassword123',
                     user_agent='Web_project /u/Reddit_Research_Proj',
                     username='Reddit_Research_Proj')


#An example of one submission's comments. We can extract all the post ids from the log files but it seems like A LOT of them are deleted. I'm not sure if my credentials will work for you above where I set up the reddit authorization, and I'm not sure what their limits are on extracting this data. I'm sure there is a lot more we can do with the API but figured I would just get something started.                     
                                        
#Can get all the titles of a sub-reddit just up the limit
for submission in reddit.subreddit('depression').hot(limit=10):
   print("Author ->" + str(submission.author))
   print(submission.title)

   
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