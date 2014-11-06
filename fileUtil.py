'''
Created on Nov 4, 2014

@author: engin
'''

import glob, os
import pandas as pd

def get_names_data():
    frame_array = []
    files = glob.glob(os.path.join('years','*.xlsx'))
    for file in files:
        xl = pd.ExcelFile(file)
        sheetNames = xl.sheet_names
        for sheetname in sheetNames:
            data = pd.read_excel(file, sheetname)
            print data.head(15)
    
    names = pd.concat(frame_array, ignore_index=True)
    return names

get_names_data()