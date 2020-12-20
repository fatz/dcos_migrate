class Manifest(object):
    """docstring for Manifest."""

    def __init__(self, path):
        super(Manifest, self).__init__()
        self.resources = []
        filePath = path

    def to_yaml(self):
        pass

    def append(self, object):
        self.resources.append(object)

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
