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


"""
To run local server use this module.
Creating an instance of Flask class. The first argument 
is the name of the application’s module or package that is
for us our main method
"""
app = Flask(__name__)

@app.route('/index', methods=['GET'])
def index():
    """
    This is a restful web service. When user open the index link from the browser,
    this function is called and render index.html file. In technically when this 
    link is clicked browser makes an http get request and takes index.html as response.
    """
    if request.method == 'GET':
        return render_template('index.html')
    
@app.route('/totalturkeypopulation', methods=['GET', 'POST'])
def getTurkeyPopulation():
    """
    This is a restful web service. When user open the totalturkeypopulation page from the browser,
    this function is called and render totalpopulation.html file. After webpage rendered user can
    make request with page element to view TurkeyPopulation changing by years, for example.
    In technically when this link is clicked browser makes an http get request and takes 
    totalpopulation.html as response. User can choose year to view TurkeyPopulation changing by years
    which is http post request and this request gets json object. This json object has three element
    total, center and village population of cities. 
    """
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
    """
    This is a restful web service. When user open the turkeymalefemalemap page from the browser,
    this function is called and render turkeymalefemalemap.html file. After webpage rendered user can
    make request with page element to view Turkey Male-Female Population changing by years, for example.
    In technically when this link is opened by browser makes an http get request and takes 
    totalpopulation.html as response. User can choose year to view Turkey Male Female Population changing by years
    which is http post request and this request gets json object. This json object has three element
    male, female and difference population of cities. 
    """
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
    """
    This is a restful web service. When user open the urbanizationinturkey page from the browser,
    this function is called and render urbanizationinturkey.html file. After webpage rendered user can
    make request with page element to view Urbanization changing by years, for example.
    In technically when this link is opened by browser makes an http get request and takes 
    urbanizationinturkey.html as response. User can choose year to view Urbanization changing by years
    which is http post request and this request gets json object. This json object has three element
    city, village and urbanization population of cities. 
    """
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
    """
    Program is executed from main method by interpreter. When program executed
    reads datas from excel files, platefile and cityAreafile. After that we run
    local server with run() method. User can reach server with server's ip adress
    default port is 5000 and first page is "/index". To reach from local, 
    localhost:5000/index is welcome page.
    """
    fs = f.find_file_names('years', '*.xlsx')
    data = f.get_names_data(fs, 'xlsx')
    yKeys = data.keys()
    yKeys.sort()
    
    plate = f.getPlate()
    cityArea = f.getArea()
    app.run(host='0.0.0.0', debug=True)