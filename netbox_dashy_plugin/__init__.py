"""Top-level package for NetBox Dashy Plugin."""

__author__ = """Digital Vortex"""
__email__ = "netbox@digitalvortex.net"
__version__ = "0.1.0"


from netbox.plugins import PluginConfig


class DashyConfig(PluginConfig):
    name = "netbox_dashy_plugin"
    verbose_name = "NetBox Dashy Plugin"
    description = "Dashboard widgets and things."
    version = "0.1.0"
    base_url = "dashy"
    author = __author__
    required_settings = []
    default_settings = []


config = DashyConfig
