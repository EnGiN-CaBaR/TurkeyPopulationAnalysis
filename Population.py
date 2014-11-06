'''
Created on Nov 4, 2014

@author: engin
'''

from fileUtil import *

if __name__ == "__main__":
    fs = find_file_names('years', '*.xlsx')
    data = get_names_data(fs, 'xlsx')
    
    print data['1965']
    print data['1970']
        