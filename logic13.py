def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is even".
    Args:
        a: int
    Returns:
        True if all digits sum is even, False otherwise
    """
    return (a % 10 + a // 10) % 2 == 0
print(main(34))