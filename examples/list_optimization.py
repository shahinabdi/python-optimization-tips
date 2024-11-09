def calculate_squares_loop(numbers: list):
    """Traditional loop approach to calculate squares of even numbers."""
    squares = []
    for num in numbers:
        if num % 2 == 0:
            squares.append(num ** 2)
    return squares

def calculate_squares_comprehension(numbers: list):
    """List comprehension approach to calculate squares of even numbers."""
    squares = [num ** 2 for num in numbers if num % 2 == 0]
    return squares