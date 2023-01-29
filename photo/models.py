from django.db import models
# add pk number
from django.contrib import admin
from django.urls import reverse

# Create your models here.
class Photo(models.Model):
    photo_name = models.CharField(max_length=20) # name
    photo_location = models.CharField(max_length=50) #where is this photo
    photo_time = models.TimeField(auto_now=False, auto_now_add=False)
    photo_text = models.CharField(max_length=100) #The Photo illustrate

    def get_absolute_url(self):
        return f"/photo/{self.id}/"
        #reverse('photos:photo_id',kwargs={'pk':self.id})

    # cover photo.object
    def __str__(self):
        return self.photo_name

    
    
    
@admin.register(Photo)    
class PhotoAdmin(admin.ModelAdmin):
    # list_display = ('id','photo_name','photo_location','photo_time','photo_text')
    # the same 
    list_display = [field.name for field in Photo._meta.fields]

