# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 12:41:37 2018

@author: iaaraya
"""

from itertools import product
import subprocess
import sys


#model = sys.argv[1]
model = "simple_LSTM"

if model == "simple_LSTM":
    
    layers = ['[5]', '[10]', '[15]', '[20]']
    
    lag = [12, 34, 36]
    
    time_steps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,\
                  18, 19, 20]
    
    epochs = [1, 5]
    
    combs = product(layers, lag, time_steps, epochs)
    
    for c in combs:
        
        if c:
            
            string = ''
            
            for element in c:
                
                string += str(element) + ','
            
            string = 'simple_LSTM.py /user/i/iaraya/CIARP/Wind_speed/data/ \
                    no_mvs_d05a.csv ' + string
            #print(string)
            subprocess.call(["qsub","main.sh","-F",string])
            
    
    




