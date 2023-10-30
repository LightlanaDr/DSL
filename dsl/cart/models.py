from django.db import models

from catalog.models import Product


class NewOrder(models.Model):
    ORDER_STATUS = (
        ('Неоплачен', 'Неоплачен'),
        ('Оплачен', 'Оплачен'),
        ('Доставляется', 'Доставляется'),
        ('Доставлен', 'Доставлен'),
    )
    first_name = models.CharField(max_length=50, default=None)
    last_name = models.CharField(max_length=50, default=None)
    email = models.EmailField(default=None)
    phone = models.CharField(max_length=12, default=None)
    address = models.CharField(max_length=250, default=None)
    data_created = models.DateTimeField(auto_now_add=True)
    data_update = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=ORDER_STATUS, max_length=100, default='Неоплачен')
    total_sum = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f'Заказ: {self.first_name}{self.last_name}' \
               f'Дата: {self.data_created}, статус:{self.status}' \
               f'Сумма: {self.total_sum}'


class OrderProduct(models.Model):
    order = models.ForeignKey(NewOrder, on_delete=models.CASCADE)
    order_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=1)
