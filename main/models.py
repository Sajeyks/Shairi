from email.mime import image
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.deletion import CASCADE
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', default='default.png')
    
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return 'Shairi\main\static\main\profile1.jpg'

    def __str__(self):
        return f'{self.user.username} Profile'

    # Overide save method of model
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        # resize it
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Sonnet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    poem = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='sonnet', on_delete=CASCADE)

    class meta:
        ordering = ['created']
        verbose_name_plural = "Sonnets"

    def __str__(self):
        return self.title
