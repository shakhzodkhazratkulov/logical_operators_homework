def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits of the number are the same".
    Args:
        a: int
    Returns:
        True if all digits of a are the same, False otherwise
    """
    return a // 10 == a % 10

print(main(11))