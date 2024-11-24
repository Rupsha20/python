def alpha_cut(fuzzy_set, alpha):
    """
    Find the alpha-cut of a fuzzy set.
    
    Parameters:
    fuzzy_set (dict): A dictionary where keys are elements and values are membership degrees.
    alpha (float): The alpha threshold (0 <= alpha <= 1).
    
    Returns:
    list: A list of elements in the alpha-cut.
    """
    # Return elements where the membership degree is greater than or equal to alpha
    return [element for element, membership_degree in fuzzy_set.items() if membership_degree >= alpha]

# Example fuzzy set
fuzzy_set = {
    'a': 0.7,
    'b': 0.8,
    'c': 0.4,
    'd': 1.0
}

# Specify the alpha value
alpha = 0.5

# Find the alpha-cut
alpha_cut_set = alpha_cut(fuzzy_set, alpha)
print(f"The alpha-cut for alpha = {alpha} is:", alpha_cut_set)
