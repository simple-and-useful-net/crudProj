# Generated by Django 4.2.5 on 2023-12-31 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldatamodel',
            name='prefecture',
            field=models.TextField(blank=True, choices=[('北海道', '北海道'), ('東京都', '東京都'), ('大阪府', '大阪府')], default='東京都'),
        ),
        migrations.AlterField(
            model_name='personaldatamodel',
            name='sex',
            field=models.TextField(choices=[('男', '男'), ('女', '女')], default='男'),
        ),
    ]