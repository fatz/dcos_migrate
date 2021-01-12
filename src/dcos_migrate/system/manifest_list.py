from .storable_list import StorableList
from .manifest import Manifest


class ManifestList(StorableList):
    """docstring for ManifestList."""

    def __init__(self, dry=False, path='./dcos-migrate/migrate'):
        super(ManifestList, self).__init__(path)
        self._dry = dry

    def find_manifest_by_name(self, name):
        pass

    def manifests(self, pluginName: str):
        ml = ManifestList()
        for m in self:
            if m.plugin_name == pluginName:
                ml.append(m)

        return ml

    def append_data(self, pluginName: str, backupName: str,
                    extenstion: str, data: str):
        b = Manifest(pluginName=pluginName, backupName=backupName,
                     extenstion=extenstion).deserialize(data)

        self.append(b)
