from __future__ import print_function
import csv
import random
import math
import pprint
import datetime
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='sonu1995', db='knearest', autocommit=True)
cur = conn.cursor()

pp = pprint.PrettyPrinter(indent=4)
f = open('myfile','w')


trainingSet=[]
testSet=[]
mycsv = csv.reader(open("/home/bhavya/Downloads/CAX_Data_Aging.csv"))
mycsv = list(mycsv)
maxVal = []

def loadDataset():
	print("Load Data Set Started !")
	rowCount = 1
	colCount = 4
	while (colCount < 269):
		max1 = 0
		rowCount = 1
		while (rowCount <= 12958):
			try:
				if (float(mycsv[rowCount][colCount]) > max1):
					max1 = float(mycsv[rowCount][colCount])
			except:
 				pass
			rowCount += 1
		maxVal.append(max1) #claculating max for each col
		colCount += 1
	print ("Got max for all columns")
	print(maxVal)
	counter = 1
	#segregating into test and training data
	while (counter <= 12958):
		try:
			data = int(mycsv[counter][1])
			trainingSet.append(counter)
		except:
			if(counter >= 0):
				testSet.append(counter)
		counter += 1
	print ("Load Data Set Completed !")

def euclideanDistanceExceptBigColumns(instance1, instance2, length):
	# print ("in euclideanDistanceExceptBigColumns")
	distance = 0
	counter = 0
	for x in range(length):
		if (counter < 4 or counter == 43 or counter == 47):
			counter += 1
			continue
		try:
			distance += pow(((float(instance1[x]) - float(instance2[x])) / maxVal[counter -4]), 2)
		except:
			pass
		counter += 1
	# print ("out euclideanDistanceExceptBigColumns")

	return math.sqrt(distance)

def euclideanDistanceAllColumns(instance1, instance2, length):
	# print ("in euclideanDistanceAllColumns")
	distance = 0
	counter = 0
	for x in range(length):
		if (counter < 4):
			counter += 1
			continue
		try:
			distance += pow(((float(instance1[x]) - float(instance2[x])) / maxVal[counter -4]), 2)
		except:
			pass
		counter += 1
	# print ("out euclideanDistanceAllColumns")
	return math.sqrt(distance)

def euclideanDistanceOnlyBigColumns(instance1, instance2, length):
	# print ("in euclideanDistanceOnlyBigColumns")
	distance = 0
	counter = 0
	for x in range(length):
		if (counter != 43 and counter != 47):
			counter += 1
			continue
		try:
			distance += pow(((float(instance1[x]) - float(instance2[x])) / maxVal[counter -4]), 2)
		except:
			pass
		counter += 1
	# print ("in euclideanDistanceOnlyBigColumns")
	return math.sqrt(distance)

