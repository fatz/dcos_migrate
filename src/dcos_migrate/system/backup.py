class Backup(object):
    """docstring for Backup."""

    def __init__(self, pluginName: str, backupName: str, data=None):
        super(Backup, self).__init__()
        self._plugin_name = pluginName
        self._name = backupName
        self._data = data

    @property
    def plugin_name(self) -> str:
        return self._plugin_name

    @property
    def backup_name(self) -> str:
        return self._name

    @property
    def data(self) -> object:
        return self._data
