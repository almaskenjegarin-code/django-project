from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория")
    icon_class = models.CharField(max_length=50, blank=True, help_text="Например: bi-trash", verbose_name="Иконка Bootstrap")
    order = models.IntegerField(default=0, verbose_name="Порядок сортировки")

    class Meta:
        verbose_name = "Категория отходов"
        verbose_name_plural = "Категории отходов"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

class SortingRule(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='rules', verbose_name="Категория")
    title = models.CharField(max_length=200, verbose_name="Что сдаем?")
    description = models.TextField(verbose_name="Как подготовить к сдаче")
    is_recyclable = models.BooleanField(default=True, verbose_name="Перерабатывается?")

    class Meta:
        verbose_name = "Правило сортировки"
        verbose_name_plural = "Правила сортировки"

    def __str__(self):
        return self.title
