from django.db import models

# Create your models here.

class training_set(models.Model):
	factor1 = models.IntegerField()
	factor2 = models.IntegerField()
	red = models.IntegerField()
	green = models.IntegerField()
	nir = models.IntegerField()
	mir = models.IntegerField()
	rs1 = models.IntegerField()
	rs2 = models.IntegerField()
	dem = models.IntegerField()
	decision = models.CharField(max_length=255)

class test_set(models.Model):
	factor1 = models.IntegerField()
	factor2 = models.IntegerField()
	red = models.IntegerField()
	green = models.IntegerField()
	nir = models.IntegerField()
	mir = models.IntegerField()
	rs1 = models.IntegerField()
	rs2 = models.IntegerField()
	dem = models.IntegerField()
	svm = models.CharField(max_length=255)
	decisiontree = models.CharField(max_length=255)
	knnuniform = models.CharField(max_length=255)
	knndist = models.CharField(max_length=255)