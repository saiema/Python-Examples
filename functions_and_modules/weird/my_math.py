def max_int(a: int, b: int) -> int:
    """
    Returns the maximum of two numbers
    :param a: the first integer value
    :param b: the second integer value
    :return: 'a' iff 'a' is greater than 'b'; returns 'b' otherwise
    """
    if a > b:
        return a
    return b


def maximum_of_ints(int_values: list[int]) -> int:
    """
    Returns the maximum of a list of numbers
    :param int_values: a non-empty list of numbers
    :return: the maximum number in 'int_values'
    """
    assert int_values is not None
    assert len(int_values) > 0
    current_max: int = int_values[0]
    for e in int_values[1:]:
        current_max = max_int(current_max, e)
    return current_max


def reverse(number: int) -> int:
    """
    Reverses a number
    :param number: the number to reverse
    :return: a reversed version of 'number'
    """
    if number == 0:
        return 0
    multiplier: int = 1
    rev: int = 0
    while number != 0:
        digit: int = number % 10
        rev = (rev * 10) + digit
        number = number // 10
    return rev

