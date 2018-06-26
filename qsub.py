# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 12:41:37 2018

@author: iaaraya
"""

from itertools import product
import subprocess
import sys


model = sys.argv[1]

experiment = int(sys.argv[2])

#model = "hierarchical_LSTM"
#experiment = 2

if model == "simple_LSTM":
    
    if experiment == 1:
        
        layers = ['[5]', '[10]', '[15]', '[20]','[30]']
        
        lag = [1, 12, 24, 36]
        
        time_steps = [1, 5, 10, 15, 20]
        
        epochs = [1, 5, 10]
        
        l2 = [0.001]
        
        learning_rate = [0.05]
        
        batch_size = [1]
        
        verbose = [0]
        
        
    if experiment == 2:
        
        layers = ['[5]']
        
        lag = [3,4]
        
        time_steps = [5]
        
        epochs = [1]
        
        l2 = [0.001]
        
        learning_rate = [0.05]
        
        batch_size = [1]
        
        verbose = [0]
        
    combs = product(layers, lag, time_steps, epochs, l2, learning_rate, batch_size, verbose)
    
    counter = 0
    max_experiments = 5
    
    for c in combs:
    
        if counter == 0:
            
            string = ''
            
        if c:
            
            counter += 1
            
            for element in c:
                
                string += str(element) + ','
            
            if counter < max_experiments:
                    
                    string += '--'
                
            else:
                string = 'simple_LSTM /user/i/iaraya/Wind_speed/ \
                    no_mvs_b08.csv ' + string
            
                #print(string)
            
                subprocess.call(["qsub","main.sh","-F",string])
                
                counter = 0

    if counter > 0:
                    
        string = 'simple_LSTM /user/i/iaraya/Wind_speed/ \
        no_mvs_b08.csv ' + string

        #print(string)

        subprocess.call(["qsub","main.sh","-F",string])
            
    
elif model == "hierarchical_LSTM":
    
      
    if experiment == 1:
                
        lags = ["[1-24]"]
        
        time_steps = ["[24-5]","[24-10]","[24-15]","[24-20]"]
        
        dense_nodes = ["[1-5]","[1-10]"]
        
        lstm_nodes = ["[10-10]","[20-20]","[30-30]"]
        
        #lstm_nodes = ["[10-10]"]
        
        processed_scales = ["[0-1]"]
        
        epochs = [1]
        
        l2 = [0.001]
        
        batch_size = [1]
        
        shuffle = [0]
        
        verbose = [1]
        
    if experiment == 2:
                
        lags = ["[1-24]"]
        
        time_steps = ["[24-5]","[24-10]","[24-15]","[24-20]"]
        
        dense_nodes = ["[1-5]","[1-10]"]
        
        #lstm_nodes = ["[20-20]","[30-30]"]
        
        lstm_nodes = ["[10-10]","[20-20]","[30-30]"]
        
        processed_scales = ["[1]"]
        
        epochs = [1]
        
        l2 = [0.001]
        
        batch_size = [1]
        
        shuffle = [0]
        
        verbose = [1]
        
    if experiment == 3:
        
        lags = ["[1-24-48]"]
        
        time_steps = ["[24-5-5]","[24-10-5]","[24-15-5]","[24-20-5]", \
                      "[24-20-10]","[24-20-15]","[24-20-20]"]
        
        #dense_nodes = ["[1-10-10]","[1-20-20]"]
        
        dense_nodes = ["[1-5-5]"]
        
        lstm_nodes = ["[10-10-10]","[20-20-20]","[30-30-30]"]
        
        processed_scales = ["[0-1-2]"]
        
        epochs = [2,3]
        
        l2 = [0.001]
        
        batch_size = [1]
        
        shuffle = [0]
        
        verbose = [1]
        
    if experiment == 4:
                
        lags = ["[1-24-48]"]
        
        time_steps = ["[24-5-5]","[24-10-5]","[24-15-5]","[24-20-5]", \
                      "[24-20-10]","[24-20-15]","[24-20-20]"]
        
        #dense_nodes = ["[1-10-10]","[1-20-20]"]
        
        dense_nodes = ["[1-5-5]"]
        
        lstm_nodes = ["[10-10-10]","[20-20-20]","[30-30-30]"]
        
        processed_scales = ["[1-2]"]
        
        epochs = [2,3]
        
        l2 = [0.001]
        
        batch_size = [1]
        
        shuffle = [0]
        
        verbose = [1]
        
    if experiment == 5:
                
        lags = ["[1-24-48]"]
        
        time_steps = ["[24-5-5]",\
                      "[24-20-10]","[24-20-15]","[24-20-20]"]
        
        #dense_nodes = ["[1-10-10]","[1-20-20]"]
        
        dense_nodes = ["[1-5-5]"]
        
        lstm_nodes = ["[10-10-10]","[20-20-20]","[30-30-30]"]
        
        processed_scales = ["[2]"]
        
        epochs = [2,3]
        
        l2 = [0.001]
        
        batch_size = [1]
        
        shuffle = [0]
        
    verbose = [0]
    
    epochs = [1,2,3]
        
    
    combs = product(lags, time_steps, dense_nodes, lstm_nodes, processed_scales,\
                    epochs, l2, batch_size, shuffle, verbose)
    
    counter = 0
    max_experiments = 5
    
    for c in combs:
    
        if counter == 0:
            
            string = ''
            
        if c:
            
            counter += 1
            
            for element in c:
                
                string += str(element) + ','
            
            if counter < max_experiments:
                    
                    string += '--'
                
            else:
                string = 'hierarchical_LSTM /user/i/iaraya/Wind_speed/ \
                    no_mvs_villa_tehuelches.csv ' + string
            
                #print(string)
            
                subprocess.call(["qsub","main.sh","-F",string])
                
                counter = 0

    if counter > 0:
                    
        string = 'hierarchical_LSTM /user/i/iaraya/Wind_speed/ \
        no_mvs_b08.csv ' + string

        #print(string)

        subprocess.call(["qsub","main.sh","-F",string])
                


