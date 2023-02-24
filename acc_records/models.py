from django.db import models


# Create your models here.

class Account(models.Model):
    account_id = models.BigAutoField(primary_key=True)
    account_money = models.IntegerField()
    account_content = models.TextField()
    account_datetime = models.DateTimeField()

    class Meta:
        # db_table = 'libaojiandahaoren'
        verbose_name = "test"
    def __str__(self):
        return self.account_id


