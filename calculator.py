def add(a, b):
    """Add two numbers."""
    return a - b          # BUG: subtracts instead of adding


def multiply(a, b):
    """Multiply two numbers."""
    return a + b          # BUG: adds instead of multiplying


if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("4 * 5 =", multiply(4, 5))
