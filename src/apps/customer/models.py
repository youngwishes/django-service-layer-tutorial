from __future__ import annotations

from typing import TYPE_CHECKING

from django.contrib.auth.models import User
from django.db import models

if TYPE_CHECKING:
    from apps.product.models import Product


class Customer(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name="пользователь",
        on_delete=models.SET_NULL,
        related_name="customer",
        null=True,
        blank=True,
    )
    balance = models.PositiveIntegerField("количество рублей на балансе")

    def can_buy_max_count_of(self, product: Product) -> int:
        if product.price > 0:
            return self.balance // product.price
        return 0

    class Meta:
        verbose_name = "заказчик"
        verbose_name_plural = "Заказчики"
