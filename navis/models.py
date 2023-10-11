from django.db import models
from django.utils.translation import gettext_lazy as _


class Feedback(models.Model):
    ORDER_CHOICES = (
        ('Корпоративный', 'Корпоративный'),
        ('Индивидуальный', 'Индивидуальный'),
        ('Срочный', 'Срочный'),
        ('Предварительный', 'Предварительный'),
    )

    name = models.CharField(_('Имя'), max_length=100)
    phone = models.CharField(_('Телефон'), max_length=100)
    order = models.CharField(_('Заказы'), max_length=100, choices=ORDER_CHOICES)
    price = models.FloatField(_('Стоимость заказа'), null=True, blank=True)
    start_of_order = models.DateField(_('Начало заказа'))
    end_of_order = models.DateField(_('Окончание заказа'))
    comment = models.TextField(_('Что вас интересует?'))
    created_at = models.DateTimeField(_(''), auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Запросы на обратную связь'

    def __str__(self):
        return self.name
