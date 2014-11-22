import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from turkeyPopulationData import *
try:
    import pygal as pg
except:
    print "Ypu should first install pg"



# coding=utf-8
def plotTotalPopulation_Cities(turkey_population_in_years, city_count):
    """This function plot total population average vs years. 
    turkey_population_in_years parameter is turkey population values.
    city_count is city number in years  
    """
    yKeys = city_count.keys()
    populationAvgPerCity = {}
    for year in yKeys:
        populationAvg = turkey_population_in_years[year] / city_count[year]
        populationAvgPerCity[year] = populationAvg
    pd.DataFrame(populationAvgPerCity).T.plot()
    plt.show()
    
def plotTotalMaleFemaleAvgPerYear(data, years):
    """
    This function plot male-female avg vs years.
    data is our dictionary. years is our year
    list.
    """
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
    """
    This function plots Top Five City Population rate by years and save it as a svg 
    file using pg. 
    Data is our data frame object which has city data. In function this data is 
    sorted according to 1965.
    years is a list contains years data.
    """
    sorted_data = data.fillna(0).sort(years, ascending=False).head(5)
    turkey_total = sorted_data.sum()
    sorted_data = (sorted_data / turkey_total) * 100
    sorted_data_columns = list(sorted_data.columns.values)
    sorted_data_rows = list(sorted_data.index.values)

    dot_chart = pg.Dot(x_label_rotation=50)
    dot_chart.title = 'Population Percentage of Top-5 cities per Year'
    dot_chart.x_labels = sorted_data_columns
    for city in sorted_data_rows:
        dot_chart.add(city, sorted_data.ix[city])
    dot_chart.render_to_file('graphs\\topfivecitypopulationgrowth.svg')
    
def plotHorizontalBarTopFive(data, years):
    """
    This function plot Top Five City Center Population and save it as a svg file using pg.
    Data is our data frame object which has city data. In function this data is sorted
    according to 1965.
    years is a list contains years data.
    """
    data_1965 = data.fillna(0).sort(['1965'],ascending=False).head(5)['1965']
    city = data_1965.index
    pop = data_1965.values
    horizontalbar_chart = pg.HorizontalBar()
    horizontalbar_chart.title = 'Top 5 city center in 1965'
    for i in range(len(city)):
        horizontalbar_chart.add(city[i], pop[i])

    horizontalbar_chart.render_to_file("graphs\\horizontalbartopfive.svg")
    

def plotLineChartTopTen(data, years):
    """
    This function plot line graph Top ten City Center Population and save 
    it as a svg file using pg.
    Data is our data frame object which has city data. In function this data is sorted
    according to 1965.
    years is a list contains years data.
    """
    sorted_data = data.fillna(0).sort(years,ascending=False).head(10)
    city = sorted_data.index
    pop = sorted_data.values
    line_chart = pg.Line()
    line_chart.title = 'Top 10 Cities Population Increased Most'
    line_chart.x_labels = map(str, years)
    for i in range(len(city)):
        line_chart.add(city[i], pop[i])
    line_chart.render_to_file("graphs\\linecharttoptencity.svg")
    
def plotLineChartTopTenRural(data, years):
    """
    This function plot line graph Top ten rural area Population and save 
    it as a svg file using pg.
    Data is our data frame object which has city data. In function this data is sorted
    according to 1965.
    years is a list contains years data.
    """
    sorted_data = data.fillna(0).sort(years,ascending=False).head(10)
    city = sorted_data.index
    pop = sorted_data.values
    line_chart = pg.Line()
    line_chart.title = 'Top 10 Village Population Increased Most'
    line_chart.x_labels = map(str, years)
    for i in range(len(city)):
        line_chart.add(city[i], pop[i])
    line_chart.render_to_file("graphs\\linecharttoptenrural.svg")


