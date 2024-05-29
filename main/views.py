from django.shortcuts import render
from .models import About, Images, Review, Subscribe, Post, Coffee, Tag

# Create your views here.


def project(request):
    about_infos = About.objects.all().first()
    images = Images.objects.all()
    review = Review.objects.all()
    posts = Post.objects.all().order_by('created_at')
    coffees = Coffee.objects.all()
    tags = Tag.objects.all()
    context = {
        'abouts': about_infos,
        'images': images,
        'reviews': review,
        'posts': posts,
        'coffees': coffees,
        'tags': tags
    }
    return render(request, 'index.html', context)
