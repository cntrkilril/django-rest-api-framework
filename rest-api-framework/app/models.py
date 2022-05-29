from django.db import models
from simple_history.models import HistoricalRecords

class Profile(models.Model):
    username = models.CharField( verbose_name='Ник пользователя', max_length=100, unique=True)
    first_name = models.CharField(verbose_name='Имя пользователя',max_length=100 )
    last_name = models.CharField( verbose_name='Фамилия пользователя', max_length=100 )
    bio = models.TextField(verbose_name='Информация о пользователе', default='...')
    location = models.CharField(verbose_name='Город', max_length=100 )

    history = HistoricalRecords()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Post(models.Model):
    title = models.CharField( verbose_name='Заголовок', max_length=100)
    information = models.TextField(verbose_name='Основная информация')
    likes = models.IntegerField( verbose_name='Количество лайков')
    dislikes = models.IntegerField(verbose_name='Количество дизлайков')
    author = models.ManyToManyField(Profile, verbose_name='Автор поста')

    history = HistoricalRecords()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Groups(models.Model):
    group_name = models.CharField( verbose_name='Заголовок', max_length=100)
    subscribes = models.TextField(verbose_name='Основная информация')
    group_likes = models.IntegerField( verbose_name='Количество лайков', default=0)
    posts = models.ManyToManyField(Post, verbose_name='Пост')
    host = models.ManyToManyField(Profile, verbose_name='Хозяин группы')

    history = HistoricalRecords()

    def __str__(self):
        return self.group_name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

