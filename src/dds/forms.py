from django import forms
from django.utils import timezone
from .models import Status, Type, Category, SubCategory, Record


class RecordForm(forms.ModelForm):
    """Форма создания/редактирования записи"""

    class Meta:
        model = Record
        fields = [
            "created_at",
            "status",
            "type",
            "category",
            "subcategory",
            "amount",
            "comment",
        ]
        widgets = {
            "created_at": forms.DateInput(
                attrs={"type": "date", "class": "form-control", "required": True}
            ),
            "status": forms.Select(attrs={"class": "form-control"}),
            "type": forms.Select(attrs={"class": "form-control", "required": True}),
            "category": forms.Select(
                attrs={"class": "form-control", "required": True}
            ),
            "subcategory": forms.Select(
                attrs={"class": "form-control", "required": True}
            ),
            "amount": forms.NumberInput(attrs={"class": "form-control", "required": True}),
            "comment": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Добавляем Bootstrap класс, если не установлен
        for field in self.fields.values():
            if not isinstance(field.widget, forms.Textarea):
                field.widget.attrs.setdefault("class", "form-control")

        # Обязательные поля (серверная валидация)
        self.fields["type"].required = True
        self.fields["category"].required = True
        self.fields["subcategory"].required = True
        self.fields["amount"].required = True

        # Подставляем сегодняшнюю дату при создании новой записи
        if not self.instance.pk:
            self.fields["created_at"].initial = timezone.now().date()

        # Категории
        if "type" in self.data:  # POST
            try:
                type_id = int(self.data.get("type"))
                self.fields["category"].queryset = Category.objects.filter(type_id=type_id)
            except (ValueError, TypeError):
                self.fields["category"].queryset = Category.objects.none()
        elif self.instance.pk and self.instance.type:  # Редактирование
            self.fields["category"].queryset = Category.objects.filter(type=self.instance.type)
        else:
            self.fields["category"].queryset = Category.objects.all()

        # Подкатегории
        if "category" in self.data:  # POST
            try:
                category_id = int(self.data.get("category"))
                self.fields["subcategory"].queryset = SubCategory.objects.filter(
                    category_id=category_id
                )
            except (ValueError, TypeError):
                self.fields["subcategory"].queryset = SubCategory.objects.none()
        elif self.instance.pk and self.instance.category:  # Редактирование
            self.fields["subcategory"].queryset = SubCategory.objects.filter(
                category=self.instance.category
            )
        else:
            self.fields["subcategory"].queryset = SubCategory.objects.none()


class RecordFilterForm(forms.Form):
    """Форма фильтрации записей"""
    start_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
    )
    end_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
    )
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    subcategory = forms.ModelChoiceField(
        queryset=SubCategory.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select"}),
    )


# Формы для справочных моделей
class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ["name"]


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ["name"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "type"]


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ["name", "category"]
