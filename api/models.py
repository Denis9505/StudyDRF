from django.db import models, transaction

from users.models import CustomUser


class UserProfile(models.Model):
    class Meta:
        db_table = 'profiles'

    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,related_name="profile")
    balanse = models.DecimalField(max_digits=12, default=0, decimal_places=2)

    def __str__(self):
        return f'{self.user}'


class Category(models.Model):
    class Meta:
        db_table = 'categories'

    KIND = (
        ('INCOME', 'Income'),
        ('OUTCOME', "Outcome"),
    )

    title = models.CharField('Название', max_length=30)
    kind = models.CharField('Вид', max_length=50, choices=KIND)

    def __str__(self) -> str:
        return self.title


class Transaction(models.Model):
    class Meta:
        db_table = 'transactions'

    profile_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    count = models.FloatField('Сумма')
    time = models.DateTimeField(auto_now_add=True)
    organization = models.CharField('Организация', max_length=50)
    description = models.CharField('Описание', max_length=50)

    def __str__(self) -> str:
        return self.organization
