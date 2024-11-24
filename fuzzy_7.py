# Function to get user input for the fuzzy set
def get_fuzzy_set():
    n = int(input("Enter the number of elements in the fuzzy set: "))
    fuzzy_set = {}
    for _ in range(n):
        element = input("Enter the element: ")
        membership_value = float(input(f"Enter the membership value for {element}: "))
        fuzzy_set[element] = membership_value
    return fuzzy_set

# Maxima method
def maxima_method(fuzzy_set):
    max_value = max(fuzzy_set.values())
    maxima = [element for element, value in fuzzy_set.items() if value == max_value]
    return maxima

# Centroid method
def centroid_method(fuzzy_set):
    sum_product = sum(i * value for i, value in enumerate(fuzzy_set.values(), start=1))
    sum_values = sum(fuzzy_set.values())
    return sum_product / sum_values if sum_values != 0 else 0

# Weighted average method
def weighted_average_method(fuzzy_set):
    sum_product = sum(i * value for i, value in enumerate(fuzzy_set.values(), start=1))
    sum_weights = sum(range(1, len(fuzzy_set) + 1))
    return sum_product / sum_weights if sum_weights != 0 else 0

# Main function to run the de-fuzzification methods
def main():
    fuzzy_set = get_fuzzy_set()
    
    # Maxima method
    maxima = maxima_method(fuzzy_set)
    print("Maxima method result:", maxima)
    
    # Centroid method
    centroid = centroid_method(fuzzy_set)
    print("Centroid method result:", centroid)
    
    # Weighted average method
    weighted_average = weighted_average_method(fuzzy_set)
    print("Weighted average method result:", weighted_average)

# Run the main function
if __name__ == "__main__":
    main()
