# Generated by Django 4.2.5 on 2024-01-02 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0015_alter_personaldatamodel_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldatamodel',
            name='hobby',
            field=models.JSONField(null=True),
        ),
    ]
