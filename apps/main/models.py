from django.db import models

# Create your models here.

class Home(models.Model):
    github = models.URLField(
        verbose_name='Github домашней страницы'
    )
    twitter = models.URLField(
        verbose_name='twiiter домашней страницы'
    )
    facebook = models.URLField(
        verbose_name='facebook домашней страницы'
    )
    google = models.URLField(
        verbose_name='Google домашней страницы'
    )

    def __str__(self):
        return 'Домашние ссылки'
    
    class Meta:
        verbose_name_plural = 'Домашние ссылки'


class Personal(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Имя Сотрудника'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    photo = models.ImageField(
        upload_to='image/'
    )
    github = models.URLField(
        verbose_name='Ссылка на Github'
    )
    twitter = models.URLField(
        verbose_name='Ссылка на Twitter'
    )
    facebook = models.URLField(
        verbose_name='Ссылка на facebook'
    )
    google = models.URLField(
        verbose_name='Ссылка на Google+'
    )
    
    def __str__(self):
        return 'Персонал'
    
    class Meta:
        verbose_name_plural = 'Сотрудники'