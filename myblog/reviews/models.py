from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class WatchList(models.Model):
    title= models.CharField(max_length=40)
    storyline= models.CharField(max_length=100)
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
     return self.title

class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    watchlist= models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name="reviews")
    description = models.CharField(max_length=100,null=True)
    active= models.BooleanField(default=True)
    created= models.DateField(auto_now_add=True)
    update= models.DateField(auto_now=True)

    def __str__(self):
       return str(self.rating) + " " + self.watchlist.title

