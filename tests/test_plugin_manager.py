from dcos_migrate.plugins.plugin_manager import PluginManager
from dcos_migrate.plugins.cluster import ClusterPlugin
from dcos_migrate.plugins.secret import SecretPlugin
from dcos_migrate.plugins.marathon import MarathonPlugin
import pytest


def test_auto_discovery():
    pm = PluginManager()

    assert "cluster" in pm.plugins.keys()
    assert "marathon" in pm.plugins.keys()
    assert "secret" in pm.plugins.keys()


@pytest.mark.xfail(reason="Dependency management not fully working")
def test_dependencies():
    pm = PluginManager(plugins={
        'cluster': ClusterPlugin,
        'marathon': MarathonPlugin,
        'secret': SecretPlugin
    })

    assert len(pm.plugins) == 3
    assert len(pm.migrate) == 3
