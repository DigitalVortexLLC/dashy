from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views


urlpatterns = (
    path("dashys/", views.DashyListView.as_view(), name="dashy_list"),
    path("dashys/add/", views.DashyEditView.as_view(), name="dashy_add"),
    path("dashys/<int:pk>/", views.DashyView.as_view(), name="dashy"),
    path("dashys/<int:pk>/edit/", views.DashyEditView.as_view(), name="dashy_edit"),
    path("dashys/<int:pk>/delete/", views.DashyDeleteView.as_view(), name="dashy_delete"),
    path(
        "dashys/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="dashy_changelog",
        kwargs={"model": models.Dashy},
    ),
)
