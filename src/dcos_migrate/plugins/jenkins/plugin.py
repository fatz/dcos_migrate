from dcos_migrate.plugins.plugin import MigratePlugin
from dcos_migrate.plugins.marathon import MarathonPlugin
from dcos_migrate.system import DCOSClient, BackupList, Backup

# we could have an abstract for cosmos services as we can extract package options in the same way
class JenkinsPlugin(MigratePlugin):
    """docstring for JenkinsPlugin."""
    plugin_name = "jenkins"

    depends_backup = [MarathonPlugin.plugin_name]

    def __init__(self):
        super(JenkinsPlugin, self).__init__()

    def backup(self, client: DCOSClient, backupList: BackupList, **kwargs) -> BackupList:
        bl = backupList()
        # extract PACKAGE options from marathon backup
        pass
