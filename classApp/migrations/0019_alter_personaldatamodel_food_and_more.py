# Generated by Django 4.2.5 on 2024-01-02 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0018_alter_personaldatamodel_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldatamodel',
            name='food',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='personaldatamodel',
            name='hobby',
            field=models.JSONField(default=dict),
        ),
    ]