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
       populationAvg = turkey_population_in_years[year] / city_count[year]
       populationAvgPerCity[year] = populationAvg
    pd.DataFrame(populationAvgPerCity).T.plot()
    plt.show()
    
def plotTotalMaleFemaleAvgPerYear(data, years):
    tp = getTurkeyPopulationsByYears(data, years)
    tpf = getTurkeyPopulationsByYearsInFemale(data, years)
    tpm = getTurkeyPopulationsByYearsInMale(data, years)
    tpf = (tpf.div(tp.ix[0], axis='columns') * 100)
    tpm = (tpm.div(tp.ix[0], axis='columns') * 100)
    tpg = tpf.append(tpm)
    tpg.index = ['FemaleAvg', 'MaleAvg']
    tpg.T.plot()
    plt.show()

def plotTurkeyPopulationByYear(data, years):
    tpf = getTurkeyPopulationsByYearsInFemale(data, years).ix['Türkiye']
    tpm = getTurkeyPopulationsByYearsInMale(data, years).ix['Türkiye']
    ind = np.arange(len(years))
    width = 0.35
    
    p1 = plt.bar(ind, tpf, width, color='r')
    p2 = plt.bar(ind, tpm, width, color='y', bottom=tpm)
    plt.ylabel('TotalPop')
    plt.title('Population Increase')
    plt.xticks(ind + width / 2., sorted(years))
    plt.yticks(np.arange(0, 7e7, 1e7))
    plt.legend((p1[0], p2[0]), ('Femen', 'Male'))  # sagüste legend cıkarıyor anlamak için

    plt.show()
    
def plotTopFiveCityPopulationGrowth(data, years):
    sorted_data = data.fillna(0).sort(years, ascending=False).head(5)
    turkey_total = sorted_data.sum()
    sorted_data = (sorted_data / turkey_total) * 100
    sorted_data_columns = list(sorted_data.columns.values)
    sorted_data_rows = list(sorted_data.index.values)
    
    
    dot_chart = pygal.Dot(x_label_rotation=50)
    dot_chart.title = 'Population Percentage of Top-5 cities per Year'
    dot_chart.x_labels = sorted_data_columns
    for city in sorted_data_rows:
        dot_chart.add(city, sorted_data.ix[city])
    dot_chart.render_to_file('dot_chart.svg')

def stackedExample(data, years):
    print data
    
    
    
    stackedline_chart = pygal.StackedLine(fill=True)
    stackedline_chart.title = 'Browser usage evolution (in %)'
    stackedline_chart.x_labels = map(str, range(2002, 2013))
    stackedline_chart.add('Firefox', [None, None, 0, 16.6, 25, 31, 36.4, 45.5, 46.3, 42.8, 37.1])
    stackedline_chart.add('Chrome', [None, None, None, None, None, None, 0, 3.9, 10.8, 23.8, 35.3])
    stackedline_chart.add('IE', [85.8, 84.6, 84.7, 74.5, 66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    stackedline_chart.add('Others', [14.2, 15.4, 15.3, 8.9, 9, 10.4, 8.9, 5.8, 6.7, 6.8, 7.5])
    stackedline_chart.render_to_file('stacked_chart.svg')
