def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a: int
    Returns:
        True if a is five-digit number, False otherwise
    """
    return 9999 < a < 100000
print(main(45689))