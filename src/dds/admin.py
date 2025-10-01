from django.contrib import admin
from .models import Status, Type, Category, SubCategory, Record


# Регистрация модели Статуса
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


# Регистрация модели Типа
@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


# Регистрация модели Категории
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "type")
    list_filter = ("type",)
    search_fields = ("name",)


# Регистрация модели Подкатегории
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    list_filter = ("category",)
    search_fields = ("name",)


# Регистрация модели Записи (основная модель)
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "status",
        "type",
        "category",
        "subcategory",
        "amount",
        "comment",
    )
    list_filter = (
        "status",
        "type",
        "category",
        "subcategory",
        "created_at",
    )
    search_fields = ("comment",)
    date_hierarchy = "created_at"
