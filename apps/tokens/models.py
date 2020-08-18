from django.db import models

# Create your models here.
class Token(models.Model):
  APP = [
    ('android', 'Android App'),
    ('ios', 'IOS App'),
    ('windows', 'Windows App'),
    ('web', 'Web App')
  ]
  appname = models.CharField(max_length=16, choices=APP, null=True)
  userId = models.CharField(max_length=8, verbose_name="User Id")
  device_token = models.CharField(max_length=512, verbose_name="Device Token")
  created_at = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Created At')

  # class Meta:
