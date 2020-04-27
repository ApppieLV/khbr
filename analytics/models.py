from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from tinymce.models import HTMLField
class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    bio = models.CharField('Немного о себе', max_length=500)

    def __str__(self):
        return self.user.username

    
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

class Category(models.Model):
    name = models.CharField('Название', max_length=100)  
    slug = models.SlugField('Ссылка', unique=True)
    is_active = models.BooleanField(default=True, verbose_name='Видимость для пользователя')
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article_by_categ', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Article(models.Model):
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=120)
    slug = models.SlugField('Ссылка')
    short_description = HTMLField('Короткое описание на 200 символов', max_length=200)
    image = models.ImageField("Фотография", upload_to='article/%Y/%m/%h/', blank=True)
    content = HTMLField("Контент")
    integer_of_day = models.BooleanField('Цифра дня', default=False)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, verbose_name="Автор")
    created = models.DateTimeField('Дата создания', default=timezone.now)
    is_active = models.BooleanField(default=True, verbose_name='Видимость для пользователя')
    views = models.PositiveIntegerField('Просмотров публикации', default=0)

    def __str__(self):
        return self.title
            
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Links(models.Model):
    name = models.CharField('Название соц.сети', max_length=50)
    link = models.CharField('Ссылка', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Соц.сеть'
        verbose_name_plural = 'Соц.сети'

class Subscribe(models.Model):
    email = models.EmailField(verbose_name='Электронная почта', unique=True)
    created = models.DateTimeField('Дата создания', default=timezone.now)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Подписчик на рассылку'
        verbose_name_plural = 'Подписчики на рассылку'