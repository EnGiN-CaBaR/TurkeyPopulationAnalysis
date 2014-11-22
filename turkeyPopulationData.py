'''
Created on Nov 4, 2014

@author: engin
'''    
# coding=utf-8

import pandas as pd
import numpy as np

CITIES = 'Cities'
CITY_TOTAL = 'City_Total' 
CITY_MALE = 'City_Male' 
CITY_FEMALE = 'City_Female' 
CITYCENTER_TOTAL = 'CityCenter_Total' 
CITYCENTER_MALE = 'CityCenter_Male'
CITYCENTER_FEMALE = 'CityCenter_Female'
VILLAGES_TOTAL = 'Villages_Total'
VILLAGES_MALE = 'Villages_Male'
VILLAGES_FEMALE = 'Villages_Female'

def getTurkeyPopulationsByYears(data, years):
    """
    This function returns the Turkey's total population of entered years as a pandas object. 
    data is our dictionary which has keys as years and values as dataframes. 
    years is our year list.
    """  
    print "Entering into getTurkeyPopulationsByYears()"
    total_Turkey_Population = {}
    s = 'Turkiye'
    for year in list(years):
        t = {}
        df = data[year]
        pop = df[df.Cities == 'Turkiye'.decode('utf-8')][CITY_TOTAL].head()
        t[s] = float(pop)
        total_Turkey_Population[year] = t
    print "Exiting from into getTurkeyPopulationsByYears()"
    return pd.DataFrame(total_Turkey_Population)

def getTurkeyPopulationsByYearsInMale(data, years):
    """
    This function returns the Turkey's total male population of entered years as a pandas object.
    data is our dictionary which has keys as years and values as dataframes. 
    years is our year list.
    """ 
    print "Entering into getTurkeyPopulationsByYearsInMale()"
    total_Turkey_Population_InMale = {}
    s = 'Turkiye'
    for year in list(years):
        t = {}
        df = data[year]
        pop = df[df.Cities == 'Turkiye'.decode('utf-8')][CITY_MALE].head()
        t[s] = float(pop)
        total_Turkey_Population_InMale[year] = t
    print "Exiting into getTurkeyPopulationsByYearsInMale()"
    return pd.DataFrame(total_Turkey_Population_InMale)

def getTurkeyPopulationsByYearsInFemale(data, years):
    """
    This function returns the Turkey's total female population of entered years as a pandas object. 
    data is our dictionary which has keys as years and values as dataframes. 
    years is our year list.
    """  
    print "Entering into getTurkeyPopulationsByYearsInFemale()"
    total_Turkey_Population_InFemale = {}
    s = 'Turkiye'
    for year in list(years):
        t = {}
        df = data[year]
        pop = df[df.Cities == 'Turkiye'.decode('utf-8')][CITY_FEMALE].head()
        t[s] = float(pop)
        total_Turkey_Population_InFemale[year] = t
    print "Exiting from into getTurkeyPopulationsByYearsInFemale()"
    return pd.DataFrame(total_Turkey_Population_InFemale)

def getTurkeyPopulationsByYearsInCityCenterTotal(data, years):
    """
    This function returns the Turkey's total urban population of entered years as a pandas object. 
    data is our dictionary which has keys as years and values as dataframes. 
    years is our year list.
    """ 
    print "Entering into getTurkeyPopulationsByYearsInCityCenterTotal()"
    total_Turkey_Population_InCityCenter = {}
    s = 'Turkiye'
    for year in list(years):
        t = {}
        df = data[year]
        pop = df[df.Cities == 'Turkiye'.decode('utf-8')][CITYCENTER_TOTAL].head()
        t[s] = float(pop)
        total_Turkey_Population_InCityCenter[year] = t
    print "Exiting from into getTurkeyPopulationsByYearsInCityCenterTotal()"
    return pd.DataFrame(total_Turkey_Population_InCityCenter)

