from dcos_migrate.system import DCOSClient, BackupList, ManifestList


class MigratePlugin(object):
    """docstring for Migrator."""
    plugin_name = None
    backup_depends = []
    backup_data_depends = []
    migrate_depends = []
    migrate_data_ddepends = []

    def __init__(self):
        pass

    def backup(self, client: DCOSClient, **kwargs) -> BackupList:
        pass

    def backup_data(self, client: DCOSClient, **kwargs):
        pass

    def migrate(self, backupList: BackupList, manifestList: ManifestList, **kwargs) -> ManifestList:
        pass

    def migrate_data(self, backupList: BackupList, manifestList: ManifestList, **kwargs):
        pass
