from dcos_migrate.system import Migrator

class ClusterMigrator(Migrator):
    """docstring for SecretsMigrator."""

    def __init__(self, **kw):
        super(SecretsMigrator, self).__init__(**kw)
        self.translate = {}
