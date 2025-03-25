from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views


urlpatterns = (
    path("ping/", views.Ping.as_view(), name="ping_widget"),
)
