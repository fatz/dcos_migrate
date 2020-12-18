# -*- coding: utf-8 -*-

import pytest
from dcos_migrate.marathon import MarathonMigrator


def test_id_parse():
    assert MarathonMigrator.parse_id("/foo/bar") == "bar.foo"
    assert MarathonMigrator.parse_id("/foo/bar_baz") == "bar-baz.foo"


def test_simple():
    m = MarathonMigrator(path="tests/examples/simple.json")

    m.migrate()

    assert m.manifest.resources[0].metadata.name == 'predictionio-server.group1'
