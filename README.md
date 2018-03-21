﻿# Group Project Web_Mining_Project


@Authors Jesse Erger, Linh Pham, Reilly Grant
Repo is for processing data from Reddit for a group project at the University of Iowa.

Use pip install to install the praw library

Use: To use the file spliter -  update the path "path_to_data_files" in split_up_files.py to the directory where the full size data files are stored.

Run split_up_files to convert them into more manageable file sizes (python filename from the command line).


The reddit extract is just an example of how we can obtain the comments from threads, all we need to do is parse the data files for the reddit.submission(id='XXXXXX') Which is included in our data set.
It does seem that there are a lot of posts that have been deleted, and posts in categories that are not of our concern. In addition there appears to be an issue when reading from the files and the language is in an unknown format
I have yet to fix this (probably need to do some encoding/decoding), but figured this will give us somewhere to start.

TODO: We will want to parse these files and was can extract the all the comments based on the thread IDs - we will need to figure out the posts that were actually within the sub-reddits that we want. I have no problem doing all of this but figured that I'd let you guys plan around with it a bit. Any questions or concerns please let me know. - Also you may want to set up your own Reddit Oauth like I did in reddit_extract, but you can use mine in the menatime if it works for you. https://praw.readthedocs.io/en/latest/getting_started/authentication.html#script-application was quite helpful in getting started on the API.


