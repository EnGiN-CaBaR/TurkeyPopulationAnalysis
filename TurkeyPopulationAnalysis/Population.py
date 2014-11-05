import pandas as pd

def readData(file_Name):
    data = pd.read_excel(file_Name, 'fixhtjNY')
    print data.dropna().head(80)
    pass 


if __name__ == "__main__":
    readData('1965.xlsx')
    