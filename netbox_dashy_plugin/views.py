from django.db.models import Count
from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse
from .forms import PingForm
from icmplib import ping
from netbox.views import generic
from . import filtersets, forms, models, tables


def ping_view(request):
    if request.method == 'POST':
        form = PingForm(request.POST)
        if form.is_valid():
            target = form.cleaned_data['ip_address']
            ping_result = ping(target, count=10, interval=0.2)
            response = {
                'avg_rtt': ping_result.avg_rtt,
                'min_rtt': ping_result.min_rtt,
                'max_rtt': ping_result.max_rtt,
                'rtts': ping_result.rtts,
                'sent': ping_result.packets_sent,
                'recevied': ping_result.packets_received,
                'packet_loss': ping_result.packet_loss,
                'jitter': ping_result.jitter,
                'is_alive': ping_result.is_alive
            }
            return JsonResponse(response)
        else:
            form = PingForm()
        return render(request, 'ping_widget.html', {'form': form})