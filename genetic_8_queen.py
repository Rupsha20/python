import random

# Define the number of queens
N = 8

# Function to create an individual
def create_individual():
    return [random.randint(0, N - 1) for _ in range(N)]

# Function to calculate fitness
def fitness(individual):
    conflicts = 0
    n = len(individual)
    for i in range(n):
        for j in range(i + 1, n):
            if individual[i] == individual[j] or abs(individual[i] - individual[j]) == abs(i - j):
                conflicts += 1
    return -conflicts  # Negative because we want to minimize conflicts

# Perform crossover between two individuals
def crossover(parent1, parent2):
    crossover_point = random.randint(0, N - 1)
    return parent1[:crossover_point] + parent2[crossover_point:]

# Mutate an individual
def mutate(individual):
    i = random.randint(0, N - 1)
    individual[i] = random.randint(0, N - 1)

# Create initial population
def create_population(size):
    return [create_individual() for _ in range(size)]

# Genetic algorithm to solve the 8-queens problem
def genetic_algorithm(population):
    mutation_probability = 0.1
    for generation in range(1000):
        population = sorted(population, key=fitness, reverse=True)
        print(f"Generation {generation}: Best fitness = {-fitness(population[0])}")
        if fitness(population[0]) == 0:
            break
        new_population = population[:2]  # Keep the best two individuals
        while len(new_population) < len(population):
            parent1, parent2 = random.choices(population[:50], k=2)
            child = crossover(parent1, parent2)
            if random.random() < mutation_probability:
                mutate(child)
            new_population.append(child)
        population = new_population
    return population[0]

# Parameters
population_size = 100

# Create initial population
population = create_population(population_size)

# Run genetic algorithm
best_solution = genetic_algorithm(population)

# Print the best solution
print("Best solution found:")
print(best_solution)
