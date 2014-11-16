'''
Created on Nov 4, 2014

@author: engin
'''
# coding=utf-8

from fileUtil import *
from pandas.core.frame import DataFrame
import pandas as pd
from turkeyPopulationData import *
import numpy as np
import matplotlib.pyplot as plt
import population_graph as pg
from flask import Flask
from flask import request
import json
from flask.templating import render_template
from flask.json import jsonify

app = Flask(__name__)


fs = find_file_names('years', '*.xlsx')
data = get_names_data(fs, 'xlsx')
yKeys = data.keys()
tm = getCityCenterPopulationsByYears(data, ['All'], yKeys)
plate = getPlate()

@app.route('/turkey_population', methods=['GET', 'POST'])
def jsonExample():
    if request.method == 'GET':
        return render_template('hello.html')
    else:
        f1 = request.args.get('Year', '')
        return tm[f1].to_json()

if __name__ == "__main__":
    
    app.run(host='0.0.0.0', debug=True)
    
    
