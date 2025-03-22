from extras.dashboard.widgets import DashboardWidget, register_widget

@register_widget
class PingWidget(DashboardWidget):
    default_title = _('Ping')
    default_config = {}
    description = _('Ping a target from the netbox job worker.')
    template_name = 'templates/ping.html'
    width = 6
    height = 4

    class ConfigForm(WidgetConfigForm):
        pass

    def render(self, request):
        return None
    
    