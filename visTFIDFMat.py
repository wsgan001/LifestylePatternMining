# -*- coding: utf-8 -*-
"""
Created on Fri Jan 08 15:29:13 2016

@author: wu34
"""

import utilise
import dataGen4DietAct
import matplotlib.pyplot as plt

def visTFIDFMatrix():
	tfidf1 = utilise.normArray(dataGen4DietAct.ActItemTfidfArray())
	# tfidf1 = dataGen4DietAct.ActItemTfidfArray()
	plt.figure()
	plt.matshow(tfidf1)
	plt.colorbar()
	plt.title('actTFIDFMatrix')
	plt.savefig('visTForTFIDFMatrix/actTFIDFMatrix')
	
	tfidf2 = utilise.normArray(dataGen4DietAct.DietItemTfidfArray())
	# tfidf2 = dataGen4DietAct.DietItemTfidfArray()
	plt.figure()
	plt.matshow(tfidf2)
	plt.colorbar()
	plt.title('dietTFIDFMatrix')
	plt.savefig('visTForTFIDFMatrix/dietTFIDFMatrix')
	
	tfidf = utilise.genCombiArray(tfidf1,tfidf2)
	plt.figure()
	plt.matshow(tfidf)
	plt.colorbar()
	plt.title('actDietTFIDFMatrix')
	plt.savefig('visTForTFIDFMatrix/actDietTFIDFMatrix')
	
	tfidf2 = utilise.normArray(dataGen4DietAct.DietTypeTfidfArray())
	# tfidf2 = dataGen4DietAct.DietTypeTfidfArray()
	plt.figure()
	plt.matshow(tfidf2)
	plt.colorbar()
	plt.title('dietTypeTFIDFMatrix')
	plt.savefig('visTForTFIDFMatrix/dietTypeTFIDFMatrix')
	
	tfidf1 = utilise.normArray(dataGen4DietAct.ActTypeTfidfArray())
	# tfidf1 = dataGen4DietAct.ActTypeTfidfArray()
	plt.figure()
	plt.matshow(tfidf1)
	plt.colorbar()
	plt.title('actTypeTFIDFMatrix')
	plt.savefig('visTForTFIDFMatrix/actTypeTFIDFMatrix')
	
	tfidf = utilise.genCombiArray(tfidf1,tfidf2)
	plt.figure()
	plt.matshow(tfidf)
	plt.colorbar()
	plt.title('actDietTypeTFIDFMatrix')
	plt.savefig('visTForTFIDFMatrix/actDietTypeTFIDFMatrix')

# visTFIDFMatrix()
