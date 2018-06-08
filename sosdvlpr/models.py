from django.db import models

from django.utils import timezone


class Thread(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    image = models.URLField(blank=True, null=True)
    text = models.TextField()
    is_sos = models.BooleanField(default=False)
    created_on =models.DateTimeField(default=timezone.now)
    framework = models.ManyToManyField('Language')
    def __str__(self):
        return self.title


class Comment(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    thread = models.ForeignKey('Thread', on_delete=models.CASCADE)
    text = models.TextField()
    image = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.text

    
class Language(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name