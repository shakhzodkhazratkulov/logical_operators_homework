def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a: int
    Returns:
        True if all digits sum is odd, False otherwise
    """
    return (a % 10 + a // 10) % 2 == 1
print(main(69))