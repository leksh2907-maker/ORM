from django.db import models
from django.contrib import admin
class car_DB(models.Model):
    car_Brand=models.CharField(max_length=10)
    Number_plate=models.CharField(primary_key=True)
    price=models.IntegerField()
    color=models.CharField()
    warranty=models.IntegerField()
class car_DBAdmin(admin.ModelAdmin):
    list_display=["car_Brand","Number_plate","price","color","warranty"]
