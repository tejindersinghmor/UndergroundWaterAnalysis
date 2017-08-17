from sklearn import datasets
from sklearn import svm
from sklearn import tree
from sklearn import neighbors
import xlrd
import pymysql
from xlrd import open_workbook

# digits = datasets.load_digits()
# print(len(digits.data))
# print(len(digits.target))
# print(digits.images[0])
def abc():
	conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='sonu1995', db='major2', autocommit=True)
	cur = conn.cursor()
	# wb = open_workbook("training-set/training_set.xls")
	cur.execute("SELECT * FROM training_training_set")
	training_set_data = cur.fetchall()
	counter = 1
	SVM_CORRECT = 0
	SVM_INCORRECT = 0
	decision_tree_predict_CORRECT = 0
	decision_tree_predict_INCORRECT = 0
	knnu_predict_CORRECT = 0
	knnu_predict_INCORRECT = 0
	knnd_predict_CORRECT = 0
	knnd_predict_INCORRECT = 0
	while (counter <= 1431):
		data = []
		target = []
		for t in training_set_data:
			# print(t)
			if (t[0] == counter):
				pass
			else:
				arr = [t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9]]
				data.append(arr)
				target.append(t[10])
		# print(data)
		# print(target)

		#svm
		clf = svm.SVC(gamma=0.0001, C=100)
		x,y = data, target
		clf.fit(x,y)

		#decision tree
		clftree = tree.DecisionTreeClassifier()
		clftree = clftree.fit(x,y)

		#knearestneighbour
		n_neighbors = 15
		#knn - uniform
		clfknnu = neighbors.KNeighborsClassifier(n_neighbors, 'uniform')
		clfknnu.fit(x, y)
		#knn - distance
		clfknnd = neighbors.KNeighborsClassifier(n_neighbors, 'distance')
		clfknnd.fit(x, y)

		cur.execute("SELECT * FROM training_training_set WHERE id=" + str(counter))
		test_set_data = cur.fetchall()
		print(test_set_data)
		for t in test_set_data:
			# print(t)
			predict = [t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9]]
			for d in data:
				if (d == predict):
					print(True)
				else:
					print(False)
			svm_predict = clf.predict(predict)[0]
			decision_tree_predict = clftree.predict(predict)[0]
			knnu_predict = clfknnu.predict(predict)[0]
			knnd_predict = clfknnd.predict(predict)[0]
			print(svm_predict)
			print(decision_tree_predict)
			print(knnd_predict)
			print(knnu_predict)
			count = t[0]
			# print(count)
			if (str(svm_predict) == t[10]):
				SVM_CORRECT += 1
			else:
				SVM_INCORRECT += 1
			if (str(decision_tree_predict) == t[10]):
				decision_tree_predict_CORRECT += 1
			else:
				decision_tree_predict_INCORRECT += 1
			if (str(knnu_predict) == t[10]):
				knnu_predict_CORRECT += 1
			else:
				knnu_predict_INCORRECT += 1
			if (str(knnd_predict) == t[10]):
				knnd_predict_CORRECT += 1
			else:
				knnd_predict_INCORRECT += 1
		# cur.execute("UPDATE training_test_set SET svm=%s, decisiontree=%s, knnuniform=%s, knndist=%s WHERE id=%s",
		#  (str(svm_predict), str(decision_tree_predict), str(knnu_predict), str(knnd_predict), str(count),))
		# print('Prediction svm:', clf.predict(predict)[0])
		# print('Prediction DecisionTreeClassifier: ', clftree.predict(predict))
		counter += 1
	print(SVM_CORRECT)
	print(SVM_INCORRECT)
	return {
		"SVM": SVM_CORRECT/(SVM_INCORRECT + SVM_CORRECT),
		"DEC": decision_tree_predict_CORRECT/ (decision_tree_predict_CORRECT + decision_tree_predict_INCORRECT),
		"KNNU": knnu_predict_CORRECT/(knnu_predict_CORRECT + knnu_predict_INCORRECT),
		"KNND": knnd_predict_CORRECT/(knnd_predict_CORRECT + knnd_predict_INCORRECT)
	}

