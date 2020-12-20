from dcos_migrate.plugins.plugin import MigratePlugin
from dcos_migrate.plugins.cluster import ClusterPlugin
from dcos_migrate.plugins.secret import SecretPlugin

class MarathonPlugin(MigratePlugin):
    """docstring for MarathonPlugin."""
    plugin_name = "marathon"
    depends_migrate = [ClusterPlugin.plugin_name, SecretPlugin.plugin_name]

    def __init__(self):
        super(MarathonPlugin, self).__init__()
