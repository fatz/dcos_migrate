from dcos_migrate.manifest_list import ManifestList

class MigratePlugin(object):
    """docstring for Migrator."""
    plugin_name = None
    backup_depends = []
    backup_data_depends = []
    migrate_depends = []
    migrate_data_ddepends = []

    def __init__(self):
        pass

    def backup(self, DCOSClient, **kwargs):
        pass

    def backup_data(self, DCOSClient, **kwargs):
        pass

    def migrate(self, backupList, manifestList, **kwargs):
        pass

    def migrate_data(self, backupList, manifestList, **kwargs):
        pass
