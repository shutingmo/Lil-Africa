from django import forms
from .mixins import PopRequestMixin, CreateUpdateAjaxMixin


class BSModalForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    pass