def plotPyramidChart(cPopMale, cPopFemale, yKeys, cityRegion):
    """
    This function plot pyramid chart belongs cities' male and female number by year 
    for every geographic region which has and save it as a svg file using pg.
    cPopMale is our data frame object which has city male data. 
    cPopFeMale is our data frame object which has city female data.
    cityRegion is our dictionary object which has region keys and cities' value as a list.
    years is a list contains years data.
    """
    cPopMale = cPopMale.fillna(0)
    cPopFemale = cPopFemale.fillna(0)
    regions = cityRegion.keys()
    sortedYears = sorted(yKeys)
    for region in regions:
        cityInRegion = cityRegion[region]
        cityPopSet = []
        cityNameInGender = []
        pyramid_chart = pg.Pyramid(human_readable=True, legend_at_bottom=True)
        pyramid_chart.title = 'Male-Female Population Changing In ' + region + ' By Year'
        pyramid_chart.x_labels = sortedYears
        for city in cityInRegion:
            cityNameInGender.append(city + " Male")
            cityNameInGender.append(city + " Female")
        for city in cityInRegion:
            cityPopMale = ()
            cityPopFemale = ()
            for year in sortedYears:
                pop_Male = cPopMale[year][city.decode('utf-8')]
                cityPopMale = cityPopMale + (pop_Male,)
                pop_Female = cPopFemale[year][city.decode('utf-8')]
                cityPopFemale = cityPopFemale + (pop_Female,)
            cityPopSet.append(cityPopMale)
            cityPopSet.append(cityPopFemale)
        for nameInGender, popSet in zip(cityNameInGender, cityPopSet):
            pyramid_chart.add(nameInGender.decode('utf-8'), popSet)
        pyramid_chart.render_to_file("graphs\\" + region + ".svg")
        
def plotRegionOverTotalPopulationInYears(cPopMale, cPopFemale, yKeys, cityRegion):
    """
    This function plot pyramid chart belongs geographic regions male and female number by year 
    which has and save it as a svg file using pg.
    cPopMale is our data frame object which has city male data. 
    cPopFeMale is our data frame object which has city female data.
    cityRegion is our dictionary object which has region keys and cities' value as a list.
    years is a list contains years data.
    """
    cPopMale = cPopMale.fillna(0)
    cPopFemale = cPopFemale.fillna(0)
    regions = cityRegion.keys()
    sortedYears = sorted(yKeys)
    regionNameInGender = []
    regionPopSet = []
    pyramid_chart = pg.Pyramid(human_readable=True, legend_at_bottom=True)
    pyramid_chart.title = 'Male-Female Population Changing In Region By Year'
    pyramid_chart.x_labels = sortedYears
    regions.sort()
    for region in regions:
        regionNameInGender.append(region + " Male")
        regionNameInGender.append(region + " Female")
    for year in sortedYears:
        regionPopMale = ()
        regionPopFemale = ()
        for region in regions:
            cityInRegion = cityRegion[region]
            cityPopMale = 0
            cityPopFemale = 0
            for city in cityInRegion:
                pop_Male = cPopMale[year][city.decode('utf-8')]
                cityPopMale = cityPopMale + pop_Male
                pop_Female = cPopFemale[year][city.decode('utf-8')]
                cityPopFemale = cityPopFemale + pop_Female
            regionPopMale = regionPopMale + (cityPopMale,)
            regionPopFemale = regionPopFemale + (cityPopFemale,)
        regionPopSet.append(regionPopMale)
        regionPopSet.append(regionPopFemale)
    for nameInGender, popSet in zip(regionNameInGender, regionPopSet):
        pyramid_chart.add(nameInGender.decode('utf-8'), popSet)
    pyramid_chart.render_to_file("graphs\\RegionPopulationPyramidGraph" + ".svg")

# GR 1 Urban Population Percentage of Top-5 cities
def plotTopFiveCityUrbanPopulationPercentage(data, years):
    sorted_data = data.fillna(0).sort(years, ascending=False).head(5)
    sorted_data_columns = list(sorted_data.columns.values)
    sorted_data_rows = list(sorted_data.index.values)
        
    dot_chart = pg.Line()
    dot_chart.title = 'Top-5 Urban Population Percentage'
    dot_chart.x_labels = sorted_data_columns
    for city in sorted_data_rows:
        dot_chart.add(city, sorted_data.ix[city])
    dot_chart.render_to_file('GR1_Top5CityUrbanPopulationPercentage.svg')   
    
