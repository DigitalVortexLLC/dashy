from django import forms
from ipam.models import Prefix
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField

from .models import Dashy


class DashyForm(NetBoxModelForm):
    class Meta:
        model = Dashy
        fields = ("name", "tags")
