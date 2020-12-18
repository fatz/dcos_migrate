from dcos_migrate.migrator import Migrator
from dcos_migrate.migrate_plugin import MigratePlugin
from kubernetes.client.models import V1Deployment, V1ObjectMeta, V1Secret

class MarathonMigrator(Migrator):
    """docstring for MarathonMigrator."""

    def __init__(self, **kw):
        super(MarathonMigrator, self).__init__(**kw)
        self.translate = {
            "id": self.translate_id
        }
        self.deployment_name = None

    @staticmethod
    def parse_id(id):
        id = id.replace('_', '-')
        return '.'.join(reversed(list(filter(None,id.split('/')))))

    def translate_id(self, key, value):
        # create Deployment
        meta = V1ObjectMeta(name=MarathonMigrator.parse_id(value))
        m = V1Deployment(metadata=meta)

        self.manifest.append(m)
        self.deployment_name = value

    def det_deployment(self):
        self.manifest.find_resource_by_name(self.deployment_name)


class MarathonPlugin(MigratePlugin):
    """docstring for MarathonPlugin."""

    def __init__(self, arg):
        super(MarathonPlugin, self).__init__()
        self.arg = arg
