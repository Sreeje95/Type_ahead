# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 14:43:28 2017

@author: Sreeje.a
"""
from nltk.util import ngrams
from collections import Counter
from collections import defaultdict
import  sys
import Config as cfg
import Input_trainer as it 
import cPickle as pickle 


def train(unigram=True,bigram=True):
    
        
    tokens=it.input_prep(cfg.INPUT_PATH)
       
    bigrams=list(ngrams(tokens,2))
    unigrams=list(ngrams(tokens,1))
    bigram_table=Counter(bigrams)
    unigram_table=Counter(unigrams)
    trigrams=list(ngrams(tokens,3))
    trigram_table=Counter(trigrams)
    
    
    with open(cfg.MODEL_PATH+"bigram_table.dat", 'wb') as handle:
        pickle.dump(bigram_table, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
    prob_table_uni = defaultdict(dict)
    bigram_table_list=bigram_table.most_common()

    prob_table_uni={}
    for i in bigram_table_list:
        key=i[0][0]
        prob_table_uni.setdefault(key, [])
        token=i[0][1]
        prob_table_uni[key].append(token)
          
    with open(cfg.MODEL_PATH+"prob_table_uni.dat", 'wb') as handle:
        pickle.dump(prob_table_uni, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
    trigram_table_list=trigram_table.most_common()

    prob_table_bi={}
    for i in trigram_table_list:
        key=(i[0][0],i[0][1])
        prob_table_bi.setdefault(key, [])
        token=i[0][2]
        prob_table_bi[key].append(token) 
   
        
    with open(cfg.MODEL_PATH+"prob_table_bi.dat", 'wb') as handle:
        pickle.dump(prob_table_bi, handle, protocol=pickle.HIGHEST_PROTOCOL)     

if __name__ == '__main__':
    
  train(unigram=True,bigram=True)  
