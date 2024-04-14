from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.

class Review(models.Model):
    author = models.CharField(max_length=20, verbose_name='Имя автора')
    text = models.TextField(verbose_name='Текст отзыва')

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Client(models.Model):
    img = models.ImageField(verbose_name='Фото компании клиента', upload_to='clients/')
    company_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Advantage(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Описание')
    icon = models.FileField(verbose_name='Иконка', upload_to='advantages', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'


class Destination(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    short_description = models.TextField(max_length=250, verbose_name='Краткое описание')
    preview = models.ImageField(verbose_name='Заставка', upload_to='destinations')
    is_popular = models.BooleanField(verbose_name='Добавить в раздел популярные туры?', default=False)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'


class Tour(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    # excerpt = models.TextField(verbose_name='Краткое описание', max_length=100)
    preview = models.ImageField(verbose_name='Заставка', upload_to='tours/', null=True, blank=True)
    price = models.IntegerField(verbose_name='Стоимость', null=True, blank=True)
    days = models.PositiveSmallIntegerField(verbose_name='Дней', null=True, blank=True)
    nights = models.PositiveSmallIntegerField(verbose_name='Ночей', null=True, blank=True)
    short_description = models.TextField(max_length=500, verbose_name='Краткое описание', null=True, blank=True)
    full_description = RichTextField(verbose_name='Полное описание 1', blank=True, null=True)
    # full_description_2 = RichTextField(verbose_name='Полное описание 2', blank=True, null=True)
    # map_link = models.URLField(verbose_name='Ссылка для карты', null=True, blank=True)
    is_popular = models.BooleanField(verbose_name='Популярный тур?', default=False)
    is_recommended = models.BooleanField(verbose_name='Рекомендуемый тур?', default=False)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, verbose_name='Направление', null=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'


class Article(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    excerpt = models.TextField(verbose_name='Краткое описание', max_length=500)
    preview = models.ImageField(verbose_name='Заставка', upload_to='articles/')
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class HotelItem(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    price = models.IntegerField(verbose_name='Цена')
    slug = models.SlugField(verbose_name='Слаг')
    preview = models.ImageField(verbose_name='Фото', upload_to='hotels/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'

