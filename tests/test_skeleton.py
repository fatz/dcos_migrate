# -*- coding: utf-8 -*-

import pytest
from dcos_migrate.skeleton import fib

__author__ = "Jan Ulferts"
__copyright__ = "Jan Ulferts"
__license__ = "apache"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
