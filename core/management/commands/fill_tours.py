from django.core.management import BaseCommand
import json
from core.models import Tour


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('core/tashkent.json', mode='r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                tour = Tour.objects.get(title=item['title'])
                tour.full_description_ru = item['data']
                tour.save()
                print(f'{tour} - updated')
