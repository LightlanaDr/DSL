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

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ: {self.id}'


class OrderProduct(models.Model):
    order = models.ForeignKey(NewOrder, on_delete=models.CASCADE)
    order_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Продукты в заказе'
