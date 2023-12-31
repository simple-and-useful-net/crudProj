
from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MinLengthValidator

class PersonalDataModel(models.Model):

    PREFECT_CHOICES = [
        ('北海道', '北海道'),
        ('東京都', '東京都'),
        ('大阪府', '大阪府'),
    ]

    SEX_CHOICES = [
        ('男', '男'),
        ('女', '女'),
    ]

    name = models.CharField(        max_length=10 )
    
    tel_regex = RegexValidator(     regex=r'^[0-9]+$', message = ("電話番号は数字で入力してください 例: '09012340001'"))
    tel = models.CharField(         validators=[tel_regex, MinLengthValidator(11)], max_length=11, default="")
     
    email=models.EmailField(        default="")
    sex = models.TextField(         choices=SEX_CHOICES,        default="男")
    prefecture = models.TextField(  choices=PREFECT_CHOICES,    blank=True, default="東京都")

    hobby   = models.JSONField()
    food    = models.JSONField()

