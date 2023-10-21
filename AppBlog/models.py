from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    body = models.CharField(max_length=1200)
    date = models.DateTimeField()
    
    image = models.ImageField(upload_to='media/blog/', null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

class Avatar(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
 
    def __str__(self):
        return f"./media/{self.imagen}"
    
