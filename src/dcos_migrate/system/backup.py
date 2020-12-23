import json


class Backup(object):
    """docstring for Backup."""

    def __init__(self, pluginName: str, backupName: str, data={}, extension='json'):
        super(Backup, self).__init__()
        self._plugin_name = pluginName
        self._name = backupName
        self._data = data
        self._extension = extension
        self._serializer = json.dumps
        self._deserializer = json.loads

    @property
    def plugin_name(self) -> str:
        return self._plugin_name

    @property
    def name(self) -> str:
        return self._name

    @property
    def extension(self) -> str:
        return self._extension

    @property
    def data(self) -> object:
        return self._data

    def serialize(self) -> str:
        return self._serializer(self._data)

    def deserialize(self, data: str) -> object:
        self._data = self._deserializer(data)