def calculateAllColumns(testSetParam, trainingSetParam):
	distanceArr = []
	predictDisease = -1
	for x in testSetParam:

		temp = {
			'x': x,
			'distance': []
		}
		for y in trainingSetParam :
			distance = euclideanDistanceAllColumns(mycsv[int(x)], mycsv[int(y)], 265)
			#distance = euclideanDistanceExceptBigColumns(mycsv[int(x)], mycsv[int(y)], 265)
			# distance = euclideanDistanceOnlyBigColumns(mycsv[int(x)], mycsv[int(y)], 265)
			temp1 = {
				'distanceBw': distance,
				'y': y
			}
			temp['distance'].append(temp1)
		distanceArr.append(temp)
		cc = temp['distance']
		cc.sort(key=lambda x: x['distanceBw'], reverse=True)
		kmin = []
		counterMin = 1
		while(counterMin < 9):
			kmin.append(temp['distance'][counterMin])
			counterMin += 1
		print({'x': temp['x'], 'kmin': kmin})

		getKNearest = {'x': temp['x'], 'kmin': kmin}
		# predict disease of test data based on k nearest data
		disease = {}

		for k in getKNearest['kmin']:
			y = k['y']
			ar = mycsv[y][1]
			an = mycsv[y][2]
			cl = mycsv[y][3]
			#print(ar, an, cl)
			try:
				if (int(ar) == 0 and int(an) == 0 and int(cl) == 0):
					try:
						disease[0] += 1
					except:
						disease[0] = 1
				elif (int(ar) == 0 and int(an) == 0 and int(cl) == 1):
					try:
						disease[1] += 1
					except:
						disease[1] = 1
				elif (int(ar) == 0 and int(an) == 1 and int(cl) == 0):
					try:
						disease[2] += 1
					except:
						disease[2] = 1
				elif (int(ar) == 0 and int(an) == 1 and int(cl) == 1):
					try:
						disease[3] += 1
					except:
						disease[3] = 1
				elif (int(ar) == 1 and int(an) == 0 and int(cl) == 0):
					try:
						disease[4] += 1
					except:
						disease[4] = 1
				elif (int(ar) == 1 and int(an) == 0 and int(cl) == 1):
					try:
						disease[5] += 1
					except:
						disease[5] = 1
				elif (int(ar) == 1 and int(an) == 1 and int(cl) == 0):
					try:
						disease[6] += 1
					except:
						disease[6] = 1
				elif (int(ar) == 1 and int(an) == 1 and int(cl) == 1):
					try:
						disease[7] += 1
					except:
						disease[7] = 1
			except:
				pass
		diseaseCount = 0
		sumTotal = 0
		maxCount = 0
		predictDisease = -1
		print(disease)
		while (diseaseCount < 8):
			try:
				sumTotal += disease[diseaseCount]
				if (disease[diseaseCount] > maxCount):
					maxCount = disease[diseaseCount]
					predictDisease = diseaseCount
			except:
				pass
			diseaseCount += 1
		print(predictDisease)






	# for z in distanceArr:
	# 	cc = z['distance']
	# 	cc.sort(key=lambda x: x['distanceBw'], reverse=True)
	# 	kmin = []
	# 	counterMin = 1
	# 	while(counterMin < 9):
	# 		kmin.append(z['distance'][counterMin])
	# 		counterMin += 1
	# 	print({'x': z['x'], 'kmin': kmin})
	# 	getKNearest = {'x': z['x'], 'kmin': kmin}
	# 	# predict disease of test data based on k nearest data
	# 	disease = {}

	# 	for k in getKNearest['kmin']:
	# 		y = k['y']
	# 		ar = mycsv[y][1]
	# 		an = mycsv[y][2]
	# 		cl = mycsv[y][3]
	# 		#print(ar, an, cl)
	# 		if (int(ar) == 0 and int(an) == 0 and int(cl) == 0):
	# 			try:
	# 				disease[0] += 1
	# 			except:
	# 				disease[0] = 1
	# 		elif (int(ar) == 0 and int(an) == 0 and int(cl) == 1):
	# 			try:
	# 				disease[1] += 1
	# 			except:
	# 				disease[1] = 1
	# 		elif (int(ar) == 0 and int(an) == 1 and int(cl) == 0):
	# 			try:
	# 				disease[2] += 1
	# 			except:
	# 				disease[2] = 1
	# 		elif (int(ar) == 0 and int(an) == 1 and int(cl) == 1):
	# 			try:
	# 				disease[3] += 1
	# 			except:
	# 				disease[3] = 1
	# 		elif (int(ar) == 1 and int(an) == 0 and int(cl) == 0):
	# 			try:
	# 				disease[4] += 1
	# 			except:
	# 				disease[4] = 1
	# 		elif (int(ar) == 1 and int(an) == 0 and int(cl) == 1):
	# 			try:
	# 				disease[5] += 1
	# 			except:
	# 				disease[5] = 1
	# 		elif (int(ar) == 1 and int(an) == 1 and int(cl) == 0):
	# 			try:
	# 				disease[6] += 1
	# 			except:
	# 				disease[6] = 1
	# 		elif (int(ar) == 1 and int(an) == 1 and int(cl) == 1):
	# 			try:
	# 				disease[7] += 1
	# 			except:
	# 				disease[7] = 1
	# 	diseaseCount = 0
	# 	sumTotal = 0
	# 	maxCount = 0
	# 	predictDisease = -1
	# 	print(disease)
	# 	while (diseaseCount < 8):
	# 		try:
	# 			sumTotal += disease[diseaseCount]
	# 			if (disease[diseaseCount] > maxCount):
	# 				maxCount = disease[diseaseCount]
	# 				predictDisease = diseaseCount
	# 		except:
	# 			pass
	# 		diseaseCount += 1
	# 	print(predictDisease)
	return predictDisease


