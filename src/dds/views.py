from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from django.db.models import Q

from .models import (
    Record, Status, Type, Category, SubCategory
)
from .forms import (
    RecordForm, RecordFilterForm, StatusForm, TypeForm, CategoryForm, SubCategoryForm
)


# ------------------- RECORD -------------------
def record_list(request):
    """Список записей с фильтрацией"""
    records = Record.objects.select_related(
        "status", "type", "category", "subcategory"
    ).all()
    filter_form = RecordFilterForm(request.GET or None)

    if filter_form.is_valid():
        data = filter_form.cleaned_data
        if data.get("start_date"):
            records = records.filter(created_at__gte=data["start_date"])
        if data.get("end_date"):
            records = records.filter(created_at__lte=data["end_date"])
        if data.get("status"):
            records = records.filter(status=data["status"])
        if data.get("type"):
            records = records.filter(type=data["type"])
        if data.get("category"):
            records = records.filter(category=data["category"])
        if data.get("subcategory"):
            records = records.filter(subcategory=data["subcategory"])

    return render(request, "dds/record_list.html", {
        "records": records,
        "filter_form": filter_form
    })


def record_create(request):
    """Создание новой записи"""
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            if not obj.created_at:
                obj.created_at = timezone.now().date()
            obj.save()
            return redirect("record_list")
    else:
        today_iso = timezone.now().date().strftime("%Y-%m-%d")
        form = RecordForm(initial={"created_at": today_iso})

    return render(request, "dds/record_form.html", {"form": form})


def record_edit(request, pk):
    """Редактирование существующей записи"""
    record = get_object_or_404(Record, pk=pk)
    if request.method == "POST":
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect("record_list")
    else:
        form = RecordForm(instance=record)

    return render(request, "dds/record_form.html", {
        "form": form,
        "title": "Редактирование записи"
    })


def record_delete(request, pk):
    """Удаление записи"""
    record = get_object_or_404(Record, pk=pk)
    if request.method == "POST":
        record.delete()
        return redirect("record_list")
    return render(request, "dds/record_delete.html", {"record": record})


def ajax_load_categories(request):
    """Возвращает категории для выбранного типа (AJAX)"""
    type_id = request.GET.get("type_id")
    categories = Category.objects.filter(type_id=type_id).values("id", "name")
    return JsonResponse(list(categories), safe=False)


def ajax_load_subcategories(request):
    """Возвращает подкатегории для выбранной категории (AJAX)"""
    category_id = request.GET.get("category_id")
    subcategories = SubCategory.objects.filter(category_id=category_id).values("id", "name")
    return JsonResponse(list(subcategories), safe=False)


# ------------------- STATUS -------------------
def status_list(request):
    items = Status.objects.all()
    return render(request, "dds/status_list.html", {"items": items})


def status_create(request):
    form = StatusForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("status_list")
    return render(request, "dds/status_form.html", {"form": form})


def status_edit(request, pk):
    item = get_object_or_404(Status, pk=pk)
    form = StatusForm(request.POST or None, instance=item)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("status_list")
    return render(request, "dds/status_form.html", {"form": form})


def status_delete(request, pk):
    item = get_object_or_404(Status, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect("status_list")
    return render(request, "dds/status_confirm_delete.html", {"item": item})


# ------------------- TYPE -------------------
def type_list(request):
    items = Type.objects.all()
    return render(request, "dds/type_list.html", {"items": items})


def type_create(request):
    form = TypeForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("type_list")
    return render(request, "dds/type_form.html", {"form": form})


def type_edit(request, pk):
    item = get_object_or_404(Type, pk=pk)
    form = TypeForm(request.POST or None, instance=item)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("type_list")
    return render(request, "dds/type_form.html", {"form": form})


def type_delete(request, pk):
    item = get_object_or_404(Type, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect("type_list")
    return render(request, "dds/type_confirm_delete.html", {"item": item})


# ------------------- CATEGORY -------------------
def category_list(request):
    items = Category.objects.select_related("type").all()
    return render(request, "dds/category_list.html", {"items": items})


def category_create(request):
    form = CategoryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("category_list")
    return render(request, "dds/category_form.html", {"form": form})


def category_edit(request, pk):
    item = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=item)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("category_list")
    return render(request, "dds/category_form.html", {"form": form})


def category_delete(request, pk):
    item = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect("category_list")
    return render(request, "dds/category_confirm_delete.html", {"item": item})


# ------------------- SUBCATEGORY -------------------
def subcategory_list(request):
    items = SubCategory.objects.select_related("category").all()
    return render(request, "dds/subcategory_list.html", {"items": items})


def subcategory_create(request):
    form = SubCategoryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("subcategory_list")
    return render(request, "dds/subcategory_form.html", {"form": form})


def subcategory_edit(request, pk):
    item = get_object_or_404(SubCategory, pk=pk)
    form = SubCategoryForm(request.POST or None, instance=item)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("subcategory_list")
    return render(request, "dds/subcategory_form.html", {"form": form})


def subcategory_delete(request, pk):
    item = get_object_or_404(SubCategory, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect("subcategory_list")
    return render(request, "dds/subcategory_confirm_delete.html", {"item": item})


# ------------------- REFERENCE -------------------
def reference_data(request):
    """Страница справочников"""
    return render(request, "dds/reference_data.html")
