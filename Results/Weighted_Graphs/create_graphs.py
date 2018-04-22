import os
import csv

#Author Jesse Erger
from random import *
def create_nodes(node_name, reddit_label, file):
    file.write("  node\n  [\n    id "+str(node_name)+"\n    label \""+str(reddit_label)+"\"\n  ]\n")

def create_edge(source,target,file,weight = 0,weighted = False):
  if(weighted):
    file.write("  edge\n  [\n    source "+str(source)+"\n    target "+str(target)+"\n    value "+str(weight)+"\n  ]\n")
  else:
    file.write("  edge\n  [\n    source "+str(source)+"\n    target "+str(target)+"\n  ]\n")

directed = True

root_dir = r'C:\Users\new user\Desktop\Git_Repos\Web_Mining_Project_Reddit\\'
subreddit_dict = {} #contains all the posts  for all years indexed by sub reddit name
active_posters_dict = {} #contains a set of users who have made a post in a subreddit - ['subreddit'] = {user1,user2,...}
active_responders_dict = {} #contains a set of users who have made a reply to a post in a subreddit - ['subreddit'] = {user1,user2,...}
users_who_replied = {} #list of users to replied to user (['user'] = [responder,#times],[responder,#times],...)
for folder, dirs, files in os.walk(root_dir):
    if("processed" in folder.split('_')):
        for folder, dirs, files in os.walk(folder):
            for file in files:
                with open(folder+r'\\'+file,'r') as csvfile_in:
                    csv_reader = csv.reader(csvfile_in,delimiter=',')
                    for row in csv_reader:
                      if(not "respondingTo" in row):
                        try:
                            subreddit_dict[file.split('_')[0]].append(row)
                        except:
                            subreddit_dict[file.split('_')[0]] = [row]
for sub_reddit in subreddit_dict.keys():
    active_posters_dict[sub_reddit] = {}
    for post in subreddit_dict[sub_reddit]:
        try:
            active_posters_dict[sub_reddit][post[0]][post[1]][1] += 1
        except:
            try:
                active_posters_dict[sub_reddit][post[0]][post[1]].append(([post[1],1]))
            except:
                try:
                    active_posters_dict[sub_reddit][post[0]][post[1]] = ([post[1],1])
                except:
                    active_posters_dict[sub_reddit][post[0]] = {}
                    active_posters_dict[sub_reddit][post[0]][post[1]] = ([post[1],1])
for subreddit in active_posters_dict.keys():
    processed_out = open(subreddit+"_Graph"+".gml",'w')
    processed_out.write("Creator \"Jesse Erger\"\ngraph\n[\n  directed "+str(int(directed))+"\n")
    for replyer in active_posters_dict[subreddit]:
        create_nodes(str(replyer),subreddit,processed_out)
    for replyer in active_posters_dict[subreddit]:
        for reply in active_posters_dict[subreddit][replyer]:
            replied_to = active_posters_dict[subreddit][replyer][reply][0]
            num_replies = active_posters_dict[subreddit][replyer][reply][1]
            create_edge(replyer,replied_to,processed_out,weight=num_replies,weighted=True)
            #print(active_posters_dict[subreddit][replyer][reply])
        #print(str(replyer) + " -> " +str(active_posters_dict[subreddit][replyer]))
        #processed_out.write(str(replyer) + " -> " +str(active_posters_dict[subreddit][replyer])+'\n\n\n')
    processed_out.write("]")
    processed_out.close()
'''
for subreddit in active_posters_dict.keys():
    processed_out = open(subreddit+"_User_NumPosts_AvgUpvote.csv",'w')
    processed_out.write("Author_of_Posts, Number_of_Posts, Average_Up_Votes\n")
    processed_out.write("Unique Users -> "+str(len(active_posters_dict[subreddit]))+"\n")
    for author in active_posters_dict[subreddit]:
        avg_upvotes = list(set(active_posters_dict[subreddit][author]))
        processed_out.write(str(author) + ' , ' + str(len(avg_upvotes)) + ' , ' + str(float(sum(avg_upvotes))/float(len(avg_upvotes)))+'\n')
        

for sub_reddit in subreddit_dict.keys():
    for post in subreddit_dict[sub_reddit]:
        try:
            active_posters_dict[sub_reddit][post[1]].append(int(post[2]))
        except:
            try:
                active_posters_dict[sub_reddit][post[1]] = ([int(post[2])])
            except:
                active_posters_dict[sub_reddit] = {}
                active_posters_dict[sub_reddit][post[1]] = ([int(post[2])])
        try:
            active_responders_dict[sub_reddit].add(post[0])
        except:
            active_responders_dict[sub_reddit] = set(post[0])

for subreddit in active_posters_dict.keys():
    processed_out = open(subreddit+"_User_NumPosts_AvgUpvote.csv",'w')
    processed_out.write("Author_of_Posts, Number_of_Posts, Average_Up_Votes\n")
    processed_out.write("Unique Users -> "+str(len(active_posters_dict[subreddit]))+"\n")
    for author in active_posters_dict[subreddit]:
        avg_upvotes = list(set(active_posters_dict[subreddit][author]))
        processed_out.write(str(author) + ' , ' + str(len(avg_upvotes)) + ' , ' + str(float(sum(avg_upvotes))/float(len(avg_upvotes)))+'\n')
'''