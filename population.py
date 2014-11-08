'''
Created on Nov 4, 2014

@author: engin
'''
# coding=utf-8

from fileUtil import *
from pandas.core.frame import DataFrame
import pandas as pd
from turkeyPopulationData import *
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    fs = find_file_names('years', '*.xlsx')
    data = get_names_data(fs, 'xlsx')
    yKeys = data.keys()
#     tm = getTurkeyPopulationsByYears(data, yKeys)
#     tm = getTurkeyPopulationsByYearsInMale(data, yKeys)
#     tm = getTurkeyPopulationsByYearsInFemale(data, yKeys)
#     tm = getCityCenterPopulationsByYears(data, ['Kilis','Yalova','Konya', 'Ankara','Ağrı'], yKeys)
#     print tm
#     tm = getCityPopulationsByYearsInMale(data, ['Kilis','Yalova','Konya', 'Ankara','Ağrı'], yKeys)
#     print tm
#     tm = getCityPopulationsByYearsInFemale(data, ['Kilis','Yalova','Konya', 'Ankara','Ağrı'], yKeys)
#     print tm
#     tm = getVillagePopulationsByYears(data, ['Kilis','Yalova','Konya', 'Ankara','Ağrı'], yKeys)
#     print tm
#     tm = getVillagePopulationsByYearsInMale(data, ['Kilis','Yalova','Konya', 'Ankara','Ağrı'], yKeys)
#     print tm
    tm = getVillagePopulationsByYearsInFemale(data, ['All'], yKeys).fillna(0).sort(yKeys, ascending=False).head(5).T
    print tm
    tm.plot()
#     print tm

#     rng = pd.date_range('1/1/2012', periods=24, freq='M')
#     ts = pd.Series(np.random.randn(len(rng)), rng).plot()
    plt.show()



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