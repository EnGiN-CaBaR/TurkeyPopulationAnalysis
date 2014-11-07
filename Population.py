'''
Created on Nov 4, 2014

@author: engin
'''
# coding=utf-8-sig

from fileUtil import *
from pandas.core.frame import DataFrame
import pandas as pd


if __name__ == "__main__":
    fs = find_file_names('years', '*.xlsx')
    data = get_names_data(fs, 'xlsx')
    
    yKeys = data.keys()
    
    
    
    df = data['1965']
    print df
    c = df['Cities']
    print c
    
    s = 'Türkiye'.decode('utf-8')
    print type(s)
    
    t = df[c == s]['City_Total'].head()
    print t