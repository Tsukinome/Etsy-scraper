def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"


def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b


def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0


class Calculator:
    """A simple calculator class."""

    def __init__(self):
        self.result = 0

    def add(self, value):
        """Add a value to the result."""
        self.result += value
        return self.result

    def reset(self):
        """Reset the calculator."""
        self.result = 0


# Test code
if __name__ == "__main__":
    print("Testing greet function:")
    print(greet("World"))
    print(greet("Python"))

    print("\nTesting add_numbers function:")
    print(f"5 + 3 = {add_numbers(5, 3)}")
    print(f"10 + 20 = {add_numbers(10, 20)}")

    print("\nTesting is_even function:")
    print(f"Is 4 even? {is_even(4)}")
    print(f"Is 7 even? {is_even(7)}")

    print("\nTesting Calculator class:")
    calc = Calculator()
    print(f"Initial result: {calc.result}")
    print(f"After adding 10: {calc.add(10)}")
    print(f"After adding 5: {calc.add(5)}")
    calc.reset()
    print(f"After reset: {calc.result}")