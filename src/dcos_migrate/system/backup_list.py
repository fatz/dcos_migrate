import os
from .storable_list import StorableList
from .backup import Backup


class BackupList(StorableList):
    """docstring for BackupList."""

    def __init__(self, dry=False, path='./dcos-migrate/backup'):
        super(BackupList, self).__init__(path)
        self._dry = dry

    def backups(self, pluginName):
        pass

    def backup(self, pluginName, backupName):
        pass

    def append_data(self, pluginName: str, backupName: str,
                    extenstion: str, data: str):
        b = Backup(pluginName=pluginName, backupName=backupName,
                   extenstion=extenstion).deserialize(data)

        self.append(b)
