from django.db import models

# About Model
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    def __str__(self):
        return "About me"

#service model

class Service(models.Model):
    name = models.CharField(max_length=100 , verbose_name="Service Name")
    description = models.TextField(verbose_name="Service Description")
    
    def __str__(self):
        return self.name

#recent work model

class Recentwork(models.Model):
    tiltle = models.CharField(max_length=100 , verbose_name="Project Title")
    image = models.ImageField(upload_to="recentwork")

    def __str__(self):
        return self.tiltle
    
#client model

class Client(models.Model):
    name = models.CharField(max_length=100 , verbose_name="Client Name")
    description = models.TextField(verbose_name="Client Description")
    image = models.ImageField(upload_to="client" , default="default.png")

    def __str__(self):
        return self.name
