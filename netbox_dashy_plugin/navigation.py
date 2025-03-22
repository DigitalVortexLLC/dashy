from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

plugin_buttons = [
    PluginMenuButton(
        link="plugins:netbox_dashy_plugin:dashy_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
    )
]

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_dashy_plugin:dashy_list",
        link_text="Dashy",
        buttons=plugin_buttons,
    ),
)
