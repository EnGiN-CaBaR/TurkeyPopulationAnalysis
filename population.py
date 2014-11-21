'''
Created on Nov 4, 2014

@author: engin
'''
# coding=utf-8

import fileUtil as f
import turkeyPopulationData as tpd
import json
import population_graph as pg
try:
    from flask import Flask
    from flask import request
    from flask.templating import render_template
except Exception:
    print "You should install Flask microframework"
 
app = Flask(__name__)

@app.route('/index', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
@app.route('/totalturkeypopulation', methods=['GET', 'POST'])
def getTurkeyPopulation():
    if request.method == 'GET':
        return render_template('totalpopulation.html')
    else:
        year = []
        jsonDic = {}
        density = {}
        f1 = request.args.get('Year', '')
        year.append(f1)
        cityCenter = tpd.getCityCenterPopulationsByYears(data, ['All'], year)
        cityVillage = tpd.getVillagePopulationsByYears(data, ['All'], year)
        cityTotal = cityCenter.fillna(0) + cityVillage.fillna(0)
        
        totalJsonDic = json.loads(cityTotal[f1].to_json())
        centerJsonDic = json.loads(cityCenter[f1].to_json())
        villageJsonDic = json.loads(cityVillage[f1].to_json())
        
        selectedYearCities = set(totalJsonDic.keys())
        currentCities = set(plate.keys())
        differenceCities = currentCities-selectedYearCities
        
        for i in range(len(differenceCities)):
            city = differenceCities.pop()
            totalJsonDic[city] = 0
            centerJsonDic[city] = 0
            villageJsonDic[city] = 0
        
        jsonDic["total"] = totalJsonDic        
        jsonDic["center"] = centerJsonDic
        jsonDic["village"] = villageJsonDic
        
        for k in jsonDic.keys():
            temp = jsonDic[k]
            for l in temp.keys():    
                temp[plate[l]] = temp.pop(l)
                if k == "total":
                    density[plate[l]] = round(temp[plate[l]] / float(cityArea[plate[l]]))
        jsonDic["cityDensity"] = density
        return json.dumps(jsonDic)
    
    
@app.route('/turkeymalefemalemap', methods=['GET', 'POST'])
def getTurkeymalefemalemapPopulation():
    if request.method == 'GET':
        return render_template('turkeymalefemalemap.html')
    else:
        year = []
        jsonDic = {}
        f1 = request.args.get('Year', '')
        year.append(f1)
        cityCenterMale = tpd.getCityPopulationsByYearsInMale(data, ['All'], year)
        villageMale = tpd.getVillagePopulationsByYearsInMale(data, ['All'], year)
        
        cityCenterFeMale = tpd.getCityPopulationsByYearsInFemale(data, ['All'], year)
        villageFemale = tpd.getVillagePopulationsByYearsInFemale(data, ['All'], year)
        
        cityTotalMale = cityCenterMale.fillna(0) + villageMale.fillna(0)
        cityTotalFeMale = cityCenterFeMale.fillna(0) + villageFemale.fillna(0)
        diffGender = cityTotalMale - cityTotalFeMale;
        
        maleJsonDic = json.loads(cityTotalMale[f1].to_json())
        femaleJsonDic = json.loads(cityTotalFeMale[f1].to_json())
        diffGenderJsonDic = json.loads(diffGender[f1].to_json())
        
        selectedYearCities = set(maleJsonDic.keys())
        currentCities = set(plate.keys())
        differenceCities = currentCities-selectedYearCities
        
        for i in range(len(differenceCities)):
            city = differenceCities.pop()
            maleJsonDic[city] = 0
            femaleJsonDic[city] = 0
            diffGenderJsonDic[city] = 0
        
        jsonDic["male"] = maleJsonDic        
        jsonDic["female"] = femaleJsonDic
        jsonDic["difference"] = diffGenderJsonDic
        
        for k in jsonDic.keys():
            temp = jsonDic[k]
            for l in temp.keys():    
                temp[plate[l]] = temp.pop(l)               
        return json.dumps(jsonDic)

@app.route('/urbanizationinturkey', methods=['GET', 'POST'])
def getUrbanizationInturkey():
    if request.method == 'GET':
        return render_template('urbanizationinturkey.html')
    else:
        year = []
        jsonDic = {}
        f1 = request.args.get('Year', '')
        year.append(f1)
        cityCenter = tpd.getCityCenterPopulationsByYears(data, ['All'], year)
        village = tpd.getVillagePopulationsByYears(data, ['All'], year)
                
        cityCenter = cityCenter.fillna(0)
        village = village.fillna(0)
        urbanization = cityCenter - village;
        
        citycenterJsonDic = json.loads(cityCenter[f1].to_json())
        villageJsonDic = json.loads(village[f1].to_json())
        urbanizationJsonDic = json.loads(urbanization[f1].to_json())
        
        selectedYearCities = set(citycenterJsonDic.keys())
        currentCities = set(plate.keys())
        differenceCities = currentCities-selectedYearCities
        
        for i in range(len(differenceCities)):
            city = differenceCities.pop()
            citycenterJsonDic[city] = 0
            villageJsonDic[city] = 0
            urbanizationJsonDic[city] = 0
        
        jsonDic["city"] = citycenterJsonDic        
        jsonDic["village"] = villageJsonDic
        jsonDic["urbanization"] = urbanizationJsonDic
        
        for k in jsonDic.keys():
            temp = jsonDic[k]
            for l in temp.keys():    
                temp[plate[l]] = temp.pop(l)               
        return json.dumps(jsonDic)

            
if __name__ == "__main__":
    fs = f.find_file_names('years', '*.xlsx')
    data = f.get_names_data(fs, 'xlsx')
    yKeys = data.keys()
    yKeys.sort()
    
    plate = f.getPlate()
    cityArea = f.getArea()
    #app.run(host='0.0.0.0', debug=True)
    
#     fs = find_file_names('years', '*.xlsx')
#     data = get_names_data(fs, 'xlsx')
#     yKeys = data.keys()
#     yKeys.sort()
    
#########################################################
#     ccp = getCityCenterPopulationsByYears(data, ['All'], yKeys)
#     pg.plotHorizontalBarTopFive(ccp, yKeys)
#     pg.plotLineChartTopTen(ccp, yKeys)
##########################################################

##########################################################
#     ccpr = getVillagePopulationsByYears(data, ['All'], yKeys)
#     pg.plotLineChartTopTenRural(ccpr, yKeys)
##########################################################
#     cpm = getCityPopulationsByYearsInMale(data, ['All'], yKeys)
#     cpf = getCityPopulationsByYearsInFemale(data, ['All'], yKeys)
#     pg.plotPieChartTopFiveCity(cpm, cpf, yKeys)

###########################################################
#     regions = find_file_names('cityRegions', '*.txt')
#     cityRegion = getRegionFiles(regions)
#     cpm = getCityPopulationsByYearsInMale(data, ['All'], yKeys)
#     cpf = getCityPopulationsByYearsInFemale(data, ['All'], yKeys)
#     pg.plotPyramidChart(cpm, cpf, yKeys, cityRegion)
############################################################

###########################################################
    regions = f.find_file_names('cityRegions', '*.txt')
    cityRegion = f.getRegionFiles(regions)
    cpm = tpd.getCityPopulationsByYearsInMale(data, ['All'], yKeys)
    cpf = tpd.getCityPopulationsByYearsInFemale(data, ['All'], yKeys)
    pg.plotRegionOverTotalPopulationInYears(cpm, cpf, yKeys, cityRegion)
############################################################


#     turkeyPop = getTurkeyPopulationsByYears(data, yKeys)
#     pg.plotRegionOverTotalPopulationInYears(turkeyPop)