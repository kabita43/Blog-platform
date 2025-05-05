from django.db import models
from django.urls import reverse

class Post(models.Model):
    tittle = models.CharField(max_length=100)
    slug = models.SlugField(unique= True)
    body= models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    published=models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('post_detail',args=[self.slug])
    class Meta:
        ordering=['created']