'''
Created on Nov 4, 2014

@author: engin
'''    
# coding=utf-8

import pandas as pd

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
    print "Entering into getTurkeyPopulationsByYears()"
    total_Turkey_Population = {}
    s = 'Türkiye'
    for year in list(years):
        t = {}
        df = data[year]
        pop = df[df.Cities == 'Türkiye'.decode('utf-8')][CITY_TOTAL].head()
        t[s] = float(pop)
        total_Turkey_Population[year] = t
    print "Exiting from into getTurkeyPopulationsByYears()"
    return pd.DataFrame(total_Turkey_Population)

def getTurkeyPopulationsByYearsInMale(data, years):
    print "Entering into getTurkeyPopulationsByYearsInMale()"
    total_Turkey_Population_InMale = {}
    s = 'Türkiye'
    for year in list(years):
        t = {}
        df = data[year]
        pop = df[df.Cities == 'Türkiye'.decode('utf-8')][CITY_MALE].head()
        t[s] = float(pop)
        total_Turkey_Population_InMale[year] = t
    print "Exiting into getTurkeyPopulationsByYearsInMale()"
    return pd.DataFrame(total_Turkey_Population_InMale)

def getTurkeyPopulationsByYearsInFemale(data, years):
    print "Entering into getTurkeyPopulationsByYearsInFemale()"
    total_Turkey_Population_InFemale = {}
    s = 'Türkiye'
    for year in list(years):
        t = {}
        df = data[year]
        pop = df[df.Cities == 'Türkiye'.decode('utf-8')][CITY_FEMALE].head()
        t[s] = float(pop)
        total_Turkey_Population_InFemale[year] = t
    print "Exiting from into getTurkeyPopulationsByYearsInFemale()"
    return pd.DataFrame(total_Turkey_Population_InFemale)

def getCityCenterPopulationsByYears(data, city, years):
    print "Entering into getCityCenterPopulationsByYears()"
    total_CityCenter_Population = {}
    for year in list(years):
        cityInYear = data[year]['Cities'].tolist()[1:]
        print "year is ", year
        cities = {}
        if city[0] == 'All':
            cityNames = data[year]['Cities'].tolist()[1:]
        else:
            cityNames = [c.decode('utf-8') for c in city]
        df = data[year][1:]
        for cityName in cityNames:
            if cityName in cityInYear:
                print cityName, " is now reading"
                s = df[df.Cities == cityName][CITYCENTER_TOTAL]
                cities[cityName] = float(s.values)
        total_CityCenter_Population[year] = cities
    print "Exiting from into getCityCenterPopulationsByYears()"
    return pd.DataFrame(total_CityCenter_Population)

def getCityPopulationsByYearsInMale(data ,city, years):
    print "Entering into getCityPopulationsByYearsInMale()"
    total_CityCenter_MalePopulation = {}
    for year in list(years):
        cityInYear = data[year]['Cities'].tolist()[1:]
        print "year is ", year
        cities = {}
        if city[0] == 'All':
            cityNames = data[year]['Cities'].tolist()[1:]
        else:
            cityNames = [c.decode('utf-8') for c in city]
        df = data[year][1:]
        for cityName in cityNames:
            if cityName in cityInYear:
                print cityName, " is now reading"
                s = df[df.Cities == cityName][CITYCENTER_MALE].head()
                cities[cityName] = float(s)
        total_CityCenter_MalePopulation[year] = cities
    print "Exiting from getCityPopulationsByYearsInMale()"
    return pd.DataFrame(total_CityCenter_MalePopulation)

def getCityPopulationsByYearsInFemale(data, city, years):
    print "Entering into getCityPopulationsByYearsInFemale()"
    total_CityCenter_FemalePopulation = {}
    for year in list(years):
        cityInYear = data[year]['Cities'].tolist()[1:]
        print "year is ", year
        cities = {}
        if city[0] == 'All':
            cityNames = data[year]['Cities'].tolist()[1:]
        else:
            cityNames = [c.decode('utf-8') for c in city]
        df = data[year][1:]
        for cityName in cityNames:
            if cityName in cityInYear:
                print cityName, " is now reading"
                s = df[df.Cities == cityName][CITYCENTER_FEMALE].head()
                cities[cityName] = float(s)
        total_CityCenter_FemalePopulation[year] = cities
    print "Exiting from into getCityPopulationsByYearsInFemale()"
    return pd.DataFrame(total_CityCenter_FemalePopulation)

def getVillagePopulationsByYears(data, city, years):
    print "Entering into getVillagePopulationsByYears()"
    total_Village_Population = {}
    for year in list(years):
        cityInYear = data[year]['Cities'].tolist()[1:]
        print "year is ", year
        cities = {}
        if city[0] == 'All':
            cityNames = data[year]['Cities'].tolist()[1:]
        else:
            cityNames = [c.decode('utf-8') for c in city]
        df = data[year][1:]
        for cityName in cityNames:
            if cityName in cityInYear:
                print cityName, " is now reading"
                s = df[df.Cities == cityName][VILLAGES_TOTAL].head()
                cities[cityName] = float(s)
        total_Village_Population[year] = cities
    print "Exiting from getVillagePopulationsByYears()"
    return pd.DataFrame(total_Village_Population)

def getVillagePopulationsByYearsInMale(data, city, years):
    print "Entering into getVillagePopulationsByYearsInMale()"
    total_Village_MalePopulation = {}
    for year in list(years):
        cityInYear = data[year]['Cities'].tolist()[1:]
        print "year is ", year
        cities = {}
        if city[0] == 'All':
            cityNames = data[year]['Cities'].tolist()[1:]
        else:
            cityNames = [c.decode('utf-8') for c in city]
        df = data[year][1:]
        for cityName in cityNames:
            if cityName in cityInYear:
                print cityName, " is now reading"
                s = df[df.Cities == cityName][VILLAGES_MALE].head()
                cities[cityName] = float(s)
        total_Village_MalePopulation[year] = cities
    print "Exiting from getVillagePopulationsByYearsInMale()"
    return pd.DataFrame(total_Village_MalePopulation)

def getVillagePopulationsByYearsInFemale(data, city, years):
    print "Entering into getVillagePopulationsByYearsInFemale()"
    total_Village_FemalePopulation = {}
    for year in list(years):
        cityInYear = data[year]['Cities'].tolist()[1:]
        print "year is ", year
        cities = {}
        if city[0] == 'All':
            cityNames = data[year]['Cities'].tolist()[1:]
        else:
            cityNames = [c.decode('utf-8') for c in city]
        df = data[year][1:]
        for cityName in cityNames:
            if cityName in cityInYear:
                print cityName, " is now reading"
                s = df[df.Cities == cityName][VILLAGES_FEMALE].head()
                cities[cityName] = float(s)
        total_Village_FemalePopulation[year] = cities
    print "Exiting from getVillagePopulationsByYearsInFemale()"
    return pd.DataFrame(total_Village_FemalePopulation)
