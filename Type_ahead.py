# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 12:06:44 2017

@author: Sreeje.a
"""
from nltk.util import ngrams
from collections import OrderedDict
import cPickle as pickle 
import re
import sys
import Config as cfg



with open(cfg.MODEL_PATH+"prob_table_uni.dat", 'rb') as handle:
        prob_table_uni = pickle.load(handle)
with open(cfg.MODEL_PATH+"prob_table_bi.dat", 'rb') as handle:
        prob_table_bi = pickle.load(handle) 
with open(cfg.MODEL_PATH+"bigram_table.dat", 'rb') as handle:
        bigram_table = pickle.load(handle)        
        
bigram_table=bigram_table.most_common()        
  

def predict(query):  
    
    query = re.sub('[^a-zA-Z0-9\n\.]', ' ', query)
    query_split=query.split()
    
    if len(query_split)==1:        
        key=query.lower()       
        predicted_words=prob_table_uni[key]            
    else:
        query_bigrams=list(ngrams(query_split, 2)) 
        n=len(query_bigrams)
        req_bigram=query_bigrams[n-1]
        predicted_words= prob_table_bi[req_bigram] 
        key=req_bigram[1]
        
    possible_pairs=[]
    for i in predicted_words:
        possible_pairs.append((key,i))
    priority=[]
    for j in bigram_table:
        if j[0] in possible_pairs:
            priority.append(j)
    priority=dict(priority)        
    
    d_sorted_by_value = OrderedDict(sorted(priority.items(), key=lambda x: x[1], reverse=True))

    first10pairs = {k: d_sorted_by_value[k] for k in d_sorted_by_value.keys()[:15]}
    possible_outcomes=[]
    for k,v in first10pairs.items():
        possible_outcomes.append((query+" "+k[1]))
       
    return  possible_outcomes     


if __name__ == '__main__':
    predict("would agree our")











