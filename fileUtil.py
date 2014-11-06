'''
Created on Nov 4, 2014

@author: engin
'''
# -*- coding: utf-8 -*-
import glob, os
import pandas as pd

def get_names_data(fileName, file_type):
    fName = fileName[6:10]
    print fName, " is now reading"
    if file_type == 'csv':
        with open(fileName, 'r') as f:
            data = pd.read_csv(f, error_bad_lines=False, delimiter=';')
    elif file_type == 'xlsx' or 'xls':
        fileX = pd.ExcelFile(fileName)
        sheetNames = fileX.sheet_names
        for sheet in sheetNames:
            data = pd.read_excel(fileName, sheet)
    return data.dropna()
        
def find_file_names(path, fileName_extension):
    files = glob.glob(os.path.join(path, fileName_extension))
    return files