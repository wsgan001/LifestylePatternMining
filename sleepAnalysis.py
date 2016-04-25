# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:19:50 2016

@author: wu34
"""


import artificialDataGenerator
import numpy as np
import pandas as pd 
import copy

def originalData():
    df,cols = artificialDataGenerator.originalData() 
    
    dd = {}
    dd_low = {}
    dd_high = {}
    for i in df.columns:
        dd[i] = [0,0,0] 
        temp = df[df[i]>0]
    #    dd[i][0] = temp[temp['label']==0].shape[0] 
    #    dd[i][1] = temp[temp['label']==1].shape[0]
    #    dd[i][2] = temp[temp['label']==2].shape[0]
        dd[i][0] = sum(temp[temp['label']==0][i])
        dd[i][1] = sum(temp[temp['label']==1][i])
        dd[i][2] = sum(temp[temp['label']==2][i])
        ll = copy.deepcopy(dd)
        dd[i][0] = dd[i][0]/float(sum(ll[i]))
        dd[i][1] = dd[i][1]/float(sum(ll[i]))
        dd[i][2] = dd[i][2]/float(sum(ll[i]))
        dd_low[i] = dd[i][0] + dd[i][1]
        dd_high[i] = dd[i][1] + dd[i][2]
        
    temp = df[df['workStudy']>0]
    print temp[temp['label']==2].shape
    
    return dd_low,dd_high

def artificialData():
    df,cols = artificialDataGenerator.artificialData()
    print df.columns 
    
    dd = {}
    dd_low = {}
    dd_high = {}
    for i in df.columns:
        dd[i] = [0,0,0] 
        temp = df[df[i]>0]
    #    dd[i][0] = temp[temp['label']==0].shape[0] 
    #    dd[i][1] = temp[temp['label']==1].shape[0]
    #    dd[i][2] = temp[temp['label']==2].shape[0]
        dd[i][0] = sum(temp[temp['label']==0][i])
        dd[i][1] = sum(temp[temp['label']==1][i])
        dd[i][2] = sum(temp[temp['label']==2][i])
        ll = copy.deepcopy(dd)
        dd[i][0] = dd[i][0]/float(sum(ll[i]))
        dd[i][1] = dd[i][1]/float(sum(ll[i]))
        dd[i][2] = dd[i][2]/float(sum(ll[i]))
        dd_low[i] = dd[i][0] + dd[i][1]
        dd_high[i] = dd[i][1] + dd[i][2]
        
    temp = df[df['workStudy']>0]
    print temp[temp['label']==2].shape
    
    return dd_low,dd_high

dd_low,dd_high = artificialData()
