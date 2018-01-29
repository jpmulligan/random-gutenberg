# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 20:02:44 2018

@author: jpmul
"""
import string
import markovify

from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers


# This is an unused function to generate the top N words
# Could use this to make a nice histogram
# Method based on Think Python exercise
def top_words(text, n):
        
    hist = dict()
    
    for line in text.split('\n'):
        line = line.replace('-', ' ')
    
        for word in line.split():
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()
            hist[word] = hist.get(word, 0) + 1
            
    print("Total words:\t", sum(hist.values()))
    print("Unique words:\t", len(hist))
    
    t = []
    for key, value in hist.items():
        t.append((value, key))
    t.sort(reverse=True)
    for word, count in t[:n]:
        print(word, count)

# Here are some book IDs from Project Gutenberg
# Orthodoxy 130
# What's Wrong with the World 1717
# Heretics 470
# All Things Considered 11505
# Tremendous Trifles 8092
# Pride and Prejudice 1342
# Alice's Adventures in Wonderland 11
# Dracula 345        
# Moby Dick 2701
# Kama Sutra 27827        

#books = [27827]
books = [130, 1717, 470, 11505, 8092]
text = ''

print(f"Loading {len(books)} book(s) from Project Gutenberg...")
for book in books:
    text = text + strip_headers(load_etext(book)).strip()
    print(f"\tBook loaded. Total source text length is now {len(text)}")
#top_words(text, 10)

print("Done.\n")

text_model = markovify.Text(text, state_size=3)
  

#for i in range(2):
#    print(text_model.make_sentence())

#print('-'*80)    

for i in range(10):

    tweet = text_model.make_short_sentence(140, max_overlap_ratio=0.70)
    if tweet is not None:
        print('-'*80)  
        print(tweet)

print('-'*80)     