def calculateExceptBigColumns(testSetParam, trainingSetParam):
	distanceArr = []
	predictDisease = -1
	for x in testSetParam:
		temp = {
			'x': x,
			'distance': []
		}
		for y in trainingSetParam :
			# distance = euclideanDistanceAllColumns(mycsv[int(x)], mycsv[int(y)], 265)
			distance = euclideanDistanceExceptBigColumns(mycsv[int(x)], mycsv[int(y)], 265)
			# distance = euclideanDistanceOnlyBigColumns(mycsv[int(x)], mycsv[int(y)], 265)
			temp1 = {
				'distanceBw': distance,
				'y': y
			}
			temp['distance'].append(temp1)

		cc = temp['distance']
		cc.sort(key=lambda x: x['distanceBw'], reverse=True)
		kmin = []
		counterMin = 1
		while(counterMin < 9):
			kmin.append(temp['distance'][counterMin])
			counterMin += 1
		print({'x': temp['x'], 'kmin': kmin})
		getKNearest = {'x': temp['x'], 'kmin': kmin}
		# predict disease of test data based on k nearest data
		disease = {}

		for k in getKNearest['kmin']:
			y = k['y']
			ar = mycsv[y][1]
			an = mycsv[y][2]
			cl = mycsv[y][3]
			#print(ar, an, cl)
			try:
				if (int(ar) == 0 and int(an) == 0 and int(cl) == 0):
					try:
						disease[0] += 1
					except:
						disease[0] = 1
				elif (int(ar) == 0 and int(an) == 0 and int(cl) == 1):
					try:
						disease[1] += 1
					except:
						disease[1] = 1
				elif (int(ar) == 0 and int(an) == 1 and int(cl) == 0):
					try:
						disease[2] += 1
					except:
						disease[2] = 1
				elif (int(ar) == 0 and int(an) == 1 and int(cl) == 1):
					try:
						disease[3] += 1
					except:
						disease[3] = 1
				elif (int(ar) == 1 and int(an) == 0 and int(cl) == 0):
					try:
						disease[4] += 1
					except:
						disease[4] = 1
				elif (int(ar) == 1 and int(an) == 0 and int(cl) == 1):
					try:
						disease[5] += 1
					except:
						disease[5] = 1
				elif (int(ar) == 1 and int(an) == 1 and int(cl) == 0):
					try:
						disease[6] += 1
					except:
						disease[6] = 1
				elif (int(ar) == 1 and int(an) == 1 and int(cl) == 1):
					try:
						disease[7] += 1
					except:
						disease[7] = 1
			except:
				pass
		diseaseCount = 0
		sumTotal = 0
		maxCount = 0
		predictDisease = -1
		print(disease)
		while (diseaseCount < 8):
			try:
				sumTotal += disease[diseaseCount]
				if (disease[diseaseCount] > maxCount):
					maxCount = disease[diseaseCount]
					predictDisease = diseaseCount
			except:
				pass
			diseaseCount += 1
		print(predictDisease)

		# distanceArr.append(temp)

	# for z in distanceArr:
		# cc = z['distance']
		# cc.sort(key=lambda x: x['distanceBw'], reverse=True)
		# kmin = []
		# counterMin = 1
		# while(counterMin < 9):
		# 	kmin.append(z['distance'][counterMin])
		# 	counterMin += 1
		# print({'x': z['x'], 'kmin': kmin})
		# getKNearest = {'x': z['x'], 'kmin': kmin}
		# # predict disease of test data based on k nearest data
		# disease = {}

		# for k in getKNearest['kmin']:
		# 	y = k['y']
		# 	ar = mycsv[y][1]
		# 	an = mycsv[y][2]
		# 	cl = mycsv[y][3]
		# 	#print(ar, an, cl)
		# 	if (int(ar) == 0 and int(an) == 0 and int(cl) == 0):
		# 		try:
		# 			disease[0] += 1
		# 		except:
		# 			disease[0] = 1
		# 	elif (int(ar) == 0 and int(an) == 0 and int(cl) == 1):
		# 		try:
		# 			disease[1] += 1
		# 		except:
		# 			disease[1] = 1
		# 	elif (int(ar) == 0 and int(an) == 1 and int(cl) == 0):
		# 		try:
		# 			disease[2] += 1
		# 		except:
		# 			disease[2] = 1
		# 	elif (int(ar) == 0 and int(an) == 1 and int(cl) == 1):
		# 		try:
		# 			disease[3] += 1
		# 		except:
		# 			disease[3] = 1
		# 	elif (int(ar) == 1 and int(an) == 0 and int(cl) == 0):
		# 		try:
		# 			disease[4] += 1
		# 		except:
		# 			disease[4] = 1
		# 	elif (int(ar) == 1 and int(an) == 0 and int(cl) == 1):
		# 		try:
		# 			disease[5] += 1
		# 		except:
		# 			disease[5] = 1
		# 	elif (int(ar) == 1 and int(an) == 1 and int(cl) == 0):
		# 		try:
		# 			disease[6] += 1
		# 		except:
		# 			disease[6] = 1
		# 	elif (int(ar) == 1 and int(an) == 1 and int(cl) == 1):
		# 		try:
		# 			disease[7] += 1
		# 		except:
		# 			disease[7] = 1
		# diseaseCount = 0
		# sumTotal = 0
		# maxCount = 0
		# predictDisease = -1
		# print(disease)
		# while (diseaseCount < 8):
		# 	try:
		# 		sumTotal += disease[diseaseCount]
		# 		if (disease[diseaseCount] > maxCount):
		# 			maxCount = disease[diseaseCount]
		# 			predictDisease = diseaseCount
		# 	except:
		# 		pass
		# 	diseaseCount += 1
		# print(predictDisease)
	return predictDisease


