from django.db import models
from gecko.models import Gecko
# Create your models here.


class HatchInfo(models.Model):
    set_temperature = models.FloatField()
    spawn_date = models.DateField()
    mother = models.ForeignKey(Gecko, on_delete=models.CASCADE, related_name='mother')
    father = models.ForeignKey(Gecko, on_delete=models.CASCADE, related_name='father')
    
    class Meta:
        verbose_name = '해칭 정보'
        verbose_name_plural = '해칭 정보 목록'

    def __str__(self):
        return f' {self.father.name} X {self.mother.name} [해칭일: {self.spawn_date}]'