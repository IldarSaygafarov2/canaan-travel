from django.core.management import BaseCommand
import json
from core.models import Tour


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('temp-data/khiva.json', mode='r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                # print(item)
                tour = Tour.objects.get(title_en=item['title'])
                tour.full_description_en = item['data']
                tour.save()
                print(f'{tour} - updated')
