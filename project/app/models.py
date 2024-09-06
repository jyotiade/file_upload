from django.db import models

class Student(models.Model):
    item_name=models.CharField(max_length=50)
    item_image=models.ImageField(upload_to="image/")
    item_resume=models.FileField(upload_to="file/")