from django.shortcuts import render
from . import models


# Create your views here.


def home_view(request):
    reviews = models.Review.objects.all()
    clients = models.Client.objects.all()
    advantages = models.Advantage.objects.all()
    destinations = models.Destination.objects.filter(is_popular=True)

    popular_tours = models.Tour.objects.filter(is_popular=True)
    recommended_tours = models.Tour.objects.filter(is_recommended=True)

    articles = models.Article.objects.all()

    context = {
        'reviews': reviews,
        'clients': clients,
        'advantages': advantages,
        'destinations': destinations,
        'popular_tours': popular_tours,
        'recommended_tours': recommended_tours,
        'articles': articles
    }
    return render(request, 'core/index.html', context)


def about_view(request):
    return render(request, 'core/about.html')


def reviews_view(request):
    reviews = models.Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'core/reviews.html', context)


def booking_view(request):
    return render(request, 'core/booking.html')


def mission_view(request):
    return render(request, 'core/mission.html')