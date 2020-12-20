"""Ordinal tests"""
import pytest

import ordinal


@pytest.mark.parametrize(
    ('num', 'expected'),
    (
        (1, '1st'),
        (42, '42nd'),
        (11, '11th'),
        (13, '13th'),
        (1523, '1523rd'),
        (87, '87th'),
        (213, '213th'),
    )
)
def test_ordinal(num: int, expected: str) -> None:
    """Ordinal tests"""
    assert ordinal.ordinal(num) == expected


@pytest.mark.parametrize(
    'num',
    (
        (-1),
        (-314),
    )
)
def test_ordinal_failure(num: int) -> None:
    with pytest.raises(ValueError):
        ordinal.ordinal(num)
