import random
import numpy as np
from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator

# Evolutionary Algorithm Parameters
NUM_ITEMS = 50
POPULATION_SIZE = 10
ELITISM_RATE = 0.0
CROSSOVER_PROB = 0.5
CROSSOVER_CELL_NUM = 2
MUTATION_PROB = 0.05
MAX_GENERATION = 10
ONLY_INT_NUMS = False
RANDOM_UPPER_BOUND = 1000
RANDOM_LOWER_BOUND = 0
SAVE_RESULT = True


class PartitionEvaluator(SimpleIndividualEvaluator):
    """
    Evaluator class for the Partition problem, responsible for defining a fitness evaluation method and evaluating it.
    Fitness is the absolute value of the subtraction between the 2 partition groups weights
    Attributes
    -------
    items: An array of weights
    """

    def __init__(self, items=None):
        super().__init__()
        # If no items are provided, generate a set of random items
        if items is None:
            items = {i: (random.randint(RANDOM_LOWER_BOUND, RANDOM_UPPER_BOUND) if ONLY_INT_NUMS else
                         random.uniform(RANDOM_LOWER_BOUND, RANDOM_UPPER_BOUND)) for i in range(NUM_ITEMS)}
        self.items = items
        # Print the dictionary of items to the console
        print("The group with the numbers:")
        print(items)

    def _evaluate_individual(self, individual):
        """
        Compute the fitness value of a given individual.
        Fitness value is the absolute value of the subtraction of the values between the 2 partition groups

        Parameters
        ----------
        individual: Vector
            The individual to compute the fitness value for.
        Returns
        -------
        float
            The evaluated fitness value of the given individual.
        """
        sum_group_zero = 0.0
        sum_group_one = 0.0
        # Iterate over the values in the individual's list
        for i in range(individual.size()):
            # If the value is 1, add the corresponding item value to sum_group_one
            if individual.cell_value(i):
                sum_group_one += self.items[i]
            # If the value is 0, add the corresponding item value to sum_group_zero
            else:
                sum_group_zero += self.items[i]
        # Return the absolute value of the difference between sum_group_one and sum_group_zero
        # This value will be used as the fitness value for the individual
        return np.abs(sum_group_one - sum_group_zero)
