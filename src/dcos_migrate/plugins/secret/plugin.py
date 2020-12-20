from dcos_migrate.plugins.plugin import MigratePlugin
from dcos_migrate.plugins.cluster import ClusterPlugin


class SecretPlugin(MigratePlugin):
    """docstring for SecretPlugin."""
    plugin_name = "secret"
    depends_migrate = [ClusterPlugin.plugin_name]

    def __init__(self):
        super(SecretPlugin, self).__init__()
