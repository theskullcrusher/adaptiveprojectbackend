# This file will parse given csv and generate all JSON. It uses textblob.py to determine the programing language of content and generate tags using tags. txt which contains stackoverflow tags(parsing code is in displayTags.py). 
import csv
import json
import datetime
import nlp
import time
from random import *
import textblb

# NoteCards.csv
#  0-> nid
#  1 -> author_id
#  2 -> type
#  3 -> title
#  4 -> content
# Test Sample
# example_sent = "in a class i can have as many constructors as i want with different argument types. i made all the constructors as private it didn't give any error because my implicit default constructor was public but when i declared my implicit default constructor as private then its showing an error while extending the class.  why?       this works fine         this can not be inherited public class demo4  {     private string name;     private int age;     private double sal;      private demo4(string name  int age) {         this.name=name;         this.age=age;        }      demo4(string name) {         this.name=name;     }      demo4() {         this(\"unknown\"  20);         this.sal=2000;     }      void show(){         system.out.println(\"name\"+name);         system.out.println(\"age: \"+age);     } }  public class demo4  {     private string name;     private int age;     private double sal;      private demo4(string name  int age) {         this.name=name;         this.age=age;     }      demo4(string name) {         this.name=name;     }      private demo4() {         this(\"unknown\"  20);         this.sal=2000;     }      void show() {         system.out.println(\"name\"+name);         system.out.println(\"age: \"+age);     } } "
# answer = nlp.contentProcessing(example_sent)
# print json.dumps(answer)
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
        taggedContent = textblb.contentProcessing(row[4],identifier)
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
