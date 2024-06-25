from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class moviemodel(models.Model):
    title = models.CharField(max_length=40)
    director = models.CharField(max_length=20)
    trailer_url = models.CharField(max_length=50, null=True, blank=True)
    release_date = models.DateField()
    reviewed_on = models.DateField()
    story = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    review = models.TextField() 
    movie_poster = models.ImageField(upload_to="movie_poster_img", blank=True, null=True)
   
    
    
    def __str__(self):
        return self.title
    
    
class commentmodel(models.Model):
    username = models.CharField(max_length=30)
    movie    = models.ForeignKey(moviemodel, on_delete=models.CASCADE)
    comment  = models.TextField()
    comment_date = models.DateTimeField(auto_now=True)
    rating   = models.DecimalField(max_digits=2, decimal_places=1)
    
    def __str__(self):
        return self.username
    
class registermodel2(User):
    ph_no = models.PositiveBigIntegerField(null=True)