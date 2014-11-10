import pandas as pd
import matplotlib.pyplot as plt
from turkeyPopulationData import *
import numpy as np
import pygal

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
    
def plotTopFiveCityPopulationGrowth(data, years):
    sorted_data = data.fillna(0).sort(years, ascending=False).head(10)
    sorted_data = (sorted_data / sorted_data[years].sum()) * 100
    sorted_data_columns = list(sorted_data.columns.values)
    sorted_data_rows = list(sorted_data.index.values)
    
    
    dot_chart = pygal.Dot(x_label_rotation=50)
    dot_chart.title = 'Population Percentage of Top-5 cities per Year'
    dot_chart.x_labels = sorted_data_columns
    for city in sorted_data_rows:
        dot_chart.add(city, sorted_data.ix[city])
    dot_chart.render_to_file('dot_chart.svg')   
