import requests
from django.conf import settings
from django.shortcuts import render, redirect

from . import models


# Create your views here.


def send_mail(request):
    data = request.POST
    msg = f'Почта отправленная с сайта: {data["email"]}'
    requests.post(settings.CHANNEL_API_LINK.format(
        token=settings.BOT_TOKEN,
        channel_id=settings.CHANNEL_ID,
        text=msg
    ))

    return redirect('home')


def send_username_and_phone(request):
    data = request.POST

    msg = f"Имя пользователя: {data['username']}\nНомер телефона: {data['phone']}"
    requests.post(settings.CHANNEL_API_LINK.format(
        token=settings.BOT_TOKEN,
        channel_id=settings.CHANNEL_ID,
        text=msg
    ))
    return redirect('home')


def book_tour(request):
    data = request.POST

    msg = f"""
Имя: {data['username']}
Дата: {data['date']}
Почта: {data['email']}
Номер телефона: {data['phone']}
Комментарий: {data['body']}
"""
    requests.post(settings.CHANNEL_API_LINK.format(
        token=settings.BOT_TOKEN,
        channel_id=settings.CHANNEL_ID,
        text=msg
    ))
    return redirect('home')


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
    clients = models.Client.objects.all()
    context = {
        'clients': clients
    }
    return render(request, 'core/about.html', context)


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


def tourists_info_view(request):
    return render(request, 'core/info.html')


def blog_view(request):
    articles = models.Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'core/blog.html', context)


def destinations_view(request, slug):
    destination = models.Destination.objects.get(slug=slug)
    tours = models.Tour.objects.filter(destination=destination)
    context = {
        'title': destination.title,
        'tours': tours
    }
    return render(request, 'core/destinations.html', context)


def tours_view(request):
    popular_tours = models.Tour.objects.all()
    context = {
        'tours': popular_tours
    }
    return render(request, 'core/tours.html', context)
