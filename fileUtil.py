'''
Created on Nov 4, 2014

@author: engin
'''
# coding=utf-8


import glob, os
import pandas as pd

def get_names_data(fileNames, file_type):
    populationYears = {}
    for fileName in fileNames:
        fName = fileName[6:10]
        print fName, " is now reading"
        if file_type == 'csv':
            data = pd.read_csv(fileName, error_bad_lines=False, delimiter=';')
        elif file_type == 'xlsx':
            fileX = pd.ExcelFile(fileName)
            sheetNames = fileX.sheet_names
            for sheet in sheetNames:
                data = pd.read_excel(fileName, sheet, parse_cols="A:L", header=10)
                data.columns = ['Cities', 'City_Total', 'City_Male', 'City_Female', 'CityCenter_Total', 
                                'CityCenter_Male', 'CityCenter_Female', 'Villages_Total', 'Villages_Male', 'Villages_Female']
            data = data.dropna()
        populationYears[fName] = data
    return populationYears

def find_file_names(path, fileName_extension):
    files = glob.glob(os.path.join(path, fileName_extension))
    return files