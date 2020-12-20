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
        (87, '87th')
    )
)
def test_ordinals(num: int, expected: str) -> None:
    """Ordinal tests"""
    assert ordinal.ordinal(num) == expected
