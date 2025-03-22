from netbox.filtersets import NetBoxModelFilterSet
from .models import Dashy


# class DashyFilterSet(NetBoxModelFilterSet):
#
#     class Meta:
#         model = Dashy
#         fields = ['name', ]
#
#     def search(self, queryset, name, value):
#         return queryset.filter(description__icontains=value)
