def main(a,b):
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is odd".
    Args:
        a: int
        b: int
    Returns:
        True if each of the numbers 'a' and 'b' is odd, False otherwise
    """
    return a % 2 == 0, b % 2 == 1
print(main(3,4))