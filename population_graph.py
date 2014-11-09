import pandas as pd
import matplotlib.pyplot as plt
from turkeyPopulationData import *
import numpy as np

# coding=utf-8

def plotTotalPopulation_Cities(turkey_population_in_years, city_count):
    yKeys = city_count.keys()
    populationAvgPerCity = {}
    for year in yKeys:
       populationAvg = turkey_population_in_years[year]/city_count[year]
       populationAvgPerCity[year] = populationAvg
    pd.DataFrame(populationAvgPerCity).T.plot()
    plt.show()
    
def plotTotalMaleFemaleAvgPerYear(data, years):
    tp = getTurkeyPopulationsByYears(data, years)
    tpf = getTurkeyPopulationsByYearsInFemale(data, years)
    tpm = getTurkeyPopulationsByYearsInMale(data, years)
    tpf = (tpf.div(tp.ix[0],axis='columns') * 100)
    tpm = (tpm.div(tp.ix[0],axis='columns') * 100)
    tpg = tpf.append(tpm)
    tpg.index = ['FemaleAvg', 'MaleAvg']
    tpg.T.plot()
    plt.show()

def plotTurkeyPopulationByYear(data, years):
    tpf = getTurkeyPopulationsByYearsInFemale(data, years).ix['Türkiye']
    tpm = getTurkeyPopulationsByYearsInMale(data, years).ix['Türkiye']
    ind = np.arange(len(years))
    width = 0.35
    
    p1 = plt.bar(ind, tpf,   width, color='r')
    p2 = plt.bar(ind, tpm, width, color='y', bottom=tpm)
    plt.ylabel('TotalPop')
    plt.title('Population Increase')
    plt.xticks(ind+width/2., sorted(years))
    plt.yticks(np.arange(0,7e7,1e7))
    plt.legend( (p1[0], p2[0]), ('Femen', 'Male') ) #sagüste legend cıkarıyor anlamak için

    plt.show()
