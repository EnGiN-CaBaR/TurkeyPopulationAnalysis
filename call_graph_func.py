import fileUtil as f
import turkeyPopulationData as tpd
import json
import population_graph as pg


fs = f.find_file_names('years', '*.xlsx')
data = f.get_names_data(fs, 'xlsx')
yKeys = data.keys()
yKeys.sort()

# GR 1 Urban Population Percentage of Top-5 cities
ccpy = tpd.getCityCenterPopulationsByYears(data, ['All'], yKeys).fillna(0)
ccpy = (ccpy/ccpy.sum()) * 100
pg.plotTopFiveCityUrbanPopulationPercentage(ccpy, sorted(yKeys,reverse=True))

# GR 2 Village Population Percentage of Top-5 cities
cvpy = tpd.getVillagePopulationsByYears(data, ['All'], yKeys).fillna(0)
cvpy = (cvpy/cvpy.sum()) * 100
pg.plotTopFiveCityVillagePopulationPercentage(cvpy, sorted(yKeys,reverse=True))

# GR 3 Urbanization Percentage of Top-5 Urbanized cities: City /(City + Urban)
ccpy = tpd.getCityCenterPopulationsByYears(data, ['All'], yKeys).fillna(0)
cvpy = tpd.getVillagePopulationsByYears(data, ['All'], yKeys).fillna(0)
uprc = 100*ccpy/(ccpy+cvpy)
pg.plotTopFiveUrbanizedCityUrbanizationPercentage(uprc, sorted(yKeys,reverse=True))    

# GR 4 Urbanization Percentage of 1965's Least-5 Urbanized cities: City /(City + Urban)
ccpy = tpd.getCityCenterPopulationsByYears(data, ['All'], yKeys).fillna(1)
cvpy = tpd.getVillagePopulationsByYears(data, ['All'], yKeys).fillna(1)
uprc = 100*ccpy/(ccpy+cvpy)
pg.plotLeastFiveUrbanizedCityUrbanizationPercentage(uprc, sorted(yKeys,reverse=False))    

# GR 5 Urbanization Percentage of Turkey: City / Turkey
tpcy = tpd.getTurkeyPopulationsByYearsInCityCenterTotal(data, yKeys)
tpty = tpd.getTurkeyPopulationsByYears(data, yKeys)
tprc = 100*tpcy/(tpty)
pg.plotTurkeyUrbanizationPercentage(tprc, sorted(yKeys,reverse=False))    


# GR 6 URBAN Population Growth of Top-5 cities
ccpy = tpd.getCityCenterPopulationsByYears(data, ['All'], yKeys)
pg.plotTopFiveCityPopulationGrowth(ccpy, sorted(yKeys,reverse=True))


# GR 7 Male - Female Ratio in Total Population
tptot = tpd.getTurkeyPopulationsByYears(data,yKeys)
tptotMale = tpd.getTurkeyPopulationsByYearsInMale(data, yKeys)
tptotFemale = tpd.getTurkeyPopulationsByYearsInFemale(data, yKeys)
pg.plotDataMaleFemalePercentBAR(tptot,tptotMale,tptotFemale,sorted(yKeys,reverse=True))


# GR 8 Village Population Change of Top-5 cities
vcpy = tpd.getVillagePopulationsByYears(data, ['All'], yKeys)
pg.plotTopFiveVillagePopulationGrowth(vcpy, sorted(yKeys,reverse=True))


# GR 9 Top-10 Urban Female Percentage (1965)
fpcy = tpd.getCityPopulationsByYearsInFemale(data, ['All'], yKeys).fillna(0)
ccpy = tpd.getCityCenterPopulationsByYears(data,['All'],yKeys).fillna(1)
fprc = 100*fpcy/(ccpy)
pg.plotTop10UrbanFemalePercent(fprc,sorted(yKeys,reverse=False))

# GR 10 Top-10 Village Female Percentage (1965)
fpvy = tpd.getVillagePopulationsByYearsInFemale(data, ['All'], yKeys).fillna(0)
cvpy = tpd.getVillagePopulationsByYears(data,['All'],yKeys).fillna(1)
fprv = 100*fpvy/(cvpy)
pg.plotTop10VillageFemalePercent(fprv,sorted(yKeys,reverse=False))

# GR 11 Top-10 Urban Male Percentage (1965)
mpcy = tpd.getCityPopulationsByYearsInMale(data, ['All'], yKeys).fillna(0)
ccpy = tpd.getCityCenterPopulationsByYears(data,['All'],yKeys).fillna(1)
mprc = 100*mpcy/(ccpy)
pg.plotTop10UrbanMalePercent(mprc,sorted(yKeys,reverse=False))

