def is_normal_fuzzy_set(fuzzy_set):
    """
    Check whether a fuzzy set is normal.
    
    A fuzzy set is normal if at least one of its membership values is 1.
    
    :param fuzzy_set: Dictionary representing a fuzzy set where keys are elements and values are membership values.
    :return: True if the fuzzy set is normal, False otherwise.
    """
    for value in fuzzy_set.values():
        if value == 1:
            return True
    return False

# Example usage
fuzzy_set = {
    'A': 0.6,
    'B': 1.0,
    'C': 0.8,
    'D': 0.4
}

if is_normal_fuzzy_set(fuzzy_set):
    print("The fuzzy set is normal.")
else:
    print("The fuzzy set is not normal.")
