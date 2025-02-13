from django.db import models

class Test(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()

    class Meta:
        db_table = "test"
        verbose_name = "テスト"
