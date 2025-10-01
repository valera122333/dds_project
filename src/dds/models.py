from django.db import models
from django.utils import timezone


class Status(models.Model):
    """Статус (Бизнес, Личное, Налог и т.д.)"""
    name = models.CharField("Название статуса", max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Type(models.Model):
    """Тип операции (Пополнение, Списание и т.д.)"""
    name = models.CharField("Название типа", max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип операции"
        verbose_name_plural = "Типы операций"


class Category(models.Model):
    """Категория (например: Маркетинг, Инфраструктура)"""
    name = models.CharField("Название категории", max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="categories")

    def __str__(self):
        return f"{self.name} ({self.type})"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        unique_together = ("name", "type")


class SubCategory(models.Model):
    """Подкатегория (например: Avito, Farpost, VPS, Proxy)"""
    name = models.CharField("Название подкатегории", max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")

    def __str__(self):
        return f"{self.name} ({self.category})"

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        unique_together = ("name", "category")


class Record(models.Model):
    """Запись ДДС"""
    created_at = models.DateField(
        "Дата записи",
        default=timezone.now #текущая дата
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="records"
    )
    type = models.ForeignKey(
        Type,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="records"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="records"
    )
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="records"
    )
    amount = models.DecimalField("Сумма", max_digits=12, decimal_places=2)
    comment = models.TextField("Комментарий", blank=True, null=True)

    def __str__(self):
        return f"{self.created_at} | {self.type} | {self.amount}₽"

    class Meta:
        verbose_name = "Запись ДДС"
        verbose_name_plural = "Записи ДДС"
        ordering = ["-created_at"]
