def find_common_elements_list(search_values):
    """List-based approach to find common elements."""
    numbers = list(range(1000000))
    found = []
    for value in search_values:
        if value in numbers:
            found.append(value)
    return found

def find_common_elements_set(search_values):
    """Set-based approach to find common elements."""
    numbers = set(range(1000000))
    found = [value for value in search_values if value in numbers]
    return found