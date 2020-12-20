"""Ordinal: get ordinal strings from numbers"""


def ordinal(num: int) -> str:
    """Converts a number into an ordinal string"""
    # special cases
    if num % 100 in (11, 12, 13):
        return f'{num}th'

    last_digit = num % 10
    if last_digit == 1:
        return f'{num}st'
    if last_digit == 2:
        return f'{num}nd'
    if last_digit == 3:
        return f'{num}rd'

    return f'{num}th'