def calculateOnlyBigColumns(testSetParam, trainingSetParam):
	distanceArr = []
	predictDisease = -1
	for x in testSetParam:
		temp = {
			'x': x,
			'distance': []
		}
		for y in trainingSetParam :
			# distance = euclideanDistanceAllColumns(mycsv[int(x)], mycsv[int(y)], 265)
			#distance = euclideanDistanceExceptBigColumns(mycsv[int(x)], mycsv[int(y)], 265)
			distance = euclideanDistanceOnlyBigColumns(mycsv[int(x)], mycsv[int(y)], 265)
			temp1 = {
				'distanceBw': distance,
				'y': y
			}
			temp['distance'].append(temp1)
		cc = temp['distance']
		# pp.pprint(cc)
		cc.sort(key=lambda x: x['distanceBw'], reverse=True)
		kmin = []
		counterMin = 1
		while(counterMin < 9):
			kmin.append(temp['distance'][counterMin])
			counterMin += 1
		print({'x': temp['x'], 'kmin': kmin})
		getKNearest = {'x': temp['x'], 'kmin': kmin}
		# predict disease of test data based on k nearest data
		disease = {}

		for k in getKNearest['kmin']:
			y = k['y']
			#print(y)
			ar = mycsv[y][1]
			an = mycsv[y][2]
			cl = mycsv[y][3]
			#print(ar, an, cl)
			try:
				if (int(ar) == 0 and int(an) == 0 and int(cl) == 0):
					try:
						disease[0] += 1
					except:
						disease[0] = 1
				elif (int(ar) == 0 and int(an) == 0 and int(cl) == 1):
					try:
						disease[1] += 1
					except:
						disease[1] = 1
				elif (int(ar) == 0 and int(an) == 1 and int(cl) == 0):
					try:
						disease[2] += 1
					except:
						disease[2] = 1
				elif (int(ar) == 0 and int(an) == 1 and int(cl) == 1):
					try:
						disease[3] += 1
					except:
						disease[3] = 1
				elif (int(ar) == 1 and int(an) == 0 and int(cl) == 0):
					try:
						disease[4] += 1
					except:
						disease[4] = 1
				elif (int(ar) == 1 and int(an) == 0 and int(cl) == 1):
					try:
						disease[5] += 1
					except:
						disease[5] = 1
				elif (int(ar) == 1 and int(an) == 1 and int(cl) == 0):
					try:
						disease[6] += 1
					except:
						disease[6] = 1
				elif (int(ar) == 1 and int(an) == 1 and int(cl) == 1):
					try:
						disease[7] += 1
					except:
						disease[7] = 1
			except:
				pass
		diseaseCount = 0
		sumTotal = 0
		maxCount = 0
		predictDisease = -1
		print(disease)
		while (diseaseCount < 8):
			try:
				sumTotal += disease[diseaseCount]
				if (disease[diseaseCount] > maxCount):
					maxCount = disease[diseaseCount]
					predictDisease = diseaseCount
			except:
				pass
			diseaseCount += 1
		print(predictDisease)

		# distanceArr.append(temp)

	# pp.pprint(distanceArr)
	# for z in distanceArr:
		# cc = z['distance']
		# # pp.pprint(cc)
		# cc.sort(key=lambda x: x['distanceBw'], reverse=True)
		# kmin = []
		# counterMin = 1
		# while(counterMin < 9):
		# 	kmin.append(z['distance'][counterMin])
		# 	counterMin += 1
		# print({'x': z['x'], 'kmin': kmin})
		# getKNearest = {'x': z['x'], 'kmin': kmin}
		# # predict disease of test data based on k nearest data
		# disease = {}

		# for k in getKNearest['kmin']:
		# 	y = k['y']
		# 	#print(y)
		# 	ar = mycsv[y][1]
		# 	an = mycsv[y][2]
		# 	cl = mycsv[y][3]
		# 	#print(ar, an, cl)
		# 	if (int(ar) == 0 and int(an) == 0 and int(cl) == 0):
		# 		try:
		# 			disease[0] += 1
		# 		except:
		# 			disease[0] = 1
		# 	elif (int(ar) == 0 and int(an) == 0 and int(cl) == 1):
		# 		try:
		# 			disease[1] += 1
		# 		except:
		# 			disease[1] = 1
		# 	elif (int(ar) == 0 and int(an) == 1 and int(cl) == 0):
		# 		try:
		# 			disease[2] += 1
		# 		except:
		# 			disease[2] = 1
		# 	elif (int(ar) == 0 and int(an) == 1 and int(cl) == 1):
		# 		try:
		# 			disease[3] += 1
		# 		except:
		# 			disease[3] = 1
		# 	elif (int(ar) == 1 and int(an) == 0 and int(cl) == 0):
		# 		try:
		# 			disease[4] += 1
		# 		except:
		# 			disease[4] = 1
		# 	elif (int(ar) == 1 and int(an) == 0 and int(cl) == 1):
		# 		try:
		# 			disease[5] += 1
		# 		except:
		# 			disease[5] = 1
		# 	elif (int(ar) == 1 and int(an) == 1 and int(cl) == 0):
		# 		try:
		# 			disease[6] += 1
		# 		except:
		# 			disease[6] = 1
		# 	elif (int(ar) == 1 and int(an) == 1 and int(cl) == 1):
		# 		try:
		# 			disease[7] += 1
		# 		except:
		# 			disease[7] = 1
		# diseaseCount = 0
		# sumTotal = 0
		# maxCount = 0
		# predictDisease = -1
		# print(disease)
		# while (diseaseCount < 8):
		# 	try:
		# 		sumTotal += disease[diseaseCount]
		# 		if (disease[diseaseCount] > maxCount):
		# 			maxCount = disease[diseaseCount]
		# 			predictDisease = diseaseCount
		# 	except:
		# 		pass
		# 	diseaseCount += 1
		# print(predictDisease)
	return predictDisease



