"""Plugin declaration for nautobot_prometheus_sd."""
# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
try:
    from importlib import metadata
except ImportError:
    # Python version < 3.8
    import importlib_metadata as metadata

__version__ = metadata.version(__name__)

from nautobot.extras.plugins import PluginConfig


class NautobotPrometheusSDConfig(PluginConfig):
    """Plugin configuration for the nautobot_prometheus_sd plugin."""

    name = "nautobot_prometheus_sd"
    verbose_name = "Nautobot prometheus sd"
    version = __version__
    author = "André Lopes"
    description = "Nautobot Prometheus SD."
    base_url = "prometheus-sd"
    required_settings = []
    min_version = "1.4.0"
    max_version = "1.9999"
    default_settings = {}
    caching_config = {}


config = NautobotPrometheusSDConfig  # pylint:disable=invalid-name
