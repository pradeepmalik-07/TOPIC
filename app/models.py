from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=50,primary_key=True)

    def __str__(self):
        return self.topic_name

class Webpages(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    url=models.CharField(max_length=50)
    email=models.CharField(max_length=50)

    def __str__(self):
        return self.name  

class AccessRecord(models.Model):
    name=models.ForeignKey(Webpages,on_delete=models.CASCADE)
    author=models.CharField(max_length=50)
    date=models.DateField()    
    def __str__(self):
        return self.author