def getTurkeyPopulationsByYearsInVillageTotal(data, years):
    """
    This function returns the Turkey's total rural population of entered years as a pandas object. 
    data is our dictionary which has keys as years and values as dataframes. 
    years is our year list.
    """ 
    print "Entering into getTurkeyPopulationsByYearsInVillageTotal()"
    total_Turkey_Population_InVillage = {}
    s = 'Turkiye'
    for year in list(years):
        t = {}
        df = data[year]
        pop = df[df.Cities == 'Turkiye'.decode('utf-8')][VILLAGES_TOTAL].head()
        t[s] = float(pop)
        total_Turkey_Population_InVillage[year] = t
    print "Exiting from into getTurkeyPopulationsByYearsInVillageTotal()"
    return pd.DataFrame(total_Turkey_Population_InVillage)

def getCityCenterPopulationsByYears(data, city, years):
    """
    This function returns urban population of cities as rows and years as columns as a pandas object. 
    data is our dictionary which has keys as years and values as dataframes. 
    years is our year list.
    city is a list which can be 'All' to select whole cities or you can give specific city names
    """  
    print "Entering into getCityCenterPopulationsByYears()"
    total_CityCenter_Population = {}
    for year in list(years):
        cityInYear = data[year]['Cities'].tolist()[1:]
        #print "year is ", year
        cities = {}
        if city[0] == 'All':
            cityNames = data[year]['Cities'].tolist()[1:]
        else:
            cityNames = [c.decode('utf-8') for c in city]
        df = data[year][1:]
        for cityName in cityNames:
            #print cityName
            if cityName in cityInYear:
                #print cityName, " is now reading"
                s = df[df.Cities == cityName][CITYCENTER_TOTAL]
                cities[cityName] = float(s.values)
        total_CityCenter_Population[year] = cities
    print "Exiting from into getCityCenterPopulationsByYears()"
    return pd.DataFrame(total_CityCenter_Population)

def getCityPopulationsByYearsInMale(data , city, years):
    """
    This function returns male population of cities as rows and years as columns as a pandas object. 
    data is our dictionary which has keys as years and values as dataframes. 
    years is our year list.
    city is a list which can be 'All' to select whole cities or you can give specific city names
    """  
    print "Entering into getCityPopulationsByYearsInMale()"
    total_CityCenter_MalePopulation = {}
    for year in list(years):
        cityInYear = data[year]['Cities'].tolist()[1:]
        #print "year is ", year
        cities = {}
        if city[0] == 'All':
            cityNames = data[year]['Cities'].tolist()[1:]
        else:
            cityNames = [c.decode('utf-8') for c in city]
        df = data[year][1:]
        for cityName in cityNames:
            if cityName in cityInYear:
                #print cityName, " is now reading"
                s = df[df.Cities == cityName][CITYCENTER_MALE].head()
                cities[cityName] = float(s)
        total_CityCenter_MalePopulation[year] = cities
    print "Exiting from getCityPopulationsByYearsInMale()"
    return pd.DataFrame(total_CityCenter_MalePopulation)

def getCityPopulationsByYearsInFemale(data, city, years):
    """
    This function returns female population of cities as rows and years as columns as a pandas object. 
    data is our dictionary which has keys as years and values as dataframes. 
    years is our year list.
    city is a list which can be 'All' to select whole cities or you can give specific city names
    """  
    print "Entering into getCityPopulationsByYearsInFemale()"
    total_CityCenter_FemalePopulation = {}
    for year in list(years):
        cityInYear = data[year]['Cities'].tolist()[1:]
        #print "year is ", year
        cities = {}
        if city[0] == 'All':
            cityNames = data[year]['Cities'].tolist()[1:]
        else:
            cityNames = [c.decode('utf-8') for c in city]
        df = data[year][1:]
        for cityName in cityNames:
            if cityName in cityInYear:
                #print cityName, " is now reading"
                s = df[df.Cities == cityName][CITYCENTER_FEMALE].head()
                cities[cityName] = float(s)
        total_CityCenter_FemalePopulation[year] = cities
    print "Exiting from into getCityPopulationsByYearsInFemale()"
    return pd.DataFrame(total_CityCenter_FemalePopulation)

