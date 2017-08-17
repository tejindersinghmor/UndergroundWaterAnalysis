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
def getR(tr):
	data = []
	target = []
	conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='sonu1995', db='major2', autocommit=True)
	cur = conn.cursor()
	cur.execute("SELECT * FROM training_training_set")
	training_set_data = cur.fetchall()
	for t in training_set_data:
		print(t)
		arr = [t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9]]
		data.append(arr)
		target.append(t[10])
	# print(data)
	# print(target)

	#svm
	clf = svm.SVC(gamma=0.0001, C=100)
	x,y = data[:-1], target[:-1]
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

	predict = [tr[1], tr[2], tr[3], tr[4], tr[5], tr[6], tr[7], tr[8], tr[9]]
	svm_predict = clf.predict(predict)[0]
	decision_tree_predict = clftree.predict(predict)[0]
	knnu_predict = clfknnu.predict(predict)[0]
	knnd_predict = clfknnd.predict(predict)[0]
	return {
		"svm": svm_predict,
		"dec": decision_tree_predict,
		"knnu": knnu_predict,
		"knnd": knnd_predict
	}


