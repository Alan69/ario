from django.db import models

# Create your models here.
class Request(models.Model):
    ur_name = models.CharField(max_length=255, verbose_name="Полное официальное наименование юридического лица*")
    biin = models.CharField(max_length=50, verbose_name="Сведения о государственной регистрации (БИН)* ")
    fio = models.CharField(max_length=255, verbose_name="ФИО представителя*")
    job_title = models.CharField(max_length=255, verbose_name="Должность*")
    email = models.EmailField(max_length=255, verbose_name="E-mail*")
    number = models.CharField(max_length=20, verbose_name="Телефон*")
    city_number = models.CharField(max_length=20, verbose_name="Городской телефон")
    ur_adres = models.CharField(max_length=255, verbose_name="Юридический адрес")
    post_adres = models.CharField(max_length=255, verbose_name="Почтовый адрес")
    post_index = models.CharField(max_length=255, verbose_name="Почтовый индекс")
    ustav_copy = models.FileField(upload_to='media/files', null=True, blank=True, verbose_name="Копия устава")

    def __str__(self):
        return self.ur_name

    class Meta:
        verbose_name_plural = "Заявки Арио"

class RequestTypeTwo(models.Model):
    job_location = models.CharField(max_length=255, verbose_name="Место работы*")
    job_title = models.CharField(max_length=255, verbose_name="Должность*")
    surname = models.CharField(max_length=255, verbose_name="Фамилия*")
    name = models.CharField(max_length=255, verbose_name="Имя*")
    father_name = models.CharField(max_length=255, verbose_name="Отчество")
    number = models.CharField(max_length=25, verbose_name="Телефон*")
    email = models.EmailField(max_length=255, verbose_name="E-mail*")
    adres = models.CharField(max_length=255, verbose_name="Адрес фактического проживания")
    cvalification = models.CharField(max_length=255, verbose_name="Квалификация*")
    udostoverenie = models.FileField(upload_to='files', null=True, blank=True, verbose_name="Документ, подтверждающий личность* (УДВ/паспорт/вод.удостоверение и др.)")
    diplom = models.FileField(upload_to='files', null=True, blank=True, verbose_name="Диплом*")
    udostoverenie_category = models.FileField(upload_to='files', null=True, blank=True, verbose_name="Удостоверение о присвоении квалифицированной категории*")
    dok_staj = models.FileField(upload_to='files', null=True, blank=True, verbose_name="Документ, подтверждающий общий стаж ТД* (трудовая книжка, выписка из приказа и др.)")
    comment = models.CharField(max_length=255, verbose_name="Комментарий")
    prolojenie = models.FileField(upload_to='files', null=True, blank=True, verbose_name="Приложения ")

    def __str__(self):
        return self.name + " " + self.job_title

    class Meta:
        verbose_name_plural = "Заявки Талiмгер"

class RequestTypeThree(models.Model):
    job_location = models.CharField(max_length=255, verbose_name="Место работы*")
    job_title = models.CharField(max_length=255, verbose_name="Должность*")
    surname = models.CharField(max_length=255, verbose_name="Фамилия*")
    name = models.CharField(max_length=255, verbose_name="Имя*")
    father_name = models.CharField(max_length=255, verbose_name="Отчество")
    number = models.CharField(max_length=25, verbose_name="Телефон*")
    email = models.EmailField(max_length=255, verbose_name="E-mail*")
    adres = models.CharField(max_length=255, verbose_name="Адрес фактического проживания")
    lgota = models.CharField(max_length=255, verbose_name="Категория льгот*")
    dokument = models.FileField(upload_to='files', null=True, blank=True, verbose_name="Подтверждающий документ*")
    comment = models.CharField(max_length=255, verbose_name="Комментарий")

    class Meta:
        verbose_name_plural = "Заявки Устаз"

    def __str__(self):
        return self.name + " " + self.job_title