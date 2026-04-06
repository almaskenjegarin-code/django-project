from django.db import models
from django.contrib.auth.models import User

class Reward(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    cost = models.PositiveIntegerField(verbose_name="Стоимость (EcoCoins)")
    image = models.ImageField(upload_to='rewards/', null=True, blank=True, verbose_name="Изображение")
    is_active = models.BooleanField(default=True, verbose_name="Активно")

    class Meta:
        verbose_name = "Награда"
        verbose_name_plural = "Награды"

    def __str__(self):
        return f"{self.title} ({self.cost} EC)"

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    reward = models.ForeignKey(Reward, on_delete=models.SET_NULL, null=True, verbose_name="Награда")
    date_purchased = models.DateTimeField(auto_now_add=True, verbose_name="Дата покупки")

    class Meta:
        verbose_name = "Покупка"
        verbose_name_plural = "Покупки"

    def __str__(self):
        return f"{self.user.username} купил {self.reward.title if self.reward else 'Неизвестно'}"