# GR 2 Village Population Percentage of Top-5 cities
def plotTopFiveCityVillagePopulationPercentage(data, years):
    sorted_data = data.fillna(0).sort(years, ascending=False).head(5)
    sorted_data_columns = list(sorted_data.columns.values)
    sorted_data_rows = list(sorted_data.index.values)
        
    dot_chart = pg.Line()
    dot_chart.title = 'Top-5 Rural Population Percentage'
    dot_chart.x_labels = sorted_data_columns
    for city in sorted_data_rows:
        dot_chart.add(city, sorted_data.ix[city])
    dot_chart.render_to_file('GR2_Top5CityVillagePopulationPercentage.svg')   

# GR 3 Urbanization Percentage of Top-5 Urbanized cities: City /(City + Urban)
def plotTopFiveUrbanizedCityUrbanizationPercentage(data, years):
    sorted_data = data.fillna(0).sort(years, ascending=False).head(5)
    sorted_data_columns = list(sorted_data.columns.values)
    sorted_data_rows = list(sorted_data.index.values)
        
    dot_chart = pg.Line()
    dot_chart.title = 'Urbanization Percentage of Top-5 Urbanized Cities'
    dot_chart.x_labels = sorted_data_columns
    for city in sorted_data_rows:
        dot_chart.add(city, sorted_data.ix[city])
    dot_chart.render_to_file('GR3_TopFiveUrbanizedCityUrbanizationPercentage.svg')   

# GR 4 Urbanization Percentage of Least-5 Urbanized cities: City /(City + Urban)
def plotLeastFiveUrbanizedCityUrbanizationPercentage(data, years):
    sorted_data = data.sort(years, ascending=True).head(5)
    sorted_data_columns = list(sorted_data.columns.values)
    sorted_data_rows = list(sorted_data.index.values)
        
    dot_chart = pg.Line()
    dot_chart.title = 'Urbanization Percentage of Least-5(1965) Urbanized Cities'
    dot_chart.x_labels = sorted_data_columns
    for city in sorted_data_rows:
        dot_chart.add(city, sorted_data.ix[city])
    dot_chart.render_to_file('GR4_1965LeastFiveUrbanizedCityUrbanizationPercentage.svg')   

# GR 5 Urbanization Percentage of Turkey: City / Turkey
def plotTurkeyUrbanizationPercentage(data, years):
    sorted_data = data.sort(years, ascending=True)
    sorted_data_columns = list(sorted_data.columns.values)
    sorted_data_rows = list(sorted_data.index.values)
        
    dot_chart = pg.Line()
    dot_chart.title = 'Urbanization Percentage of Turkey'
    dot_chart.x_labels = sorted_data_columns
    for city in sorted_data_rows:
        dot_chart.add(city, sorted_data.ix[city])
    dot_chart.render_to_file('GR5_TurkeyUrbanizationPercentage.svg')   

# GR 6 Urban Population Growth of Top-5 cities 
def plotTopTenCityPopulationGrowth(data, years):
    sorted_data = data.fillna(0).sort(years, ascending=False).head(10)
    sorted_data_columns = list(sorted_data.columns.values)
    sorted_data_rows = list(sorted_data.index.values)
        
    dot_chart = pg.Dot(x_label_rotation=50)
    dot_chart.title = 'Cities with Top-5 Urban Population'
    dot_chart.x_labels = sorted_data_columns
    for city in sorted_data_rows:
        dot_chart.add(city, sorted_data.ix[city])
    dot_chart.render_to_file('GR6_Top10UrbanPopulation.svg')   
    