# GR 12 Top-10 Village Male Percentage (1965)
mpvy = tpd.getVillagePopulationsByYearsInMale(data, ['All'], yKeys).fillna(0)
cvpy = tpd.getVillagePopulationsByYears(data,['All'],yKeys).fillna(1)
mprv = 100*mpvy/(cvpy)
pg.plotTop10VillageMalePercent(mprv,sorted(yKeys,reverse=False))

# GR 13 Top-20 Urban Female Change Percentage
fpcy = tpd.getCityPopulationsByYearsInFemale(data, ['All'], yKeys).fillna(1000000)
fdrc = 100*(fpcy['2000']-fpcy['1965'])/fpcy['1965']
fdrc.sort(ascending=False)
pg.plotTop20UrbanFemalePercentageChange(fdrc)

# GR 14 Top-20 Village Female Change Percentage
fpvy = tpd.getVillagePopulationsByYearsInFemale(data, ['All'], yKeys).fillna(1000000)
fdrv = 100*(fpvy['2000']-fpvy['1965'])/fpvy['1965']
fdrv.sort(ascending=False)
pg.plotTop20VillageFemalePercentageChange(fdrv)

# GR 15 Top-20 Urban Male Change Percentage
mpcy = tpd.getCityPopulationsByYearsInMale(data, ['All'], yKeys).fillna(1000000)
mdrc = 100*(mpcy['2000']-mpcy['1965'])/mpcy['1965']
mdrc.sort(ascending=False)
pg.plotTop20UrbanMalePercentageChange(mdrc)

# GR 16 Top-20 Village Male Change Percentage
mpvy = tpd.getVillagePopulationsByYearsInMale(data, ['All'], yKeys).fillna(1000000)
mdrv = 100*(mpvy['2000']-mpvy['1965'])/mpvy['1965']
mdrv.sort(ascending=False)
pg.plotTop20VillageMalePercentageChange(mdrv)

# GR 17 Male / Female Total Population 
tptot = tpd.getTurkeyPopulationsByYears(data,yKeys)
tptotMale = tpd.getTurkeyPopulationsByYearsInMale(data, yKeys)
tptotFemale = tpd.getTurkeyPopulationsByYearsInFemale(data, yKeys)

# GR 18 Urban / Rural Total Population 
tptotUrban = tpd.getTurkeyPopulationsByYearsInCityCenterTotal(data, yKeys)
tptotRural = tpd.getTurkeyPopulationsByYearsInVillageTotal(data, yKeys)
pg.plotPopulationTrend(tptot,tptotMale,tptotFemale,tptotUrban,tptotRural, sorted(yKeys,reverse=True))

# GR 19 Turkey's Population Prediction 
tptot = tpd.getTurkeyPopulationsByYears(data,yKeys)
tptot['2010']=0
tptot['2020']=0
tptot['2030']=0
tptot['2040']=0
tptot['2050']=0

predictedpop = tpd.populationPredictionForTurkey(tptot)
predictedpop['1965']=0
predictedpop['1970']=0
predictedpop['1975']=0
predictedpop['1980']=0
predictedpop['1985']=0
predictedpop['1990']=0
predictedpop=predictedpop.sort(columns=None,axis=1,ascending=True,inplace=False)
pg.plotPopulationPrediction(tptot,predictedpop,sorted(yKeys,reverse=True))


#########################################################
#Ploting line chart for top ten cities
ccp = tpd.getCityCenterPopulationsByYears(data, ['All'], yKeys)
pg.plotHorizontalBarTopFive(ccp, yKeys)
pg.plotLineChartTopTen(ccp, yKeys)
##########################################################

##########################################################
#Ploting line chart for top ten rural area
ccpr = tpd.getVillagePopulationsByYears(data, ['All'], yKeys)
pg.plotLineChartTopTenRural(ccpr, yKeys)
##########################################################

###########################################################
#Ploting pyramid chart male vs female for every region according to cities
regions = f.find_file_names('cityRegions', '*.txt')
cityRegion = f.getRegionFiles(regions)
cpm = tpd.getCityPopulationsByYearsInMale(data, ['All'], yKeys)
cpf = tpd.getCityPopulationsByYearsInFemale(data, ['All'], yKeys)
pg.plotPyramidChart(cpm, cpf, yKeys, cityRegion)
############################################################

###########################################################
#Ploting pyramid chart male vs female for every region
regions = f.find_file_names('cityRegions', '*.txt')
cityRegion = f.getRegionFiles(regions)
cpm = tpd.getCityPopulationsByYearsInMale(data, ['All'], yKeys)
cpf = tpd.getCityPopulationsByYearsInFemale(data, ['All'], yKeys)
pg.plotRegionOverTotalPopulationInYears(cpm, cpf, yKeys, cityRegion)
############################################################
