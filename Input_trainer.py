# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 10:22:11 2018

@author: Sreeje.a
"""

import re
import os , sys
import pandas as pd
import operator

def input_prep(ip_path):
    
    extension = os.path.splitext(ip_path)[1]
    
    if extension==".txt":
        tokens=[]
        with open(INPUT_PATH) as f:      
          for line in f:
            if not line.isspace():
                line=line.lower()
                line_new = re.sub('[^a-zA-Z0-9\n\.]', ' ', line)
                line_new = line_new.replace(',', '').replace('.','')
            items=line_new.split()
            tokens+=items   
            
    elif extension==".csv":
        data=pd.read_csv(INPUT_PATH)
        column_names=data.columns.tolist()
        tok=[]
        for i in column_names:
            col=data[i].tolist()
            for line in col:
                if str(line)!="nan":     
                    line=line.lower()
                    line_new = re.sub('[^a-zA-Z0-9\n\.]', ' ', line)              
                    line_new = line_new.replace(',', '').replace('.','')
                    tok.append(line_new.split())
                
        tokens=reduce(operator.concat,tok)        

    return tokens
            
        
                     
            
            
            
            
            
            
            
