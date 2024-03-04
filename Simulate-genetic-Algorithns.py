import random

def generate_random_gene(genes):
    return random.choice(genes)

def generate_random_individual(target_string, genes):
    return ''.join(generate_random_gene(genes) for _ in range(len(target_string)))

def calculate_fitness(individual, target_string):
    return sum(1 for a, b in zip(individual, target_string) if a == b)

def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(individual, mutation_rate, genes):
    mutated_individual = list(individual)
    for i in range(len(mutated_individual)):
        if random.random() < mutation_rate:
            mutated_individual[i] = generate_random_gene(genes)
    return ''.join(mutated_individual)

def genetic_algorithm(target_string, genes, population_size, mutation_rate):
    # Initialize population
    population = [generate_random_individual(target_string, genes) for _ in range(population_size)]

    generation = 1
    while True:
        # Evaluate fitness of each individual in the population
        fitness_scores = [calculate_fitness(individual, target_string) for individual in population]

        # Check for a perfect match
        if max(fitness_scores) == len(target_string):
            print("Target string reached!")
            break

        # Select the top individuals for reproduction
        selected_indices = sorted(range(len(fitness_scores)), key=lambda k: fitness_scores[k], reverse=True)[:10]
        selected_parents = [population[i] for i in selected_indices]

        # Create a new population through crossover and mutation
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = random.choices(selected_parents, k=2)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate, genes)
            new_population.append(child)

        population = new_population

        # Print progress
        print(f"Generation {generation}: {max(fitness_scores)} / {len(target_string)}")
        generation += 1

if __name__ == "__main__":
    # Get user input
    target_string = input("Enter the target string: ")
    genes = input("Enter the possible genes (characters): ")
    population_size = int(input("Enter the population size: "))
    mutation_rate = float(input("Enter the mutation rate: "))
    genetic_algorithm(target_string, genes, population_size, mutation_rate)
