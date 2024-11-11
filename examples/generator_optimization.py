def process_with_list(n):
    """Process numbers using list - loads all into memory."""
    numbers = [x * x for x in range(n)]  # Creates full list in memory
    return sum(numbers)

def process_with_generator(n):
    """Process numbers using generator - generates one at a time."""
    numbers = (x * x for x in range(n))  # Creates generator object
    return sum(numbers)

# Memory intensive example
def large_list_operation(n):
    """Creates a large list and performs operations."""
    data = [i * i for i in range(n)]
    return data

def large_generator_operation(n):
    """Creates a generator for the same operation."""
    for i in range(n):
        yield i * i