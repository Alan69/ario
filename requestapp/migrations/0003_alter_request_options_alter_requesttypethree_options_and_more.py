# Generated by Django 4.1.4 on 2022-12-27 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("requestapp", "0002_requesttypethree"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="request",
            options={"verbose_name_plural": "Заявки Арио"},
        ),
        migrations.AlterModelOptions(
            name="requesttypethree",
            options={"verbose_name_plural": "Заявки Устаз"},
        ),
        migrations.AlterModelOptions(
            name="requesttypetwo",
            options={"verbose_name_plural": "Заявки Талiмгер"},
        ),
        migrations.AlterField(
            model_name="request",
            name="biin",
            field=models.CharField(
                max_length=50,
                verbose_name="Сведения о государственной регистрации (БИН)* ",
            ),
        ),
        migrations.AlterField(
            model_name="request",
            name="city_number",
            field=models.CharField(max_length=20, verbose_name="Городской телефон"),
        ),
        migrations.AlterField(
            model_name="request",
            name="email",
            field=models.EmailField(max_length=255, verbose_name="E-mail*"),
        ),
        migrations.AlterField(
            model_name="request",
            name="fio",
            field=models.CharField(max_length=255, verbose_name="ФИО представителя*"),
        ),
        migrations.AlterField(
            model_name="request",
            name="job_title",
            field=models.CharField(max_length=255, verbose_name="Должность*"),
        ),
        migrations.AlterField(
            model_name="request",
            name="number",
            field=models.CharField(max_length=20, verbose_name="Телефон*"),
        ),
        migrations.AlterField(
            model_name="request",
            name="post_adres",
            field=models.CharField(max_length=255, verbose_name="Почтовый адрес"),
        ),
        migrations.AlterField(
            model_name="request",
            name="post_index",
            field=models.CharField(max_length=255, verbose_name="Почтовый индекс"),
        ),
        migrations.AlterField(
            model_name="request",
            name="ur_adres",
            field=models.CharField(max_length=255, verbose_name="Юридический адрес"),
        ),
        migrations.AlterField(
            model_name="request",
            name="ur_name",
            field=models.CharField(
                max_length=255,
                verbose_name="Полное официальное наименование юридического лица*",
            ),
        ),
        migrations.AlterField(
            model_name="request",
            name="ustav_copy",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="media/files",
                verbose_name="Копия устава",
            ),
        ),
        migrations.AlterField(
            model_name="requesttypethree",
            name="adres",
            field=models.CharField(
                max_length=255, verbose_name="Адрес фактического проживания"
            ),
        ),
        migrations.AlterField(
            model_name="requesttypethree",
            name="comment",
            field=models.CharField(max_length=255, verbose_name="Комментарий"),
        ),
        migrations.AlterField(
            model_name="requesttypethree",
            name="dokument",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="files",
                verbose_name="Подтверждающий документ*",
            ),
        ),
        migrations.AlterField(
            model_name="requesttypethree",
            name="email",
            field=models.EmailField(max_length=255, verbose_name="E-mail*"),
        ),
        migrations.AlterField(
            model_name="requesttypethree",
            name="father_name",
            field=models.CharField(max_length=255, verbose_name="Отчество"),
        ),
        migrations.AlterField(
            model_name="requesttypethree",
            name="job_location",
            field=models.CharField(max_length=255, verbose_name="Место работы*"),
        ),
        migrations.AlterField(
            model_name="requesttypethree",
            name="job_title",
            field=models.CharField(max_length=255, verbose_name="Должность*"),
        ),
        migrations.AlterField(
            model_name="requesttypethree",
            name="lgota",
            field=models.CharField(max_length=255, verbose_name="Категория льгот*"),
        ),
        migrations.AlterField(
            model_name="requesttypethree",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Имя*"),
        ),
        migrations.AlterField(
            model_name="requesttypethree",
            name="number",
            field=models.CharField(max_length=25, verbose_name="Телефон*"),
        ),
        migrations.AlterField(
            model_name="requesttypethree",
            name="surname",
            field=models.CharField(max_length=255, verbose_name="Фамилия*"),
        ),
        migrations.AlterField(
            model_name="requesttypetwo",
            name="adres",
            field=models.CharField(
                max_length=255, verbose_name="Адрес фактического проживания"
            ),
        ),
        migrations.AlterField(
            model_name="requesttypetwo",
            name="comment",
            field=models.CharField(max_length=255, verbose_name="Комментарий"),
        ),
        migrations.AlterField(
            model_name="requesttypetwo",
            name="cvalification",
            field=models.CharField(max_length=255, verbose_name="Квалификация*"),
        ),
        migrations.AlterField(
            model_name="requesttypetwo",
            name="diplom",
            field=models.FileField(
                blank=True, null=True, upload_to="files", verbose_name="Диплом*"
            ),
        ),
        migrations.AlterField(
            model_name="requesttypetwo",
            name="dok_staj",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="files",
                verbose_name="Документ, подтверждающий общий стаж ТД* (трудовая книжка, выписка из приказа и др.)",
            ),
        ),
        migrations.AlterField(
            model_name="requesttypetwo",
            name="email",
            field=models.EmailField(max_length=255, verbose_name="E-mail*"),
        ),
        migrations.AlterField(
            model_name="requesttypetwo",
            name="father_name",
            field=models.CharField(max_length=255, verbose_name="Отчество"),
        ),
        migrations.AlterField(
            model_name="requesttypetwo",
            name="job_location",
            field=models.CharField(max_length=255, verbose_name="Место работы*"),
        ),
        migrations.AlterField(
            model_name="requesttypetwo",
            name="job_title",
            field=models.CharField(max_length=255, verbose_name="Должность*"),
        ),
        migrations.AlterField(
            model_name="requesttypetwo",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Имя*"),
        ),
        migrations.AlterField(
            model_name="requesttypetwo",
            name="number",
            field=models.CharField(max_length=25, verbose_name="Телефон*"),
        ),
        migrations.AlterField(
            model_name="requesttypetwo",
            name="prolojenie",
            field=models.FileField(
                blank=True, null=True, upload_to="files", verbose_name="Приложения "
            ),
        ),
        migrations.AlterField(
            model_name="requesttypetwo",
            name="surname",
            field=models.CharField(max_length=255, verbose_name="Фамилия*"),
        ),
        migrations.AlterField(
            model_name="requesttypetwo",
            name="udostoverenie",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="files",
                verbose_name="Документ, подтверждающий личность* (УДВ/паспорт/вод.удостоверение и др.)",
            ),
        ),
        migrations.AlterField(
            model_name="requesttypetwo",
            name="udostoverenie_category",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="files",
                verbose_name="Удостоверение о присвоении квалифицированной категории*",
            ),
        ),
    ]
