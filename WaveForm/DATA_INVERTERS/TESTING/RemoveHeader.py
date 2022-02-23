# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 10:37:56 2017

@author: jherna4
"""

# REMOVE HEADER FROM CSV AND ADDS ANGLE AND VA COLUMNS

import csv, os
import re
import numpy as np

power10 = re.compile(r'power=0.1')
power20 = re.compile(r'power=0.2')
power30 = re.compile(r'power=0.3')
power40 = re.compile(r'power=0.4')
power50 = re.compile(r'power=0.5')
power60 = re.compile(r'power=0.6')
power70 = re.compile(r'power=0.7')
power80 = re.compile(r'power=0.8')
power90 = re.compile(r'power=0.9')
power100 = re.compile(r'power=1.0')
power110 = re.compile(r'power=1.1')

os.chdir('C:\\DATA_INVERTERS\\TESTING')
os.makedirs('headerRemoved', exist_ok=True)

#Loop through every file in the current working directory to change its name
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue
    mo10 = power10.search(csvFilename)
    mo20 = power20.search(csvFilename)
    mo30 = power30.search(csvFilename)
    mo40 = power40.search(csvFilename)
    mo50 = power50.search(csvFilename)
    mo60 = power60.search(csvFilename)
    mo70 = power70.search(csvFilename)
    mo80 = power80.search(csvFilename)
    mo90 = power90.search(csvFilename)
    mo100 = power100.search(csvFilename)
    mo110 = power110.search(csvFilename)
    if mo10 != None :
        os.rename(csvFilename, 'POW10.csv')
    elif mo20 != None :
        os.rename(csvFilename, 'POW20.csv')
    elif mo30 != None :
        os.rename(csvFilename, 'POW30.csv')
    elif mo40 != None :
        os.rename(csvFilename, 'POW40.csv')
    elif mo50 != None :
        os.rename(csvFilename, 'POW50.csv')
    elif mo60 != None :
        os.rename(csvFilename, 'POW60.csv')
    elif mo70 != None :
        os.rename(csvFilename, 'POW70.csv')
    elif mo80 != None :
        os.rename(csvFilename, 'POW80.csv')
    elif mo90 != None :
        os.rename(csvFilename, 'POW90.csv')
    elif mo100 != None :
        os.rename(csvFilename, 'POW100.csv')
    elif mo110 != None :
        os.rename(csvFilename, 'POW110.csv')
        
#Loop through every file in the current working directory to remove first row and add up angle and VA columns
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue
    print('Removing header from ' + csvFilename + '...')
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRows.append(row+[0]+[0])
    csvFileObj.close()
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    a = len(csvRows)
    for k in range(len(csvRows)):
        vas = float(csvRows[k][4])
        watts = float(csvRows[k][6])
        ANG = np.arctan(vas/watts)
        VA = np.sqrt(np.square(vas)+np.square(watts))
        csvRows[k][8] = str(ANG)
        csvRows[k][9] = str(VA)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
                        
        
        

        
        
    