def findtotal():
	y = 1
	disease = {}
	while(y < 12000):
		ar = mycsv[y][1]
		an = mycsv[y][2]
		cl = mycsv[y][3]
		#print(ar, an, cl)
		try:
			if (int(ar) == 0 and int(an) == 0 and int(cl) == 0):
				try:
					disease[0] += 1
				except:
					disease[0] = 1
			elif (int(ar) == 0 and int(an) == 0 and int(cl) == 1):
				try:
					disease[1] += 1
				except:
					disease[1] = 1
			elif (int(ar) == 0 and int(an) == 1 and int(cl) == 0):
				try:
					disease[2] += 1
				except:
					disease[2] = 1
			elif (int(ar) == 0 and int(an) == 1 and int(cl) == 1):
				try:
					disease[3] += 1
				except:
					disease[3] = 1
			elif (int(ar) == 1 and int(an) == 0 and int(cl) == 0):
				try:
					disease[4] += 1
				except:
					disease[4] = 1
			elif (int(ar) == 1 and int(an) == 0 and int(cl) == 1):
				try:
					disease[5] += 1
				except:
					disease[5] = 1
			elif (int(ar) == 1 and int(an) == 1 and int(cl) == 0):
				try:
					disease[6] += 1
				except:
					disease[6] = 1
			elif (int(ar) == 1 and int(an) == 1 and int(cl) == 1):
				try:
					disease[7] += 1
				except:
					disease[7] = 1
		except:
			pass
		y += 1
	print(disease)

