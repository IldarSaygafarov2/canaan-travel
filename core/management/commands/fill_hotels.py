from django.core.management import BaseCommand
from django.template.defaultfilters import slugify

from core.models import Hotel
from core.utils import get_hotels

from django.conf import settings
import os

import requests


class Command(BaseCommand):
    def handle(self, *args, **options):
        hotels = get_hotels('https://canaan.travel/ru/uzbekistan/hotels')
        for item in hotels:
            price = int(''.join(list(filter(lambda x: x.isdigit(), item['price']))))
            with open(os.path.join(settings.BASE_DIR, os.path.basename(item["img"])), 'wb') as file:
                file.write(requests.get(item["img"]).content)
            obj = Hotel.objects.create(
                name=item['title'],
                price=price,
                preview=f'hotels/{os.path.basename(item["img"])}',
                slug=slugify(item['title'])
            )
            obj.save()
            print(obj, 'created')
