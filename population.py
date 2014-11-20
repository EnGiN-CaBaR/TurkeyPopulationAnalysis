'''
Created on Nov 4, 2014

@author: engin
'''
# coding=utf-8

import fileUtil as f
import turkeyPopulationData as tpd
from flask import Flask
from flask import request
import json
from flask.templating import render_template
 
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
        f1 = request.args.get('Year', '')
        year.append(f1)
        cityCenter = tpd.getCityCenterPopulationsByYears(data, ['All'], year)
        cityVillage = tpd.getVillagePopulationsByYears(data, ['All'], year)
        cityTotal = cityCenter.fillna(0) + cityVillage.fillna(0)
        jsonDic = json.loads(cityTotal[f1].to_json())
        for city in jsonDic.keys():
            jsonDic[plate[city]] = jsonDic.pop(city)
        return json.dumps(jsonDic)
            
if __name__ == "__main__":
    fs = f.find_file_names('years', '*.xlsx')
    data = f.get_names_data(fs, 'xlsx')
    yKeys = data.keys()
    yKeys.sort()
    
    plate = f.getPlate()
    app.run(host='0.0.0.0', debug=True,port=80)
    
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


#     turkeyPop = getTurkeyPopulationsByYears(data, yKeys)
#     pg.plotRegionOverTotalPopulationInYears(turkeyPop)