from django.db import models
from django.conf import settings
from sosdvlpr.models import Language
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatar', blank= True)
    languages = models.ManyToManyField('Language', on_delete=models.CASCADE)

    def __str__(self):
        return 'Profile for ${self.user.username}'
