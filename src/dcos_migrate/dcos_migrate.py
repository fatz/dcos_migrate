from dcos_migrate.plugins.plugin_manager import PluginManager
from dcos_migrate.system.client import DCOSClient
from dcos_migrate.system.backup_list import BackupList


class DCOSMigrate(object):
    """docstring for DCOSMigrate."""

    def __init__(self):
        super(DCOSMigrate, self).__init__()
        self.client = DCOSClient()
        self.pm = PluginManager()
        self.manifest_list = ManifestList()
        self.backup_list = BackupList()

    def run():
        pass

    def backup(self, pluginName=None):
        for batch in self.pm.backup_batch:
            # each batch could also be executed in parallel.
            # But for not just start sequencial
            for plugin in batch:
                blist = plugin.backup(DCOSClient=self.client)
                self.backup_list.extend(blist)

    def migrate(self, pluginName=None):
        for batch in self.pm.migrate_batch:
            # each batch could also be executed in parallel.
            # But for not just start sequencial
            for plugin in batch:
                mlist = plugin.migrate(backupList=self.backup_list, manifestList=self.manifest_list)
                self.manifest_list.extend(mlist)


if __name__ == "__main__":
    DCOSMigrate().run()
