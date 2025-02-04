import re

from django.core.exceptions import ValidationError
from django.forms import BooleanField, ModelForm

from catalog.models import Product

FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ("views_counter",)

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной!")
        return price

    def clean_name(self):
        name = self.cleaned_data["name"]
        name_list = re.sub("[^\w\s]", " ", name).lower().split()
        for word in name_list:
            if word in FORBIDDEN_WORDS:
                raise ValidationError(f"{word} - запрещенное слово!")
        return name

    def clean_description(self):
        description = self.cleaned_data["description"]
        description_list = re.sub("[^\w\s]", " ", description).lower().split()
        for word in description_list:
            if word.strip() in FORBIDDEN_WORDS:
                raise ValidationError(f"{word} - запрещенное слово!")
        return description

class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ("is_published",)
