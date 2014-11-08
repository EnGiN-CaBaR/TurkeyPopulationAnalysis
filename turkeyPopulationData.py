'''
Created on Nov 4, 2014

@author: engin
'''    
# coding=utf-8-sig

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
    total_Turkey_Population = {}
    s = 'Türkiye'
    for year in list(years):
        t = {}
        df = data[year]
        pop = df[df.Cities == 'Türkiye'.decode('utf-8')][CITY_TOTAL].head()
        t[s] = float(pop)
        total_Turkey_Population[year] = t
    return pd.DataFrame(total_Turkey_Population)

def getTurkeyPopulationsByYearsInMale(data, years):
    total_Turkey_Population_InMale = {}
    s = 'Türkiye'
    for year in list(years):
        t = {}
        df = data[year]
        pop = df[df.Cities == 'Türkiye'.decode('utf-8')][CITY_MALE].head()
        t[s] = float(pop)
        total_Turkey_Population_InMale[year] = t
    return pd.DataFrame(total_Turkey_Population_InMale)

def getTurkeyPopulationsByYearsInFemale(data, years):
    total_Turkey_Population_InFemale = {}
    s = 'Türkiye'
    for year in list(years):
        t = {}
        df = data[year]
        pop = df[df.Cities == 'Türkiye'.decode('utf-8')][CITY_FEMALE].head()
        t[s] = float(pop)
        total_Turkey_Population_InFemale[year] = t
    return pd.DataFrame(total_Turkey_Population_InFemale)

def getCityCenterPopulationsByYears(data, years, city):
    total_CityCenter_Population = {}
    for year in list(years):
        cities = {}
        if city == 'All':
            cityNames = data[year]['Cities'].tolist()[1:]
        else:
            cityNames = city
        df = data[year][1:]
        for cityName in cityNames:
            s = df[df.Cities == cityName][CITYCENTER_TOTAL]
            cities[cityName] = float(s.values)
        total_CityCenter_Population[year] = cities
    return pd.DataFrame(total_CityCenter_Population)

def getCityPopulationsByYearsInMale(data ,city, years):
    total_CityCenter_MalePopulation = {}
    for year in list(years):
        cities = {}
        if city[0] == 'All':
            cityNames = data[year]['Cities'].tolist()[1:]
        else:
            cityNames = city
        for cityName in cityNames:
            df = data[year]
            s = df[df.Cities == cityName][CITYCENTER_MALE].head()
            cities[cityName] = float(s)
        total_CityCenter_MalePopulation[year] = cities
    return pd.DataFrame(total_CityCenter_MalePopulation)

def getCityPopulationsByYearsInFemale(data, city, years):
    total_CityCenter_FemalePopulation = {}
    for year in list(years):
        cities = {}
        if city[0] == 'All':
            cityNames = data[year]['Cities'].tolist()[1:]
        else:
            cityNames = city
        for cityName in cityNames:
            df = data[year]
            s = df[df.Cities == cityName][CITYCENTER_FEMALE].head()
            cities[cityName] = float(s)
        total_CityCenter_FemalePopulation[year] = cities
    return pd.DataFrame(total_CityCenter_FemalePopulation)

def getVillagePopulationsByYears(data, city, years):
    total_Village_Population = {}
    for year in list(years):
        cities = {}
        if city[0] == 'All':
            cityNames = data[year]['Cities'].tolist()[1:]
        else:
            cityNames = city
        for cityName in cityNames:
            df = data[year]
            s = df[df.Cities == cityName][VILLAGES_TOTAL].head()
            cities[cityName] = float(s)
        total_Village_Population[year] = cities
    return pd.DataFrame(total_Village_Population)

def getVillagePopulationsByYearsInMale(data, city, years):
    total_Village_MalePopulation = {}
    for year in list(years):
        cities = {}
        if city[0] == 'All':
            cityNames = data[year]['Cities'].tolist()[1:]
        else:
            cityNames = city
        for cityName in cityNames:
            df = data[year]
            s = df[df.Cities == cityName][VILLAGES_MALE].head()
            cities[cityName] = float(s)
        total_Village_MalePopulation[year] = cities
    return pd.DataFrame(total_Village_MalePopulation)

def getVillagePopulationsByYearsInFemale(data, city, years):
    total_Village_FemalePopulation = {}
    for year in list(years):
        cities = {}
        if city[0] == 'All':
            cityNames = data[year]['Cities'].tolist()[1:]
        else:
            cityNames = city
        for cityName in cityNames:
            df = data[year]
            s = df[df.Cities == cityName][VILLAGES_FEMALE].head()
            cities[cityName] = float(s)
        total_Village_FemalePopulation[year] = cities
    return pd.DataFrame(total_Village_FemalePopulation)
