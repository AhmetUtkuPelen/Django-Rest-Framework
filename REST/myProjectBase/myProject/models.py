from django.db import models

# Create your models here.

class MovieData(models.Model):
    name = models.CharField(max_length=500)
    duration = models.FloatField()
    rating = models.FloatField()
    type = models.CharField(max_length=50,default='action')
    image = models.ImageField(upload_to='Images/',default='Images/None/Noimg.jpg')
    
    def __str__(self):
        return self.name
    
    
