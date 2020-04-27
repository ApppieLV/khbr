from django.db import models
from django.urls import reverse
from django.utils import timezone
from embed_video.fields import EmbedVideoField
from analytics.models import Author
from tinymce.models import HTMLField

class VideoDownloading(models.Model):
    title = models.CharField('Заголовок',max_length=120, blank=True)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, verbose_name="Автор")
    url = models.CharField('Ссылка', max_length=200, help_text='URL-страницы')
    notes = HTMLField('Заметки', help_text='Заметки', blank=True, null=True)
    video = EmbedVideoField('Загрузить видео', help_text='Заходим на страницу видео-Поделиться-Встроить-Копируем link, содержащий строку embeded')
    created = models.DateTimeField('Дата создания', default=timezone.now)
    is_active = models.BooleanField(default=True, verbose_name='Видимость для пользователя')
                    
    class Meta:
        verbose_name = 'Видеообзор'
        verbose_name_plural = 'Видеообзоры'
    
    def __str__(self):
        return self.title