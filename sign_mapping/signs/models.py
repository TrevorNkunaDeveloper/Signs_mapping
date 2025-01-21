from django.db import models

class Sign(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='sign_images/')
    latitude = models.DecimalField(max_digits=9, decimal_places=6) 
    longitude = models.DecimalField(max_digits=9, decimal_places=6)  
    date_taken = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
