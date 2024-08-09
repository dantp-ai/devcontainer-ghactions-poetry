import pytest


def test_one():
    assert len([1, 3, 4]) == 3


def test_two():
    with pytest.raises(KeyError):
        d = {}
        obs = d["obs"]
        return obs
