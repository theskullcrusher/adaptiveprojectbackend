from textblob import TextBlob
from textblob.np_extractors import ConllExtractor
from guesslang import Guess
import json
import re

# identifier = set()
# with open('tags.txt','r') as inF:
#     for line in inF:
#         identifier.add(line.strip())
# print ("File read complete")
# print (identifier)
# extractor = ConllExtractor()
# for i in range(1,3):
#     file = str(i) +".json"
#     with open(file) as fp:
#         tags = []
#         data = json.load(fp)
def contentProcessing(example_sent,identifier):
        tags = []
        name = Guess().language_name(example_sent)
        tags.append(name)
        text = TextBlob(example_sent)

        # text2 = TextBlob(data["content"], np_extractor=extractor)
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

        print (tags)
        return tags
