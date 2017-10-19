from django.db import models

class committe(models.Model):
	name =models.CharField(max_length=50)
	members_no=models.IntegerField()
	value= models.TextField()
	def __str__(self):
		return (self.name)
class member(models.Model):
	"""docstring for members"""
	name=models.CharField(max_length=70)
	committe=models.ForeignKey(committe)
	tasks=models.IntegerField()
	def __str__(self):
		return (self.name)
