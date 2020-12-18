class MigratePlugin(object):
    """docstring for Migrator."""

    def __init__(self, migrationPlugins):
        super(Migrator, self).__init__()
        self.migrationPlugins = migrationPlugins
        self.ManifestList = ManifestList()

    def backup_metadata(self, arg):
        pass

    def backup_data(self, arg):
        pass

    def migrate_metadata(self, arg):
        pass

    def migrate_data(self, arg):
        pass
