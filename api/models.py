from django.db import models

from studydrf import settings


class Category(models.Model):
    class Meta:
        db_table = 'categories'

    KIND = (
        ('I', 'Income'),
        ('O', "Outcome"),
    )

    title = models.CharField('Название', max_length=30)
    kind = models.CharField('Вид', max_length=50, choices=KIND)

    def __str__(self) -> str:
        return self.title


class Transaction(models.Model):
    class Meta:
        db_table = 'trnsactions'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    count = models.FloatField('Сумма')
    time = models.DateTimeField(auto_now_add=True)
    organization = models.CharField('Организация', max_length=50)
    description = models.CharField('Описание', max_length=50)

    def __str__(self) -> str:
        return self.organization
