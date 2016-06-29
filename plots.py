import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


inputFiles = [
    'ssvep20Hz0306A.csv'
    ]
    

def readCSV(filename):
    dataFrame = pd.read_csv(filename)
    return dataFrame
    
    
def main():
    dataFrame = readCSV(inputFiles[0])
    print(dataFrame)
    return 0
