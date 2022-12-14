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

class RequestTypeTwo(models.Model):
    job_location = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    number = models.CharField(max_length=25)
    email = models.EmailField(max_length=255)
    adres = models.CharField(max_length=255)
    cvalification = models.CharField(max_length=255)
    udostoverenie = models.FileField(upload_to='files', null=True, blank=True)
    diplom = models.FileField(upload_to='files', null=True, blank=True)
    udostoverenie_category = models.FileField(upload_to='files', null=True, blank=True)
    dok_staj = models.FileField(upload_to='files', null=True, blank=True)
    comment = models.CharField(max_length=255)
    prolojenie = models.FileField(upload_to='files', null=True, blank=True)

    def __str__(self):
        return self.name + " " + self.job_title