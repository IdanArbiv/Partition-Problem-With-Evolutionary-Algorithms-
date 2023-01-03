from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.creators.ga_creators.bit_string_vector_creator import GABitStringVectorCreator
from eckity.genetic_operators.crossovers.vector_k_point_crossover import VectorKPointsCrossover
from eckity.genetic_operators.mutations.vector_random_mutation import BitStringVectorFlipMutation
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.subpopulation import Subpopulation
from LiveGraphStatistics import LiveGraphStatistics
from PartitionEvaluator import PartitionEvaluator, RANDOM_UPPER_BOUND, SAVE_RESULT, NUM_ITEMS, POPULATION_SIZE, \
    ELITISM_RATE, CROSSOVER_PROB, CROSSOVER_CELL_NUM, MUTATION_PROB, MAX_GENERATION


def main():
    """
    Partition Optimization Problem: \n
    Input - A = {a1, ... , an} weights series of numbers \n
    Output - A partition of {1, ... ,n} into two foreign groups D0,D1 that minimizes the difference between \n
    the sum of weights in the two groups.
    ----------
    About the Partition problem and examples: https://en.wikipedia.org/wiki/Partition_problem
    """
    # Initialize the evolutionary algorithm
    algo = SimpleEvolution(
        Subpopulation(
            # Define which data structure to use and how many items in the main group
            creators=GABitStringVectorCreator(length=NUM_ITEMS),
            # The number of individuals in this subpopulation.
            population_size=POPULATION_SIZE,
            # user-defined fitness evaluation method
            evaluator=PartitionEvaluator(),
            # minimize problem (Absolute subtraction of the values between 2 groups), smaller fitness is better
            higher_is_better=False,
            # What percentage of the subpopulation's individuals should be kept as elites for the next generation
            elitism_rate=ELITISM_RATE,
            # Genetic operators sequence to be applied in each generation
            operators_sequence=[
                # CROSSOVER_PROB probability to execute crossover on CROSSOVER_CELL_NUM cells from the random vector
                VectorKPointsCrossover(probability=CROSSOVER_PROB, k=CROSSOVER_CELL_NUM),
                # MUTATION_PROB probability to execute mutation on random vector
                BitStringVectorFlipMutation(probability=MUTATION_PROB)
            ],
            selection_methods=[
                # (selection method, selection probability) tuple
                (TournamentSelection(tournament_size=4, higher_is_better=False), 1)
            ]),
        breeder=SimpleBreeder(),
        # Maximal number of worker nodes for the Executor object that evaluates the fitness of the individuals
        max_workers=1,
        max_generation=MAX_GENERATION,
        # Add termination_checker
        statistics=LiveGraphStatistics(RANDOM_UPPER_BOUND, POPULATION_SIZE, SAVE_RESULT)
    )

    # Evolve the generated initial population
    algo.evolve()


if __name__ == '__main__':
    main()
