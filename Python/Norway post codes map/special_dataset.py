# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 16:12:55 2019

@author: Nastia aka Anastasija Litvinionok nlitvinionok@gmail.com
"""

import pandas as pd
import numpy as np

    #print(type(uniq_grouped)) # In case we need to know the type
    
def make_df(num_array):
    
    row_set = np.empty((0, 100))
    col_set = list(range(0,10000,100))
    new_data_set = np.ndarray(shape=(0, 100), dtype=str)
    print(col_set)
    print(len(col_set))
    
    new_data_frame = pd.DataFrame(data=new_data_set, columns=col_set)
    
    print('Data frame:')
    print(new_data_frame.head())

    for column in new_data_frame :
        
            for line in num_array :
                if int(line) > column and int(line) < column + 100:
                    row_set = np.append(row_set, [line])
            #col_n = column
            #
            #print(col_n) # To check the column   
            #print(row_set.tolist()) # To check the row
            
            if row_set != np.empty((0, 100)) :
                new_data_frame[column] = pd.Series(row_set)
            row_set = np.empty((0, 100))
                
    print('Data frame updated:')
    print(new_data_frame.head())
    print(new_data_frame.describe())
    new_data_frame.to_excel('special.dataset.xlsx')
    
    