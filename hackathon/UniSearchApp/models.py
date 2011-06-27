from django.contrib import admin
from django.db import models




# Create your models here.
class Hostels(models.Model):
	name	= models.CharField(max_length=60)
	room_type = ('4-in-room GHC800.00','2-in-room GHC1300.00','4-in-room GHC3200.00')	
	university_id = models.IntegerField()
	def __unicode__(self):
		return self.title


class University(models.Model):
	name = models.CharField(max_length=60)
	description = models.TextField()
	location = models.CharField(max_length=60)
	
class HostelsAdmin(admin.ModelAdmin):
	pass 
	
class UniversityAdmin(admin.ModelAdmin):
	pass	

admin.site.register(Hostels, HostelsAdmin)
admin.site.register(University, UniversityAdmin)