def getVillagePopulationsByYears(data, city, years):
    """
    This function returns rural population of cities as rows and years as columns as a pandas object. 
    data is our dictionary which has keys as years and values as dataframes. 
    years is our year list.
    city is a list which can be 'All' to select whole cities or you can give specific city names
    """  
    print "Entering into getVillagePopulationsByYears()"
    total_Village_Population = {}
    for year in list(years):
        cityInYear = data[year]['Cities'].tolist()[1:]
        #print "year is ", year
        cities = {}
        if city[0] == 'All':
            cityNames = data[year]['Cities'].tolist()[1:]
        else:
            cityNames = [c.decode('utf-8') for c in city]
        df = data[year][1:]
        for cityName in cityNames:
            if cityName in cityInYear:
                #print cityName, " is now reading"
                s = df[df.Cities == cityName][VILLAGES_TOTAL].head()
                cities[cityName] = float(s)
        total_Village_Population[year] = cities
    print "Exiting from getVillagePopulationsByYears()"
    return pd.DataFrame(total_Village_Population)

def getVillagePopulationsByYearsInMale(data, city, years):
    """
    This function returns rural male population of cities as rows and years as columns as a pandas object. 
    data is our dictionary which has keys as years and values as dataframes. 
    years is our year list.
    city is a list which can be 'All' to select whole cities or you can give specific city names
    """   
    print "Entering into getVillagePopulationsByYearsInMale()"
    total_Village_MalePopulation = {}
    for year in list(years):
        cityInYear = data[year]['Cities'].tolist()[1:]
        #print "year is ", year
        cities = {}
        if city[0] == 'All':
            cityNames = data[year]['Cities'].tolist()[1:]
        else:
            cityNames = [c.decode('utf-8') for c in city]
        df = data[year][1:]
        for cityName in cityNames:
            if cityName in cityInYear:
                #print cityName, " is now reading"
                s = df[df.Cities == cityName][VILLAGES_MALE].head()
                cities[cityName] = float(s)
        total_Village_MalePopulation[year] = cities
    print "Exiting from getVillagePopulationsByYearsInMale()"
    return pd.DataFrame(total_Village_MalePopulation)

def getVillagePopulationsByYearsInFemale(data, city, years):
    """
    This function returns rural female population of cities as rows and years as columns as a pandas object. 
    data is our dictionary which has keys as years and values as dataframes. 
    years is our year list.
    city is a list which can be 'All' to select whole cities or you can give specific city names
    """  
    print "Entering into getVillagePopulationsByYearsInFemale()"
    total_Village_FemalePopulation = {}
    for year in list(years):
        cityInYear = data[year]['Cities'].tolist()[1:]
        #print "year is ", year
        cities = {}
        if city[0] == 'All':
            cityNames = data[year]['Cities'].tolist()[1:]
        else:
            cityNames = [c.decode('utf-8') for c in city]
        df = data[year][1:]
        for cityName in cityNames:
            if cityName in cityInYear:
                #print cityName, " is now reading"
                s = df[df.Cities == cityName][VILLAGES_FEMALE].head()
                cities[cityName] = float(s)
        total_Village_FemalePopulation[year] = cities
    print "Exiting from getVillagePopulationsByYearsInFemale()"
    return pd.DataFrame(total_Village_FemalePopulation)

def getCityNumberByYears(data, years):
    """
    This function returns count of cities at an entered year. 
    data is our dictionary which has keys as years and values as dataframes. 
    years is our year list.
    """  
    print "Entering into getCityNumberByYears()"
    city_count = {}
    for year in list(years):
        cityInYear = data[year]['Cities'].tolist()[1:]
        #print "year is ", year
        city_count[year] = len(cityInYear)
    print "Exiting from getCityNumberByYears()"
    return city_count

def populationPredictionForTurkey(dft):
    """
    This function returns total population prediction data from 2010 to 2050. 
    """  
    print "Entering into getCityNumberByYears()"
    growth_rate = (dft['1990'].values - dft['1985'].values) / dft['1990'].values
    P1995 = (dft['1990'].values) * ((np.e) ** (growth_rate * 1))
    print P1995
    print "Exiting from getCityNumberByYears()"
    
