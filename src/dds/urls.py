from django.urls import path
from . import views

urlpatterns = [
    # Записи
    path("", views.record_list, name="record_list"),
    path("create/", views.record_create, name="record_create"),
    path("<int:pk>/edit/", views.record_edit, name="record_edit"),
    path("<int:pk>/delete/", views.record_delete, name="record_delete"),

    # AJAX для динамических списков
    path("ajax/load-categories/", views.ajax_load_categories, name="ajax_load_categories"),
    path("ajax/load-subcategories/", views.ajax_load_subcategories, name="ajax_load_subcategories"),

    # Статусы
    path("status/", views.status_list, name="status_list"),
    path("status/create/", views.status_create, name="status_create"),
    path("status/<int:pk>/edit/", views.status_edit, name="status_edit"),
    path("status/<int:pk>/delete/", views.status_delete, name="status_delete"),

    # Типы
    path("type/", views.type_list, name="type_list"),
    path("type/create/", views.type_create, name="type_create"),
    path("type/<int:pk>/edit/", views.type_edit, name="type_edit"),
    path("type/<int:pk>/delete/", views.type_delete, name="type_delete"),

    # Категории
    path("category/", views.category_list, name="category_list"),
    path("category/create/", views.category_create, name="category_create"),
    path("category/<int:pk>/edit/", views.category_edit, name="category_edit"),
    path("category/<int:pk>/delete/", views.category_delete, name="category_delete"),

    # Подкатегории
    path("subcategory/", views.subcategory_list, name="subcategory_list"),
    path("subcategory/create/", views.subcategory_create, name="subcategory_create"),
    path("subcategory/<int:pk>/edit/", views.subcategory_edit, name="subcategory_edit"),
    path("subcategory/<int:pk>/delete/", views.subcategory_delete, name="subcategory_delete"),

    # Справочники
    path("reference/", views.reference_data, name="reference_data"),
]
