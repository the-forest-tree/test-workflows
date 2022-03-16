import typing as t
from collections import namedtuple

import pytest

MyParam = namedtuple("MyParam", "a, b")


def parameterize_equ() -> t.List[pytest.param]:
    params = [
        pytest.param(MyParam(a=1, b=1), id="test_1"),
        pytest.param(MyParam(a=3, b=3), id="test_3"),
    ]
    return params


def test_equ(my_param):
    assert my_param.a == my_param.b
