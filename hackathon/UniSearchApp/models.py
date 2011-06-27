from django.contrib import admin
from django.db import models




# Create your models here.
class Hostels(models.Model):
	name= models.CharField(max_length=60)
	One_in_room_GHC = models.IntegerField(max_length=10)	
	Two_in_room_GHC = models.IntegerField(max_length=10)	
	Three_in_room_GHC = models.IntegerField(max_length=10)	
	university_id = models.IntegerField()
	def __unicode__(self):
		return self.name


class University(models.Model):
	name = models.CharField(max_length=60)
	description = models.TextField()
	location = models.CharField(max_length=60)
	def __unicode__(self):
		return self.name
	
class HostelsAdmin(admin.ModelAdmin):
	pass 
	
class UniversityAdmin(admin.ModelAdmin):
	pass	

admin.site.register(Hostels, HostelsAdmin)
admin.site.register(University, UniversityAdmin)

