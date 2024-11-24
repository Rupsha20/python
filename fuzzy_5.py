def is_singleton(fuzzy_set):
    """
    Check whether a fuzzy set is a singleton.
    
    A fuzzy set is a singleton if it contains exactly one element.
    
    :param fuzzy_set: Dictionary representing a fuzzy set where keys are elements and values are membership values.
    :return: True if the fuzzy set is a singleton, False otherwise.
    """
    return len(fuzzy_set) == 1

# Example usage
fuzzy_set1 = {
    'A': 0.6
}

fuzzy_set2 = {
    'A': 0.6,
    'B': 0.4
}

if is_singleton(fuzzy_set1):
    print("The fuzzy set1 is a singleton.")
else:
    print("The fuzzy set1 is not a singleton.")

if is_singleton(fuzzy_set2):
    print("The fuzzy set2 is a singleton.")
else:
    print("The fuzzy set2 is not a singleton.")
