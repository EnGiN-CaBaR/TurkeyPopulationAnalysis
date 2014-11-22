'''
Created on Nov 4, 2014

@author: engin
'''
# coding=utf-8


import glob, os
import pandas as pd

def get_names_data(fileNames, file_type):
    """
    This function read file list and file type. After identifying file type
    function makes process according to type and return a dictionary has keys(years)
    and values(DataFrames belongs to this year). If it is csv, reading file with 
    csv function, for example.
    fileNames parameter takes a list which has file names in a specific 
    folder.
    file_type parameter takes file type to identify file. 
    """
    populationYears = {}
    for fileName in fileNames:
        fName = fileName[6:10]
        print fName, " is now reading"
        if file_type == 'csv':
            data = pd.read_csv(fileName, error_bad_lines=False, delimiter=';')
        elif file_type == 'xlsx':
            try:
                fileX = pd.ExcelFile(fileName)
            except Exception:
                print fileName, " cannot be find."
            sheetNames = fileX.sheet_names
            for sheet in sheetNames:
                try:
                    data = pd.read_excel(fileName, sheet, parse_cols="A:L", header=10)
                except:
                    print fileName, " cannot be find."
                data.columns = ['Cities', 'City_Total', 'City_Male', 'City_Female', 'CityCenter_Total',
                                'CityCenter_Male', 'CityCenter_Female', 'Villages_Total', 'Villages_Male', 'Villages_Female']
            data = data.dropna()
        populationYears[fName] = data
    return populationYears

def find_file_names(path, fileName_extension):
    """
    This function returns all file names as a list.
    path parameter is files' path.
    fileName_extension is file type
    """
    files = glob.glob(os.path.join(path, fileName_extension))
    return files

def getPlate():
    "This function read all cities plate code from plaka.txt file."
    plate = {}
    with open('static/plaka.txt', 'r') as f:
        for line in f.readlines():
            l = line.split(":")
            plate[l[1].rstrip().decode('utf-8')] = l[0]
    return plate

def getRegionFiles(regionFiles):
    """
        This function returns a dictionary which has region keys and city list value
    """
    regions = {}
    for region in regionFiles:
        regionName = region[12:-4]
        with open(region, 'r') as f:
            regions[regionName] = f.readlines()[0].split(',')
    return regions

def getArea():
    """
    This function returns a dictionary which has cityname keys and vales(city area list) 
    """
    area = {}
    with open('static/cityAreas.txt', 'r') as f:
        for line in f.readlines():
            l = line.split(":")
            area[l[0].rstrip().decode('utf-8')] = l[1]
    return area