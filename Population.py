'''
Created on Nov 4, 2014

@author: engin
'''

from fileUtil import *

if __name__ == "__main__":
    fs = find_file_names('years', '*.xls')
    for f in fs:
        data = get_names_data(f, 'xls')
        print data