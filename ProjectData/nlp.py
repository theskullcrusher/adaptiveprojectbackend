import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import json
import re

ps = PorterStemmer()


def contentProcessing(example_sent):
    stop_words = set(stopwords.words('english'))

    #tokenize words from text.
    word_tokens = word_tokenize(example_sent)

    #print(word_tokens)
    #apply stemming to words, select on distinct words.
    word_stem = set()
    for w in word_tokens:
        word_stem.add(w)





    #remove stop words and words choose words >1.
    filtered_sentence = []

    for w in word_stem:
        if w not in stop_words and len(w) > 3 and re.match("^[a-zA-Z_]*$", w):
            filtered_sentence.append(w)
    # print(filtered_sentence)

    #Classifying based on grammer.
    tagged = nltk.pos_tag(filtered_sentence)
    # print(tagged)


    chunkGram = r"""Chunk: {<NN>|<NNPS>|<NNP>}"""
    chunkParser = nltk.RegexpParser(chunkGram)
    chunked = chunkParser.parse(tagged)
    # print (chunked)
    result = []
    for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
        result.append(str(subtree.leaves()[0][0]))
        # print subtree.leaves()[0][0]

    # print (json.dumps(result))
    return result



# namedEnt = nltk.ne_chunk(tagged, binary=True)
# # print (chunked)
# for subtree in namedEnt.subtrees(filter=lambda t: t.label() == 'NE'):
#     print subtree.leaves()[0][0]

# Refrenced: https://pythonprogramming.net/tokenizing-words-sentences-nltk-tutorial/