# GR 7 Male - Female Ratio in Total Population
def plotDataMaleFemalePercentBAR(data, data1, data2, years):
    sorted_data = data
    sorted_data_percentage = (sorted_data / sorted_data[years].sum()) * 100
    sorted_data_columns = list(sorted_data.columns.values)
    sorted_data_rows = list(sorted_data.index.values)
    
    sorted_data_male = data1
    sorted_data_male_percentage = (sorted_data_male / sorted_data[years].sum()) * 100
    sorted_data_male_columns = list(sorted_data_male.columns.values)
    sorted_data_male_rows = list(sorted_data_male.index.values)

    sorted_data_female = data2
    sorted_data_female_percentage = (sorted_data_female / sorted_data[years].sum()) * 100
    sorted_data_female_columns = list(sorted_data_female.columns.values)
    sorted_data_female_rows = list(sorted_data_female.index.values)
 
   
    bar_chart = pg.Line()
    bar_chart.title = 'Male - Female Ratio in Turkey Population'
    bar_chart.x_labels = sorted_data_columns
    for city in sorted_data_rows:
        bar_chart.add("Male", sorted_data_male_percentage.ix[city])
        bar_chart.add("Female", sorted_data_female_percentage.ix[city])
    bar_chart.render_to_file('GR7_MaleFemaleRatioTotalPopulation.svg')   


# GR 8 Top-5 Village Population 
def plotTopFiveVillagePopulationGrowth(data, years):
    sorted_data = data.fillna(0).sort(years, ascending=False).head(5)
    sorted_data_columns = list(sorted_data.columns.values)
    sorted_data_rows = list(sorted_data.index.values)
        
    dot_chart = pg.Dot(x_label_rotation=50)
    dot_chart.title = 'Cities with Top-5 Rural Population'
    dot_chart.x_labels = sorted_data_columns
    for city in sorted_data_rows:
        dot_chart.add(city, sorted_data.ix[city])
    dot_chart.render_to_file('GR8_Top5VillagePopulation.svg')

# GR 9 Top-10 Urban Female Percentage (1965) 
def plotTop10UrbanFemalePercent(data, years):
    sorted_data = data.sort(years, ascending=False).head(10)
    sorted_data_columns = list(sorted_data.columns.values)
    sorted_data_rows = list(sorted_data.index.values)
        
    dot_chart = pg.Line()
    dot_chart.title = 'Top-10 Urban Female Percentage (1965)'
    dot_chart.x_labels = sorted_data_columns
    for city in sorted_data_rows:
        dot_chart.add(city, sorted_data.ix[city])
    dot_chart.render_to_file('GR9_Top10UrbanFemalePercentage.svg')   

# GR 10 Top-10 Village Female Percentage (1965) 
def plotTop10VillageFemalePercent(data, years):
    sorted_data = data.sort(years, ascending=False).head(10)
    sorted_data_columns = list(sorted_data.columns.values)
    sorted_data_rows = list(sorted_data.index.values)

    dot_chart = pg.Line()
    dot_chart.title = 'Top-10 Urban Male Percentage (1965)'
    dot_chart.x_labels = sorted_data_columns
    for city in sorted_data_rows:
        dot_chart.add(city, sorted_data.ix[city])
    dot_chart.render_to_file('GR11_Top10UrbanMalePercentage.svg')   

 
# GR 11 Top-10 Urban Male Percentage (1965) 
def plotTop10UrbanMalePercent(data, years):
    sorted_data = data.sort(years, ascending=False).head(10)
    sorted_data_columns = list(sorted_data.columns.values)
    sorted_data_rows = list(sorted_data.index.values)
        
    dot_chart = pg.Line()
    dot_chart.title = 'Top-10 Urban Male Percentage (1965)'
    dot_chart.x_labels = sorted_data_columns
    for city in sorted_data_rows:
        dot_chart.add(city, sorted_data.ix[city])
    dot_chart.render_to_file('GR11_Top10UrbanMalePercentage.svg')   

# GR 12 Top-10 Village Male Percentage (2000) 
def plotTop10VillageMalePercent(data, years):
    sorted_data = data.sort(years, ascending=False).head(10)
    sorted_data_columns = list(sorted_data.columns.values)
    sorted_data_rows = list(sorted_data.index.values)
       
    dot_chart = pg.Line()
    dot_chart.title = 'Top-10 Rural Male Percentage (1965)'
    dot_chart.x_labels = sorted_data_columns
    for city in sorted_data_rows:
        dot_chart.add(city, sorted_data.ix[city])
    dot_chart.render_to_file('GR12_Top10VillageMalePercentage.svg')   

