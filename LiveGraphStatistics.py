import os
import shutil
from sys import stdout
from eckity.statistics.statistics import Statistics
import numpy as np
import matplotlib.pyplot as plt


class LiveGraphStatistics(Statistics):
    """
    Concrete Statistics class. Provides statistics about the best fitness, average fitness and worst fitness of every
    subpopulation in some generation. And generate a bar graph where the columns show the index of each sample,
    and the height of the columns represents the fitness given to it in each generation.

    Parameters
    ----------
    max_fitness_to_display: int
        What is the upper limit of the y values to be displayed in the graph

    population_size: int
        How many columns will be displayed in the graph

    save_result: bool
        save the results in a dedicated folder

    format_string: str
        String format of the data to output.
        Value depends on the information the statistics provides.
        For more information, check out the concrete classes who extend this class.

    output_stream: Optional[SupportsWrite[str]], default=stdout
        Output file for the statistics.
        By default, the statistics will be written to stdout.
    """

    def __init__(self, max_fitness_to_display, population_size, save_result, format_string=None, output_stream=stdout):
        # Initialize the save_result, population_size, and max_fitness_to_display instance variables
        self.save_result = save_result
        self.population_size = population_size
        self.max_fitness_to_display = max_fitness_to_display
        # Create a list of integers from 0 to population_size - 1
        self.xim = list(range(0, self.population_size))
        if format_string is None:
            format_string = 'best fitness {}\nworst fitness {}\naverage fitness {}\n'
        # Create a new figure with the title "Live Graph"
        plt.figure('Live Graph')
        # If the Photos directory already exists, delete it
        if os.path.exists('Photos'):
            shutil.rmtree('Photos')
        # If save_result is True, create a new Photos directory
        if save_result:
            os.makedirs('Photos')
        super().__init__(format_string, output_stream)

    def write_statistics(self, sender, data_dict):
        # Extract the generation number from the data dictionary
        gen_num = data_dict["generation_num"]
        # Print the generation number to the output stream
        print(f'generation #{gen_num}', file=self.output_stream)
        # Iterate over the subpopulations in the population
        for index, sub_pop in enumerate(data_dict["population"].sub_populations):
            # Calculate the best, worst, and average fitness values for the current subpopulation
            best = sub_pop.get_best_individual().get_pure_fitness()
            worst = sub_pop.get_worst_individual().get_pure_fitness()
            avg = sub_pop.get_average_fitness()
            # Print the subpopulation number and the best, worst, and average fitness values to the output stream
            print(f'subpopulation #{index}', file=self.output_stream)
            print(self.format_string.format(best, worst, avg), file=self.output_stream)
            # This function create the live graph with all the parameters
            self.live_graph(avg, best, gen_num, sub_pop, worst)

    def live_graph(self, avg, best, gen_num, sub_pop, worst):
        # Create a new figure with the title "Live Graph"
        plt.figure("Live Graph")
        # Create a list of the pure fitness values for each individual in sub_pop
        yim = [i.get_pure_fitness() for i in sub_pop.individuals]
        # This function added titles to the graph
        self.titles(gen_num, best, worst, avg)
        # Set the x-axis tick marks to the values in self.xim
        plt.xticks(np.arange(len(self.xim)), self.xim)
        # Set the y-axis limits to be between 0 and self.max_fitness_to_display
        plt.ylim([0, self.max_fitness_to_display])
        # Sort yim - do it for the colors below
        yim.sort()
        # Create a bar chart using self.xim as the x-values and yim as the y-values
        # The color of each bar is set to "green" if it corresponds to the lowest value in yim, and "red" otherwise
        plt.bar(self.xim, yim, color=["red" if i != yim[0] else "green" for i in yim])
        # Pause the plot for each generation
        plt.pause(max(1 - gen_num / 3, 0.5))
        # If self.save_result is True, save the current figure as an image file in "Photos" directory
        if self.save_result:
            plt.savefig("Photos/" + f'generation #{gen_num}')
        # Clear the current figure
        plt.clf()

    # In each generation we call it for the titles of the live graph
    def titles(self, gen_num, best, worst, avg):
        plt.title(
            f'Generation #{gen_num} \n Best Fitness: %(1).2f - Worst Fitness: %(2).2f - Average Fitness: %(3).2f' % {
                '1': best,
                '2': worst,
                '3': avg},
            fontsize=10)
        plt.ylabel('Fittness')
        plt.xlabel('Samples')

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['output_stream']
        return state

    # Necessary for valid unpickling, since modules cannot be pickled
    def __setstate__(self, state):
        self.__dict__.update(state)
        self.output_stream = stdout