def accuracy(chosen, testSet1, trainingSet1):
	counter = 1
	#segregating into test and training data
	# print(testSet1, trainingSet1)
	while (counter <= 12958):
		try:
			data = int(mycsv[counter][1])
			if (counter == chosen):
				testSet1.append(counter)
			else:
				trainingSet1.append(counter)
		except:
			#testSet1.append(counter)
			pass
		counter += 1
		#print(testSet1, trainingSet1)

startTime = datetime.datetime.today()
loadDataset()
# findtotal()
# print("FOR ALL COLUMNS____________________________________________")
# for t in testSet:
# 	zz = []
# 	zz.append(t)
# 	predictDisease = calculateAllColumns(zz, trainingSet)
# 	cur.execute("INSERT INTO predictallcol VALUES (" + str(t) + "," + str(predictDisease) + ");")

# print("-----------------------------accuracy-------------------------------------")
# # counttrue = 0
# # counttotal = 0
# counttrue = 6194
# counttotal = 9291
# for chosen in trainingSet:
# 	if (chosen <= 11474):
# 		continue
# 	counttotal += 1
# 	testSet1 = []
# 	trainingSet1 = []
# 	accuracy(chosen, testSet1, trainingSet1)
# 	# print(testSet1, trainingSet1)
# 	predictDisease = calculateAllColumns(testSet1, trainingSet1)
# 	#print(predictDisease)
# 	mydisease=-1
# 	ar = mycsv[chosen][1]
# 	an = mycsv[chosen][2]
# 	cl = mycsv[chosen][3]
# 	try:
# 		if (int(ar) == 0 and int(an) == 0 and int(cl) == 0):
# 			mydisease=0
# 		elif (int(ar) == 0 and int(an) == 0 and int(cl) == 1):
# 			mydisease=1
# 		elif (int(ar) == 0 and int(an) == 1 and int(cl) == 0):
# 			mydisease=2
# 		elif (int(ar) == 0 and int(an) == 1 and int(cl) == 1):
# 			mydisease=3
# 		elif (int(ar) == 1 and int(an) == 0 and int(cl) == 0):
# 			mydisease=4
# 		elif (int(ar) == 1 and int(an) == 0 and int(cl) == 1):
# 			mydisease=5
# 		elif (int(ar) == 1 and int(an) == 1 and int(cl) == 0):
# 			mydisease=6
# 		elif (int(ar) == 1 and int(an) == 1 and int(cl) == 1):
# 			mydisease=7
# 		#print("Bimarii---->>>")
# 		# print(predictDisease, mydisease)
# 		if(predictDisease == mydisease):
# 			counttrue += 1
# 		cur.execute("INSERT INTO accuracyallcol VALUES (" + str(chosen) + "," + str(predictDisease) + "," + str(mydisease) + "," + str(counttrue)+ "," + str(counttotal) + ");")
# 	except:
# 		pass
# 	# chosen += 1
# print(counttrue, counttotal)
# percentage = (counttrue * 100)/counttotal
# print(percentage)



print("FOR EXCEPT BIG COLUMNS____________________________________________")
for t in testSet:
	zz = []
	zz.append(t)
	predictDisease = calculateExceptBigColumns(zz, trainingSet)
	cur.execute("INSERT INTO predictexceptbig VALUES (" + str(t) + "," + str(predictDisease) + ");")
	print(cur)

