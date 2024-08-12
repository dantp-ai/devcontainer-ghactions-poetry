import pytest
from typing import Any


def test_one() -> None:
    assert len([1, 3, 4]) == 3


@pytest.mark.parametrize(
    "inp, expected",
    [
        (1, 2),
        (3, 4),
    ],
)
def test_add(inp: int, expected: int) -> None:
    assert inp + 1 == expected


def test_two() -> None:
    with pytest.raises(KeyError):
        d: dict[str, Any] = {}
        obs = d["obs"]  # noqa: F841
