import yaml


class Manifest(list):
    """docstring for Manifest."""

    def __init__(self, pluginName: str, backupName: str, data={},
                 extension='yaml'):
        super(Manifest, self).__init__()
        self._plugin_name = pluginName
        self._name = backupName
        self._data = data
        self._extension = extension
        self._serializer = self.dump
        self._deserializer = yaml.load_all

        self.resources = []
        filePath = path

    def dump(self) -> str:
        docs = []
        for d in self:
            docs.append(yaml.dump(d))

        return '\n---\n'.join(docs)

    def find_resource_by_name(self, name):
        for r in self.resources:
            if r.Name == name:
                return r
        return None

    def findall_by_annotation(self, annotation, value=None):
        rs = []
        for r in self.resources:
            for a, v in r.metadata.annotations.items():
                if a == annotation:
                    if value is None:
                        rs.append(r)
                    else:
                        if v == value:
                            rs.append(r)

        if len(rs) > 0:
            return rs
        return None

    def find_by_annotation(self, annotation, value=None):
        r = self.findall_by_annotation(annotation=annotation, value=value)
        if r is None:
            return r

        # return first match
        return r[0]