print("-----------------------------accuracy-------------------------------------")
counttrue = 0
counttotal = 0
for chosen in trainingSet:
	counttotal += 1
	testSet1 = []
	trainingSet1 = []
	accuracy(chosen, testSet1, trainingSet1)
	# print(testSet1, trainingSet1)
	predictDisease = calculateExceptBigColumns(testSet1, trainingSet1)
	#print(predictDisease)
	mydisease=-1
	ar = mycsv[chosen][1]
	an = mycsv[chosen][2]
	cl = mycsv[chosen][3]
	try:
		if (int(ar) == 0 and int(an) == 0 and int(cl) == 0):
			mydisease=0
		elif (int(ar) == 0 and int(an) == 0 and int(cl) == 1):
			mydisease=1
		elif (int(ar) == 0 and int(an) == 1 and int(cl) == 0):
			mydisease=2
		elif (int(ar) == 0 and int(an) == 1 and int(cl) == 1):
			mydisease=3
		elif (int(ar) == 1 and int(an) == 0 and int(cl) == 0):
			mydisease=4
		elif (int(ar) == 1 and int(an) == 0 and int(cl) == 1):
			mydisease=5
		elif (int(ar) == 1 and int(an) == 1 and int(cl) == 0):
			mydisease=6
		elif (int(ar) == 1 and int(an) == 1 and int(cl) == 1):
			mydisease=7
		#print("Bimarii---->>>")
		# print(predictDisease, mydisease)
		if(predictDisease == mydisease):
			counttrue += 1
		cur.execute("INSERT INTO accuracyexceptbig VALUES (" + str(chosen) + "," + str(predictDisease) + "," + str(mydisease) + "," + str(counttrue)+ "," + str(counttotal) + ");")
	except:
		pass
	# chosen += 1
print(counttrue, counttotal)
percentage = (counttrue * 100)/counttotal
print(percentage)


print("FOR ONLY BIG COLUMNS____________________________________________")
for t in testSet:
	zz = []
	zz.append(t)
	predictDisease = calculateOnlyBigColumns(zz, trainingSet)
	cur.execute("INSERT INTO predictonlybig VALUES (" + str(t) + "," + str(predictDisease) + ");")
print("-----------------------------accuracy-------------------------------------")
counttrue = 0
counttotal = 0
for chosen in trainingSet:
	counttotal += 1
	testSet1 = []
	trainingSet1 = []
	accuracy(chosen, testSet1, trainingSet1)
	# print(testSet1, trainingSet1)
	predictDisease = calculateOnlyBigColumns(testSet1, trainingSet1)
	#print(predictDisease)
	mydisease=-1
	ar = mycsv[chosen][1]
	an = mycsv[chosen][2]
	cl = mycsv[chosen][3]
	try:
		if (int(ar) == 0 and int(an) == 0 and int(cl) == 0):
			mydisease=0
		elif (int(ar) == 0 and int(an) == 0 and int(cl) == 1):
			mydisease=1
		elif (int(ar) == 0 and int(an) == 1 and int(cl) == 0):
			mydisease=2
		elif (int(ar) == 0 and int(an) == 1 and int(cl) == 1):
			mydisease=3
		elif (int(ar) == 1 and int(an) == 0 and int(cl) == 0):
			mydisease=4
		elif (int(ar) == 1 and int(an) == 0 and int(cl) == 1):
			mydisease=5
		elif (int(ar) == 1 and int(an) == 1 and int(cl) == 0):
			mydisease=6
		elif (int(ar) == 1 and int(an) == 1 and int(cl) == 1):
			mydisease=7
		#print("Bimarii---->>>")
		# print(predictDisease, mydisease)
		if(predictDisease == mydisease):
			counttrue += 1
		cur.execute("INSERT INTO accuracyonlybig VALUES (" + str(chosen) + "," + str(predictDisease) + "," + str(mydisease) + "," + str(counttrue)+ "," + str(counttotal) + ");")

	except:
		pass
	# chosen += 1
print(counttrue, counttotal)
percentage = (counttrue * 100)/counttotal
print(percentage)


print("----------------------------Time of start is : ---------------------------")
print(startTime)
print("----------------------------Time of end is : ---------------------------")
print(datetime.datetime.today())
f.close() # you can omit in most cases as the destructor will call it
