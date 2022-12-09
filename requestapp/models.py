from django.db import models

# Create your models here.
class Request(models.Model):
    ur_name = models.CharField(max_length=255)
    biin = models.CharField(max_length=50)
    fio = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    number = models.CharField(max_length=20)
    city_number = models.CharField(max_length=20)
    ur_adres = models.CharField(max_length=255)
    post_adres = models.CharField(max_length=255)
    post_index = models.CharField(max_length=255)
    ustav_copy = models.FileField(upload_to='files', null=True, blank=True)

    def __str__(self):
        return self.ur_name
