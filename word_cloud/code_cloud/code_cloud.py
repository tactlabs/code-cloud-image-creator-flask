#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on Aug 26, 2017

Course work: NLP

@author: raja

source:
    https://github.com/amueller/word_cloud/tree/master/examples
'''

# Import necessary modules
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

from wordcloud import WordCloud, STOPWORDS

# get data directory
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'code2.txt')).read()

# read the mask image
image_base = np.array(Image.open(path.join(d, "s14.png")))

stopwords = set(STOPWORDS)

wc = WordCloud(background_color="white", max_words=2500, mask=image_base,
               stopwords=stopwords, contour_width=3, contour_color='steelblue')

# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "output.png"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(image_base, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()



