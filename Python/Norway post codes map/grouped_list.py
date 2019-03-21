# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 17:51:36 2019

@author: Nastia aka Anastasija Litvinionok nlitvinionok@gmail.com
"""

import geopandas as gpd
import numpy as np
import special_dataset as sd

def get_list_of_codes():
    
    norway_set = gpd.read_file('Basisdata_0000_Norge_25833_Postnummeromrader_SOSI_Postnummerområde_FLATE.shp')
    norway_set = norway_set[['POSTNUMMER', 'geometry']]
      
    for item in norway_set[['POSTNUMMER']][:-1]:
        uniquelist = norway_set[item].unique()
        print('Unique rows:')
        print(uniquelist)
        
    #print(type(uniquelist)) # In case we need to know the type
        
    # All unique post codes are here !
    print('Unique post codes:')
    uniquelist = np.sort(uniquelist, kind='quicksort')
    print(uniquelist.tolist())

    uniq_grouped = norway_set.groupby('POSTNUMMER').first()
    #print(type(uniq_grouped)) # In case we need to know the type
    print(uniq_grouped)
    print('Unique grouped:')
    num_array = uniq_grouped.index.to_numpy(copy=True)
    print(num_array.tolist())
    print('Size of array: ' + str(uniq_grouped.size))
    print('Shape of array: ' + str(uniq_grouped.shape))
    
    sd.make_df(num_array)

get_list_of_codes()