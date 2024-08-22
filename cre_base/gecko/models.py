from django.db import models

# Create your models here.


class Gecko(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M', "수컷"
        FEMALE = 'F', "암컷"
        UNKNOWN = 'U', "미구분"

    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, choices=Gender,default=Gender.UNKNOWN)
    
    
    class Meta:
        verbose_name = '게코'
        verbose_name_plural = '게코 목록'

    def __str__(self):
        return self.name