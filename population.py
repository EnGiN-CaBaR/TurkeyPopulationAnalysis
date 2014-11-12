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


@app.route('/turkey_population')
def jsonExample():
    exampleDic = {'a' : [1, 2, 3], 'b' : [5, 6, 7]}
    a = json.dumps(exampleDic)
    return str(a)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    
    fs = find_file_names('years', '*.xlsx')
    data = get_names_data(fs, 'xlsx')
    yKeys = data.keys()
    tm = getTurkeyPopulationsByYears(data, yKeys)
