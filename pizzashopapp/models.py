from django.db import models
from django.contrib.auth.models import User

class PizzaShop(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE,
        verbose_name='Пользователь', related_name='pizzashop')
    name = models.CharField("Название", max_length=100)
    phone = models.CharField("Телефон", max_length=100)
    address = models.CharField("Адрес", max_length=100)
    logo = models.ImageField("Логотип", upload_to='pizzashop_logo/', blank=True)

    def __str__(self):
        return str(self.name)

class Pizza(models.Model):
    owner = models.ForeignKey(PizzaShop, on_delete=models.CASCADE, verbose_name='Владелец')
    name = models.CharField("Название", max_length=100)
    short_description = models.CharField("Короткая информация", max_length=100)
    img = models.ImageField("Изображение", upload_to='pizza_image/', blank=False)
    price = models.IntegerField("Стоимость", default=0)

    def __str__(self):
        return str(self.name)