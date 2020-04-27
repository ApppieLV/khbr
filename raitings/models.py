from django.db import models
from django.urls import reverse
from django.utils import timezone
from analytics.models import Author
from tinymce.models import HTMLField


class Raiting(models.Model):
    title = models.CharField('Заголовок',max_length=200)
    slug = models.SlugField('Ссылка')
    short_description = HTMLField('Короткое описание на 200 символов', max_length=200)
    content = HTMLField("Контент")
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, verbose_name="Автор")
    image = models.ImageField('Фотография', upload_to='raitings/%Y/%m/%h/', blank=True)
    created = models.DateTimeField('Дата создания', default=timezone.now)
    is_active = models.BooleanField(default=True, verbose_name='Видимость для пользователя')
    views = models.PositiveIntegerField('Просмотров публикации', default=0)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('raiting_detail', kwargs={'slug': self.slug})