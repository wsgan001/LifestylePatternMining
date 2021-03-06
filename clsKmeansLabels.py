# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 11:10:18 2016

@author: wu34
"""
import xlwt
import matplotlib.pyplot as plt
import numpy as np
import utilise
import dataGen4DietAct
import validation4DC

# Domain = ['ActItem','DietItem','DietType','ActType','ActDietItem','ActDietType']
Domain = ['DietType','ActType']

def bestLabel(labelsDietType,labelsActType):

    workbookW = xlwt.Workbook()
    ws = workbookW.add_sheet('sheet1')
    rowW = 0

    for domain in Domain:
        if domain == 'DietType':
            labels = utilise.string2array(labelsDietType) 
            row_labels = utilise.itemDict2list(dataGen4DietAct.genDietTypeDict())
            X = dataGen4DietAct.genDietTypeTFArray()
        elif domain == 'ActType':
            labels = utilise.string2array(labelsActType)
            row_labels = utilise.itemDict2list(dataGen4DietAct.genActTypeDict())
            X = dataGen4DietAct.genActTypeTFArray()
        X = utilise.normArray(X)
        
        
        # write the lables to excel file  
        col = 0
        for label in row_labels:
            ws.write(rowW,col,label)
            col += 1 
        rowW += 1 
        
        # print type(labels)
        plt.figure()
        
        n_clusters = np.max(labels) + 1 
        
        for k in range(n_clusters):
            class_members = labels == k
            i = 0
            sumVec = np.zeros(X.shape[1])
            for x in X[class_members]:
                i += 1
                sumVec += x 
            meanVec = sumVec/i 
            meanVec.tolist()
            
            # write the mean vector of each group to excel file 
            col = 0
            for value in meanVec:
                ws.write(rowW,col,value)
                col += 1 
            rowW += 1 
            # print meanVec 
            
            # we don't have to do normalization here, as the input X has already been normalized 
            # totalSum = np.sum(meanVec[0])
            # print totalSum
            # meanVec = meanVec/totalSum
            
            # # normalize the meanVec 
            # firstMax = np.max(meanVec)
            # meanVec = meanVec/firstMax
            
            firstMax = np.max(meanVec)
            # print firstMax
            tempVec = np.copy(meanVec)
            for j in range(X.shape[1]):
                if tempVec[j] == firstMax:
                    tempVec[j] = 0
            secondMax = np.max(tempVec)
            # print secondMax
            tempVec2 = np.copy(tempVec)
            for j in range(X.shape[1]):
                if tempVec2[j]==secondMax:
                    tempVec2[j] = 0
            thirdMax = np.max(tempVec2)
            # print thirdMax

            
            x = range(X.shape[1])
            plt.plot(x,meanVec)
            # print meanVec
            for j in range(X.shape[1]):
                # if meanVec[j] == firstMax:
                # if meanVec[j] == firstMax or meanVec[j] == secondMax:
                if meanVec[j] == firstMax or meanVec[j] == secondMax or meanVec[j] == thirdMax:
                    print k,domain,n_clusters,meanVec[j],row_labels[j]
                    plt.text(x[j],meanVec[j],row_labels[j])

        # print row_labels
        # plt.xlabel(row_labels)
        plt.title(domain+'_TF_KMeans_'+str(n_clusters))
        plt.savefig('visClustering'+domain+'Pattern/KMeans__TF_'+str(n_clusters)+'_groupFreq')
    
    workbookW.save('tempLabels.xls')

def bestLabel4DC(labelsDietType,labelsActType):

    workbookW = xlwt.Workbook()
    ws = workbookW.add_sheet('sheet1')
    rowW = 0

    for domain in Domain:
        if domain == 'DietType':
            labels = utilise.string2array(labelsDietType)
            X = validation4DC.getDietTypeTFArray4DC()
            row_labels = utilise.itemDict2list(dataGen4DietAct.genDietTypeDict())
        elif domain == 'ActType':
            labels = utilise.string2array(labelsActType)
            X = validation4DC.getActTypeTFArray4DC()
            row_labels = utilise.itemDict2list(dataGen4DietAct.genActTypeDict())
        X = utilise.normArray(X)
        
        # write the lables to excel file  
        col = 0
        for label in row_labels:
            ws.write(rowW,col,label)
            col += 1 
        rowW += 1 
        
        # print type(labels)
        plt.figure()
        
        n_clusters = np.max(labels) + 1
        
        for k in range(n_clusters):
            class_members = labels == k
            i = 0
            sumVec = np.zeros(X.shape[1])
            for x in X[class_members]:
                i += 1
                sumVec += x 
            meanVec = sumVec/i 
            meanVec.tolist()
            
            # write the mean vector of each group to excel file 
            col = 0
            for value in meanVec:
                ws.write(rowW,col,value)
                col += 1 
            rowW += 1 
            # print meanVec 
            
            # we don't have to do normalization here, as the input X has already been normalized 
            # totalSum = np.sum(meanVec[0])
            # print totalSum
            # meanVec = meanVec/totalSum
            
            # # normalize the meanVec 
            # firstMax = np.max(meanVec)
            # meanVec = meanVec/firstMax
            
            firstMax = np.max(meanVec)
            # print firstMax
            tempVec = np.copy(meanVec)
            for j in range(X.shape[1]):
                if tempVec[j] == firstMax:
                    tempVec[j] = 0
            secondMax = np.max(tempVec)
            # print secondMax
            tempVec2 = np.copy(tempVec)
            for j in range(X.shape[1]):
                if tempVec2[j]==secondMax:
                    tempVec2[j] = 0
            thirdMax = np.max(tempVec2)
            # print thirdMax

            
            x = range(X.shape[1])
            plt.plot(x,meanVec)
            # print meanVec
            for j in range(X.shape[1]):
                # if meanVec[j] == firstMax:
                # if meanVec[j] == firstMax or meanVec[j] == secondMax:
                if meanVec[j] == firstMax or meanVec[j] == secondMax or meanVec[j] == thirdMax:
                    ws.write(rowW,0,k)
                    ws.write(rowW,1,domain)
                    ws.write(rowW,2,row_labels[j])
                    ws.write(rowW,3,meanVec[j])
                    rowW += 1 
                    print k,domain,n_clusters,meanVec[j],row_labels[j]
                plt.text(x[j],meanVec[j],row_labels[j])

        # print row_labels
        # plt.xlabel(row_labels)
        plt.title(domain+'_TF_KMeans_'+str(n_clusters))
        plt.savefig('visClustering'+domain+'Pattern/KMeans__TF_'+str(n_clusters)+'_groupFreq')
    
    workbookW.save('tempLabels.xls')

# def clusteringKmeansLabels():
    # for domain in Domain:
        # for n_clusters in range(4,5):
            # for metric in Metric:
                # bestLabel(domain,metric,n_clusters)

#def clusteringKmeansLabels():
#   for n_clusters in range(2,3):
#       bestLabel('TF',n_clusters)

def clusteringKmeansLabels():
    labelsDietType = '1 1 0 1 1 1 0 0 0 0 0 1 0 0 0 0 1 0 0 1 0 0 0 0 1 0 1 1 1'
    labelsActType = '1 0 1 1 0 0 2 2 2 1 2 0 1 2 1 2 0 1 1 2 0 1 1 2 1 1 0 2 1'
    bestLabel4DC(labelsDietType,labelsActType)

# bestLabel('DietItem',4)
clusteringKmeansLabels()
