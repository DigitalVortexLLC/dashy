from django.db.models import Count
from django.contrib import messages
from django.shortcuts import redirect
from .jobs import PingJob
from netbox.views import generic
from . import filtersets, forms, models, tables


class PingView(generic.ObjectView):
    action = 'ping'
    queryset = models.Dashy.objects.all()

    def do_action(self, request, form):
        PingJob.enqueue(
            data=request.data,
            user=request.user,
            commit=False
        )
        messages.success(request, _("Pinging target IP"))

        return redirect('home')