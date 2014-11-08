'''
Created on Nov 4, 2014

@author: engin
'''
# coding=utf-8-sig

from fileUtil import *
from pandas.core.frame import DataFrame
import pandas as pd
from turkeyPopulationData import *

if __name__ == "__main__":
    fs = find_file_names('years', '*.xlsx')
    data = get_names_data(fs, 'xlsx')
    yKeys = data.keys()
    #tm = getTurkeyPopulationsByYears(data, yKeys)
    #tm = getTurkeyPopulationsByYearsInMale(data, yKeys)
    #tm = getTurkeyPopulationsByYearsInFemale(data, yKeys)
    city='All'
    tm = getCityCenterPopulationsByYears(data, yKeys, city)
    #tm = getCityPopulationsByYearsInMale(data, ['Konya', 'Ankara'], yKeys)
    #tm = getCityPopulationsByYearsInFemale(data, ['Konya', 'Ankara'], yKeys)
    #tm = getVillagePopulationsByYears(data, ['Konya', 'Ankara'], yKeys)
    #tm = getVillagePopulationsByYearsInMale(data, ['Konya', 'Ankara'], yKeys)
    #tm = getVillagePopulationsByYearsInFemale(data, ['Konya', 'Ankara'], yKeys)
    print tm
    
    
    
#     df = data['1965']
#     print df
#     c = df['Cities']
#     print c
#     
#     s = 'Türkiye'.decode('utf-8')
#     print type(s)
#     
#     t = df[c == s]['City_Total'].head()
#     print t