# GR 13 Top-20 Urban Female Population Change Percentage
def plotTop20UrbanFemalePercentageChange(data):
    datah = data.head(20)
    sorted_data_rows = datah.keys()  
    print datah
    bar_chart = pg.HorizontalBar()
    bar_chart.title = 'Top-20 Cities by Percentage of Urban Female Population Change'
    for city in sorted_data_rows:
        bar_chart.add(city, datah.ix[city])
    bar_chart.render_to_file('GR13_Top20UrbanFemalePercentageChange.svg')   

# GR 14 Top-20 Village Female Population Change Percentage
def plotTop20VillageFemalePercentageChange(data):
    datah = data.head(20)
    sorted_data_rows = datah.keys()  
    print datah
    bar_chart = pg.HorizontalBar()
    bar_chart.title = 'Top-20 Cities by Percentage of Rural Female Population Change'
    for city in sorted_data_rows:
        bar_chart.add(city, datah.ix[city])
    bar_chart.render_to_file('GR14_Top20VillageFemalePercentageChange.svg')   
    

# GR 15 Top-20 Urban Male Population Change Percentage
def plotTop20UrbanMalePercentageChange(data):
    datah = data.head(20)
    sorted_data_rows = datah.keys()  
    print datah
    bar_chart = pg.HorizontalBar()
    bar_chart.title = 'Top-20 Cities by Percentage of Urban Male Population Change'
    for city in sorted_data_rows:
        bar_chart.add(city, datah.ix[city])
    bar_chart.render_to_file('GR15_Top20UrbanMalePercentageChange.svg')   

# GR 16 Top-20 Village Male Population Change Percentage
def plotTop20VillageMalePercentageChange(data):
    datah = data.head(20)
    sorted_data_rows = datah.keys()  
    print datah
    bar_chart = pg.HorizontalBar()
    bar_chart.title = 'Top-20 Cities by Percentage of Rural Male Population Change'
    for city in sorted_data_rows:
        bar_chart.add(city, datah.ix[city])
    bar_chart.render_to_file('GR16_Top20VillageMalePercentageChange.svg') 
    
# GR 17 Male Female Total Population Trend
def plotPopulationTrend(data, data1, data2, data3, data4, years):
    sorted_data = data
    sorted_data_columns = list(sorted_data.columns.values)
    sorted_data_rows = list(sorted_data.index.values)
       
    bar_chart = pg.StackedBar(fill=True)
    bar_chart.title = 'Male / Female Population Trend'
    bar_chart.x_labels = sorted_data_columns
    for city in sorted_data_rows:   
        #bar_chart.add("Total", sorted_data.ix[city])
        bar_chart.add("Male",  data1.ix[city])
        bar_chart.add("Female", data2.ix[city])
    bar_chart.render_to_file('GR17_TotalPopulationMFTrend.svg')   

 # GR 18 Urban Rural Total Population Trend
    bar_chart = pg.StackedBar(fill=True)
    bar_chart.title = 'Urban / Rural Population Trend'
    bar_chart.x_labels = sorted_data_columns
    for city in sorted_data_rows:   
        bar_chart.add("Urban",  data3.ix[city])
        bar_chart.add("Rural", data4.ix[city])
    bar_chart.render_to_file('GR18_TotalPopulationURTrend.svg')   


    
# GR 19 Total Population Prediction
def plotPopulationPrediction(data, data1, years):
    real_data = data
    real_data_columns = list(real_data.columns.values)
    real_data_rows = list(real_data.index.values)
       
    predicted_data = data1

    bar_chart = pg.Bar(fill=True)
    bar_chart.title = 'Population Prediction'
    bar_chart.x_labels = real_data_columns
    for city in real_data_rows:   
        #bar_chart.add("Total", sorted_data.ix[city])
        bar_chart.add("Real",  data.ix[city])
        bar_chart.add("Predicted", data1.ix[city])
    bar_chart.render_to_file('GR19_PopulationPrediction.svg')