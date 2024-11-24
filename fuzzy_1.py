def union(set1, set2):
    return {x: max(set1.get(x, 0), set2.get(x, 0)) for x in set(set1) | set(set2)}

def intersection(set1, set2):
    return {x: min(set1.get(x, 0), set2.get(x, 0)) for x in set(set1) & set(set2)}

def complement(fuzzy_set):
    return {x: 1 - degree for x, degree in fuzzy_set.items()}

def difference(set1, set2):
    return {x: max(set1.get(x, 0) - set2.get(x, 0), 0) for x in set(set1) | set(set2)}

def de_morgan(set1, set2):
    return (complement(union(set1, set2)) == intersection(complement(set1), complement(set2)),
            complement(intersection(set1, set2)) == union(complement(set1), complement(set2)))

def cartesian_product(set1, set2):
    return {(x, y): min(set1[x], set2[y]) for x in set1 for y in set2}

def max_min_composition(r1, r2):
    result = {}
    for (a, b), val1 in r1.items():
        for (b2, c), val2 in r2.items():
            if b == b2:
                result[(a, c)] = max(result.get((a, c), 0), min(val1, val2))
    return result

# Example usage
set1 = {'a': 0.6, 'b': 0.7, 'c': 0.3}
set2 = {'b': 0.9, 'c': 0.8, 'd': 0.4}

print("Union:", union(set1, set2))
print("Intersection:", intersection(set1, set2))
print("Complement of Set 1:", complement(set1))
print("Complement of Set 2:", complement(set2))
print("Difference (Set1 - Set2):", difference(set1, set2))

de_morgan_results = de_morgan(set1, set2)
print("De Morgan's Law - complement of union:", de_morgan_results[0])
print("De Morgan's Law - complement of intersection:", de_morgan_results[1])

relation = cartesian_product(set1, set2)
print("Cartesian Product:", relation)

composition = max_min_composition(relation, relation)
print("Max-Min Composition:", composition)