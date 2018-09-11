#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on Feb 27, 2018

Course work: 

@author: raja

Source:
    https://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file
    https://stackoverflow.com/questions/40325980/how-is-the-vader-compound-polarity-score-calculated-in-python-nltk
    https://stackoverflow.com/questions/tagged/vader
    https://github.com/cjhutto/vaderSentiment
    https://pypi.python.org/pypi/vaderSentiment/0.5
    https://web.stanford.edu/~jurafsky/pubs/neutrality.pdf
    https://stackoverflow.com/questions/370357/python-variable-scope-error
    https://stackoverflow.com/questions/26045779/python-how-to-turn-all-numbers-in-a-list-into-their-negative-counterparts
    http://www.nltk.org/_modules/nltk/sentiment/vader.html
    
    https://github.com/cjhutto/vaderSentiment
    
Cite:
    Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
    Sentiment Analysis of Social Media Text. Eighth International Conference on
    Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
'''

# Import necessary modules
import json
from pprint import pprint
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = [
    'Plenty of opportunity learn, Obviously self learning is important and so many documentation available.',
    'Though plivo provide periodic training, but self learning gets you fast.',
    'Flexible timing and excellent office environment.',
    'Management really cares for the people and benefits are good in the industry.',    
]

#twt = data['tweets'][1]['text']

sid = SentimentIntensityAnalyzer()

def get_sentiment(sentence):
        
    print(sentence)

    ss = sid.polarity_scores(sentence)
    
    #print(type(ss['pos']))

    positive_meter = round((ss['pos'] * 10), 2) 
    negative_meter = round((ss['neg'] * 10), 2)
    
    '''
    for k in sorted(ss):
        #print(ss)
        print('{0}: {1}, '.format(k, ss[k]), end = '')
    '''
    
    print('positive : {0}, negative : {1}'.format(positive_meter, negative_meter))
    
    print()    

    
def main():    
    #print(data)
    
    contents = data
    
    total_contents = len(contents)
    for x in range(total_contents):
        get_sentiment(contents[x])
        print('---')
        #print(contents[x])        
        
    
if __name__ == '__main__':
    main()