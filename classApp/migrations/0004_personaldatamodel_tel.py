# Generated by Django 4.2.5 on 2023-12-31 05:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0003_personaldatamodel_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldatamodel',
            name='tel',
            field=models.CharField(default='', max_length=11, validators=[django.core.validators.RegexValidator(message="電話番号は数字で入力してください 例: '09012340001'", regex='^[0-9]+$')], verbose_name='電話番号'),
        ),
    ]
