from dcos_migrate.manifest_list import ManifestList

class MigratePlugin(object):
    """docstring for Migrator."""
    plugin_name = None
    backup_depends = []
    backup_data_depends = []
    migrate_depends = []
    migrate_data_ddepends = []

    def __init__(self):
        self.manifest_list = ManifestList()

    def backup_metadata(self, arg):
        pass

    def backup_data(self, arg):
        pass

    def migrate_metadata(self, arg):
        pass

    def migrate_data(self, arg):
        pass
