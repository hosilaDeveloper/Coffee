from django.db import models


# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class About(TimeStamp):
    video = models.CharField(max_length=212)
    title = models.CharField(max_length=212)
    sub_title = models.CharField(max_length=212)
    description = models.TextField()
    sign = models.FileField(upload_to='about')
    background_image = models.ImageField(upload_to='about')

    def __str__(self):
        return self.title


class Coffee(TimeStamp):
    name = models.CharField(max_length=212)
    price = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Images(TimeStamp):
    image1 = models.ImageField(upload_to='images')
    image2 = models.ImageField(upload_to='images')
    image3 = models.ImageField(upload_to='images')
    image4 = models.ImageField(upload_to='images')
    image5 = models.ImageField(upload_to='images')


class Review(TimeStamp):
    happy_clients_count = models.CharField(max_length=212)
    projects_count = models.IntegerField(default=0)
    cups_coffee_count = models.IntegerField(default=0)
    submitted_count = models.IntegerField(default=0)


class Post(TimeStamp):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='blog')
    description = models.TextField()
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title


class Tag(TimeStamp):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Subscribe(TimeStamp):
    email = models.EmailField(null=True, blank=True)