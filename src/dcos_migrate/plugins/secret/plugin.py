from dcos_migrate.plugins.plugin import MigratePlugin
from dcos_migrate.plugins.cluster import ClusterPlugin
from dcos_migrate.system.client import DCOSClient
import urllib
import base64


# class DCOSSecretsService:
#
#     def __init__(self, DCOSClient):
#         self.client = DCOSClient
#         self.url = self.client.dcos_url + '/secrets/v1'
#         self.store = 'default'
#
#     def list(self, path: str = '') -> List[str]:
#         r = self.client.get(
#             self.url + '/secret/{store}/{path}?list=true'.format(
#                 store=urllib.parse.quote(self.store), path=urllib.parse.quote(path)
#             ),
#         )
#         r.raise_for_status()
#         return r.json()['array']
#
#     def get(self, path: str, key: str) -> Dict[str, str]:
#         # There are two types of secrets: text and binary.  Using `Accept: */*`
#         # the returned `Content-Type` will be `application/octet-stream` for
#         # binary secrets and `application/json` for text secrets.
#         #
#         # Returns the secret as:
#         # {
#         #   "path": "...",
#         #   "key": "...",
#         #   "type": "{text|binary}",
#         #   "value": "base64(value)"
#         # }
#         full_path = (path + '/' + key).strip('/')
#         url = self.url + '/secret/{store}/{path}'.format(
#             store=urllib.parse.quote(self.store), path=urllib.parse.quote(full_path)
#         )
#         r = self.client.requests.get(
#             url
#         )
#         r.raise_for_status()
#         content_type = r.headers['Content-Type']
#         if content_type == 'application/octet-stream':
#             response = {
#                 'type': 'binary',
#                 'value': base64.b64encode(r.content).decode('ascii')
#             }
#         else:
#             assert content_type == 'application/json', content_type
#             response = r.json()
#             response['type'] = 'text'
#             # Always encode the secret as base64, even when it is safe UTF-8 text.
#             # This obscures the values to prevent unintentional exposure.
#             response['value'] = base64.b64encode(
#                 response['value'].encode('utf-8')).decode('ascii')
#         # Always add the `path` and `key` values to the JSON response. Ensure the key always has a
#         # value by taking the last component of the path if necessary.
#         if not key:
#             parts = path.rsplit('/', 1)
#             key = parts.pop()
#             parts.append('')
#             path = parts[0]
#         response['path'] = path
#         response['key'] = key
#         return response


class SecretPlugin(MigratePlugin):
    """docstring for SecretPlugin."""

    plugin_name = "secret"
    depends_migrate = [ClusterPlugin.plugin_name]

    def __init__(self):
        super(SecretPlugin, self).__init__()

    def backup(self, DCOSClient, **kwargs):
        pass
