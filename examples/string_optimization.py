def concatenate_with_plus(items):
    """String concatenation using + operator."""
    result = ''
    for item in items:
        result = result + str(item) + ', '
    return result[:-2]  # Remove last comma and space

def concatenate_with_join(items):
    """String concatenation using join method."""
    return ', '.join(str(item) for item in items)

def concatenate_with_fstring(items):
    """String concatenation using f-strings in a list comprehension."""
    return ', '.join(f"{item}" for item in items)

def concatenate_with_format(items):
    """String concatenation using .format() method."""
    return ', '.join("{}".format(item) for item in items)