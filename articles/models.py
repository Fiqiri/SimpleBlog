from django.db import models
from taggit.managers import TaggableManager
from PIL import Image


# Create your models here.
class Article(models.Model):
    slug = models.SlugField()
    image = models.ImageField(default='image.png', blank=True)
    tags = TaggableManager()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slug

    def snippet(self):
        return f'{self.content[:75]} .....'

    def save(self):
        super().save()  # saving image first

        img = Image.open(self.image.path)  # Open image using self

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.image.path)  # saving image at the same path
