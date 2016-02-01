# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 13:25:44 2016

@author: wu34
"""

import xlrd
import utilise
available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']

def diaryDurationList():
	durationList = []
	for subjectID in available_list:
		durationList.append(getDuration(subjectID))
	return durationList
	

def getDuration(subjectID):
	file_location = 'subject_template_'+subjectID+'.xlsx'
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(3)
	duration = 0 
	for row in range(8,sheet.nrows):
		if sheet.cell_value(row,0):
			duration += 1 
	return duration 

def getStartEndTime(subjectID):
	file_location = 'subject_template_'+subjectID+'.xlsx'
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(3)
	startDate = sheet.cell_value(8,0)
	for row in range(8,sheet.nrows):
		if sheet.cell_value(row,0):
			endDate = sheet.cell_value(row,0)
	return startDate, endDate

def getTimeDict(subjectID):
	timeDict = {}
	startDate,endDate = getStartEndTime(subjectID)
	timeDict['startDate'] = startDate
	timeDict['endDate'] = endDate
	timeDict['duration'] = getDuration(subjectID)
	return timeDict 
	
def diaryTimeDict():
	totalTimeDict = {}
	for i in range(len(available_list)):
		totalTimeDict[i] = getTimeDict(available_list[i])
	return totalTimeDict

# print diaryTimeDict()
# tf = utilise.genActItemTFArray()
# print tf.shape
# tf = utilise.genDietItemTFArray()
# print tf.shape