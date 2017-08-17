from django.shortcuts import render
import acuracy
from getResults import getR
# Create your views here.
def home(request):
	return render(request, 'page1major.html')

def lastPage(request):
	return render(request, 'lastpage.html')

def greyAndCuckoo(request):
	# a = acuracy.abc()
	# print(a)
	prediction = request.GET.get("prediction")
	return render(request, 'greyandcuckoo.html', {"prediction": prediction})

def swarmi(request):
	prediction = request.GET.get("prediction")
	print(prediction)
	return render(request, 'swarmi.html', {"prediction": prediction})

def submitDetails(request):
	factor1 = request.POST.get("factor1")
	factor2 = request.POST.get("factor2")
	red = request.POST.get("red")
	green = request.POST.get("green")
	nir = request.POST.get("nir")
	mir = request.POST.get("mir")
	rs1 = request.POST.get("rs1")
	rs2 = request.POST.get("rs2")
	dem = request.POST.get("dem")
	t = []
	t.append(0)
	t.append(int(factor1))
	t.append(int(factor2))
	t.append(int(red))
	t.append(int(green))
	t.append(int(nir))
	t.append(int(mir))
	t.append(int(rs1))
	t.append(int(rs2))
	t.append(int(dem))
	result = getR(t)
	print(result)
	temp = {}
	temp["BARREN"] = 0
	temp["ROCKY"] = 0
	temp["VEGETATION"] = 0
	temp["WATER"] = 0
	temp["URBAN"] = 0
	max1 = 0
	temp[result["knnd"]] += 1
	temp[result["knnu"]] += 1
	temp[result["dec"]] += 1
	temp[result["svm"]] += 1

	max1 = max(temp["BARREN"], temp["ROCKY"], temp["VEGETATION"], temp["WATER"], temp["URBAN"])
	if (max1 == temp["BARREN"]):
		prediction = "BARREN"
	elif (max1 == temp["VEGETATION"]):
		prediction = "VEGETATION"
	elif (max1 == temp["WATER"]):
		prediction = "WATER"
	elif (max1 == temp["URBAN"]):
		prediction = "URBAN"
	else:
		prediction = "ROCKY"
	if (max1 < 2):
		prediction = "No definite prediction !"
	result["prediction"] = prediction
	return render(request, "page2.html", result)



