from django.db import models
from app.settings import APP_URL

class Platform(models.Model):
    
    name = models.CharField(max_length=20, null=False, blank=False)
    image = models.ImageField(upload_to='media/shop/flatform')
    
    def logo(self):
        return APP_URL + self.image.url

    def __str__(self) -> str:
        return self.name