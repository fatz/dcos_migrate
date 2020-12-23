import json
from jsonpath_ng.ext import parse
from .manifest import Manifest


class Migrator(object):
    """docstring for Migrator."""

    def __init__(self, path=None, object=None, migrations=None):
        super(Migrator, self).__init__()
        self.path = path
        self.object = object
        self.migrations = migrations
        self.manifest = Manifest('', '')

        self.translate = {}

    def valid(self):
        """Returns True if self.object is what we expect"""
        return True

    def migrate(self):
        if not self.valid():
            return None

        for k, v in self.translate.items():
            expr = parse(k)
            for match in expr.find(self.object):
                v(match.full_path, match.value)

        return True
