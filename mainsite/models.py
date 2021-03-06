from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200, null=True, blank=True)
    thumbnails = models.ImageField(null=True, blank=True, upload_to="images", default="desktop wallpaper.jpg") # pip install pillow
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, null=True)
    # slug =

    def __str__(self):
        return self.headline

class Certificate(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200, null=True, blank=True)
    validation_id = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    thumbnails = models.ImageField(null=True, blank=True, upload_to="images", default="desktop wallpaper.jpg") # pip install pillow
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, null=True)

    def __str__(self):
        return self.headline
