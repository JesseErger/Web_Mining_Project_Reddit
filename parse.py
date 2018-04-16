import sys
import json
import csv
import os

def parseLineObject_print( data):
    for d in data:
        if (isinstance(d,dict) and 'data' in d.keys()):
            obj =d['data']
            if ('author' in obj.keys()):
                print((obj['author']))
            if ('children' in obj.keys()):
                if isinstance(obj['children'],list) :
                     parseLineObject_print(obj['children'])
            if ('replies' in obj.keys()):
                if isinstance(obj['replies'],dict):
                    parseLineObject_print(obj['replies']['data']['children'])

# data is a list of objects, initially, the list from a single line
def parseLineObject_list( data, result=None):
    if result is None:
        result = []
    for d in data:
        temp = {}
        if (isinstance(d,dict) and 'data' in d.keys()):
            obj =d['data']
            if ('author' in obj.keys()):
                temp['author']=(obj['author'])
            if ('ups' in obj.keys()):
                temp['ups'] = obj['ups']
            if ('downs' in obj.keys()):
                temp['downs'] = obj['downs']
            if temp:
                result.append(temp)
            if ('children' in obj.keys()):
                if isinstance(obj['children'],list) :
                    children = obj['children']
                    result.append(parseLineObject(obj['children']))
            if ('replies' in obj.keys()):
                if isinstance(obj['replies'],dict):
                    children = obj['replies']['data']['children']
                    result.append(parseLineObject(obj['replies']['data']['children']))
    return result
        
# data is a list of objects, initially, the list from a single line
def parseLineObject( data):
    if (isinstance(data,dict) and 'data' in data.keys()):
        return parseLineObject(data['data'])
    if (not isinstance(data,dict)):
        return []
    else:    
        temp = {}
        obj =data
        if ('author' in obj.keys()):
            temp['author']=(obj['author'])
        if ('ups' in obj.keys()):
            temp['ups'] = obj['ups']
        if ('downs' in obj.keys()):
            temp['downs'] = obj['downs']
        temp['children'] = []
        if ('children' in obj.keys()):
            if isinstance(obj['children'],list) :
                children = obj['children']
                for child in children:
                    temp['children'].append(parseLineObject(child))
        if ('replies' in obj.keys()):
            if isinstance(obj['replies'],dict):
                children = obj['replies']['data']['children']
                for child in children:
                    temp['children'].append(parseLineObject(child))
        return temp
        



def processRedditJsonFile(filename):
    data = []
    f = open(filename)
    for line in f:
        data.append(json.loads(line))

    # The forloops only run once usually/ when there is only one line
    # in the file

    lst =[]
    for d in data:
        headPost  = d[0]['data']['children'][0]
        postObj = parseLineObject(headPost)
        postObj['children'] =[]
        restPosts = d[1]['data']['children']
        for post in restPosts:
            postObj['children'].append(parseLineObject(post))
        lst.append(postObj)
    return lst

def RedditJsonFilesToCSV(filenames, newname):
    table =[]
    for filename in filenames :
        lst = processRedditJsonFile(filename)
        jsonObject = lst[0]
        JsonToTable(jsonObject,table)
    with open(newname, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['poster','respondingTo','ups','downs'])
        [writer.writerow(r) for r in table]
       
def JsonToTable(jsonObject,table):
    for child in jsonObject['children']:
        if 'author' in child.keys():
            table.append([child['author'],jsonObject['author'],
                        jsonObject['ups'],jsonObject['downs']])
            JsonToTable(child,table)


def GetFiles():
    changeMyViews = []
    depression = []
    insightfulQuestion = []
    programmerHumor = []
    suicideWatch = []
    funny = []
    humor = []
    ptsd = []
    directory = sys.argv[1]
    for root, dirs, files in os.walk(directory):
        for name in files :
            if name.endswith('json'):
                if ('ChangeMyView' in root):
                    changeMyViews.append(os.path.join(root, name))
                if ('depression' in root):
                    depression.append(os.path.join(root, name))
                if ('funny' in root):
                    funny.append(os.path.join(root, name))
                if ('InsightfulQuestions' in root):
                    insightfulQuestion.append(os.path.join(root, name))
                if ('SuicideWatch' in root):
                    suicideWatch.append(os.path.join(root, name))
                if ('humor' in root):
                    humor.append(os.path.join(root, name))
                if ('PTSD' in root):
                    ptsd.append(os.path.join(root, name))
                if ('ProgrammerHumor' in root):
                    programmerHumor.append(os.path.join(root, name))
    RedditJsonFilesToCSV(changeMyViews, "ChangeMyView.csv")
    RedditJsonFilesToCSV(depression, "depression.csv")
    RedditJsonFilesToCSV(insightfulQuestion, "insightfulQuestion.csv")
    RedditJsonFilesToCSV(programmerHumor, "programmerHumor.csv")
    RedditJsonFilesToCSV(suicideWatch, "suicideWatch.csv")
    RedditJsonFilesToCSV(funny, "funny.csv")
    RedditJsonFilesToCSV(ptsd, "ptsd.csv")
    RedditJsonFilesToCSV(humor, "humor.csv")


GetFiles()
#lst = processRedditJsonFile(filename)
#print(lst[0])
"""
top_posts =[]
for json_line in lst:
    top_posts.append(json_line[0])
    original_author = json_line[0][0]['author']
    for reply_thread in json_line[1]:
        if isinstance(reply_thread,dict):
            reply_thread['reply_to']= original_author
        else:
            reply_thread[0]['reply_to']= original_author
"""
#for l in lst[0]:
#    print(l)
#    print("-----")
            
# print(lst)
#print(top_posts)        
