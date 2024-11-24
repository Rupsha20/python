def is_convex_fuzzy_set(fuzzy_set):
    """
    Check if a fuzzy set is convex.
    
    Parameters:
    fuzzy_set (dict): A dictionary where keys are elements (ordered by position) and values are membership degrees.
    
    Returns:
    bool: True if the fuzzy set is convex, False otherwise.
    """
    # Convert membership degrees to a list for easier index-based access
    membership_degrees = list(fuzzy_set.values())
    
    # Check convexity condition for every pair of neighboring elements
    for i in range(1, len(membership_degrees) - 1):
        # Check if the membership degree of the middle element is at least the minimum
        # of its two neighbors
        if membership_degrees[i] < min(membership_degrees[i - 1], membership_degrees[i + 1]):
            return False
    
    return True

# Example fuzzy set
fuzzy_set = {
    'a': 1.0,
    'b': 0.8,
    'c': 0.6,
    'd': 0.8,
    'e': 1.0
}

# Check if the fuzzy set is convex
if is_convex_fuzzy_set(fuzzy_set):
    print("The fuzzy set is convex.")
else:
    print("The fuzzy set is not convex.")
