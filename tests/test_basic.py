import pytest
from typing import Any


def test_one() -> None:
    assert len([1, 3, 4]) == 3


def test_two() -> None:
    with pytest.raises(KeyError):
        d: dict[str, Any] = {}
        obs = d["obs"]  # noqa: F841
