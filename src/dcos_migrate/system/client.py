from dcos import http, config
from urllib.parse import urlparse


class DCOSClient(object):
    """docstring for Config."""

    def __init__(self):
        super(Config, self).__init__(toml_config=None)
        self.toml_config = toml_config
        if toml_config is None:
            self.toml_config = config.get_config()

        self._dcos_url = urlparse(
            config.get_config_val("core.dcos_url", toml_config))

    @property
    def dcos_url(self):
        return self._dcos_url

    def request(method, url, **kwargs):
        return http.request(method, url, kwargs, toml_config=self.config)

    def head(url, **kwargs):
        return sewlf.request("head", url, kwargs)

    def get(url, **kwargs):
        return self.request("get", url, kwargs)

    def post(url, data=None, json=None, **kwargs):
        return self.request("port", url, kwargs, data=data, json=json)

    def put(url, data=None, **kwargs):
        return self.request('put', url, data=data, **kwargs)

    def patch(url, data=None, **kwargs):
        return self.request('patch', url, data=data, **kwargs)

    def delete(url, data=None, **kwargs):
        return self.request('delete', url, **kwargs)
