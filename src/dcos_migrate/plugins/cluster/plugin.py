from dcos_migrate.plugins.plugin import MigratePlugin

class ClusterPlugin(MigratePlugin):
    """docstring for ClusterPlugin."""
    plugin_name = "cluster"
    # No depends wanna run first

    def __init__(self):
        super(ClusterPlugin, self).__init__()
