# This file will parse given csv and generate all JSON. It uses textblob.py to determine the programing language of content and generate tags using tags. txt which contains stackoverflow tags(parsing code is in display).
from textblob import TextBlob
from textblob.np_extractors import ConllExtractor
from guesslang import Guess
import csv
import json
import datetime
import nlp
import time
from random import *
import textblb
import requests
import re

# NoteCards.csv
#  0-> nid
#  1 -> author_id
#  2 -> type
#  3 -> title
#  4 -> content

#parse notecards.csv file and store all cards into 532 json files. later call mergeJson to create cards.json as single content file.
def parseCSVFile():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    # print st

    json_struct = {"nId": "", "userId": "", "type": "", "title": "", "content": "", "upVote": 0, "downVote": 0, "tags": [], "favorite" : False, "dateCreated": st, "dateModified": st}
    #print json_struct
    count = 0
    identifier = set()
    with open('tags.txt','r') as inF:
        for line in inF:
            identifier.add(line.strip())
    print ("File read complete")

    with open('notecards.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            json_struct['nId'] = row[0]
            json_struct['userId'] = row[1]
            json_struct['type'] = row[2]
            json_struct['title'] = row[3]
            json_struct['content'] = row[4]
            taggedContent = contentProcessing(row[4],identifier)
            json_struct['tags'] = taggedContent
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            json_struct['dateCreated'] = st
            json_struct['dateModified'] = st
            # json_struct['upVote'] = randint(1,50)
            # json_struct['downVote'] = randint(1,20)

            if "NULL" != row[3] and row[4] != "NULL":
                count = count +1
                print (count)
                #Create File Name.
                fileName = str(count)+'.json'
                print (fileName)

                #Open new JSON file and store CSV as JSON.
                with open(fileName, 'w') as fp:
                    json.dump(json_struct, fp)

                print(json.dumps(json_struct, indent=4))
    return

# This function generates tags for given content with 0th index tag being the Programming language
# Guessed from card content.
def contentProcessing(example_sent,identifier):
        tags = []
        name = Guess().language_name(example_sent)
        tags.append(name)
        text = TextBlob(example_sent)
        print ("Noun phrases",text.noun_phrases)
        nphrases = text.noun_phrases
        # print ("Extractor Noun", nphrases)
        # print ("language", name)
        valid_nouns = set()

        for nun in nphrases:
            if nun in identifier:
                valid_nouns.add(nun)
        if len(valid_nouns) != 0:
            tags += valid_nouns

        # print (tags)
        return tags

# This function will store all tags from tags.txt file and store in form of set.
def getTags():
    identifier = set()
    with open('tags.txt','r') as inF:
        for line in inF:
            identifier.add(line.strip())
    print ("File read complete")

# merge all json files into single file, cards.json.
def mergeJson():
    jsonList = []
    for i in range(1,532):
        file = str(i) + ".json"
        with open(file) as fp:
            data = json.load(fp)
            jsonList.append(data)
            print data["tags"]


    with open("cards.json","w") as fp:
        json.dump(jsonList, fp, indent =2)


# This function is used to analyze tags generated for all 531 Cards.
def displayTags():
    for i in range(532):
        if i == 0:
            continue
        file = str(i) + ".json"
        with open(file) as fp:
            data = json.load(fp)
            print data["tags"]

# This function will write all tags from stackoverflow site into tags.txt file in append mode.
def getStackOverflowTags():
    with open("tags.txt","a") as fp:
        for i in range(0,2000):
            i = i+1
            print "page", i
            url = "https://api.stackexchange.com//2.2/tags?page="+str(i)+"&pagesize=100&order=desc&sort=popular&site=stackoverflow&key=uY1y6v5RlMRidvLO1Zi0Ag(("
            res = requests.get(url)
            data = json.loads(res.text)
            print "Quota remaining", data["quota_remaining"]
            print "has mode", data["has_more"]
            for doc in data["items"]:
                val = doc["name"]
                fp.write(val + "\n")
