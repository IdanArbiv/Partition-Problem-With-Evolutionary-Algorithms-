# Evolutionary-Algorithms-Partition-Problem
## Introduction 
This project contains 2 main parts:
1. Solving the partition problem by using an evolutionary algorithm and using the EC_KITY library.
2. Added a new feature to the EC-KITY library: Live graph

## The partition problem
Partition problem is to determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is the same. 
The partition problem is NP-complete.
In our project we solve the Partition problem with Genetic Algorithm (GA), using EC-KitY, written in python.
In addition, we have added virtualization in a bar graph that can be added as a supplement to the existing EC-KitY.

<p align="center">
  <img src="https://user-images.githubusercontent.com/79116144/210153158-ca6a1f4a-968e-42b9-b13e-aea0d458ab38.png" alt="image">
</p>

Partition problem in our implementation:

As input to the problem we randomly generate a group of numbers that will be in an array. We chose to represent the group as an array of the same size as the input array with zeros and ones Each element in the array in position i that contains the digit 0 signifies that the element in the input array in position i is in one group, and each element in the array in position j that contains the digit 1 signifies that the element in the input array in position j is in the other group.

## Dependencies
- Matplotlib
- EC-KitY

For the basic evolution mode, EC-KitY requires:

- numpy (>=1.14.6)
- pandas (>=0.25.0)
- overrides (>= 6.1.0)

For sklearn mode, EC-KitY additionally requires:
- scikit-learn (>=0.24.2)

## Methods
#### Main.py:
In this file we initialized all the details required to send our problem to the EC-KitY tool. 

#### LiveGraphStatistics.py:
- write statistics - provides statistics about the best fitness, average fitness and worst fitness of every subpopulation in some generation and print it in the console.
- live_graph - show the results of the statistics in a graph and also save the results of the graph in a folder if you want.

#### PartitionEvaluator.py:
- init - In this function we initialized the input array for the problem, with random numbers.
- evaluate_individual – This function checks according to the arrays, the sum of the numbers in the two groups and returns as a fitness value - the absolute value of the subtraction between the sums of the two groups.

## Representation

We will represent the problem using row vectors.

Phenotype will be a division of the input into 2 foreign groups

Genotype will be a vector whose length is the length of the input vector with possible values of 0,1. If the member in the i-th place gets the value 1, the member in the i-th place in the input vector will belong to the group "1", and if the member in the i-th place gets the value 0, the member in the i-th place in the input vector will belong to the "0" group (The order is not important)

<p align="center">
  <img src="https://user-images.githubusercontent.com/79116144/210153233-9db880e4-0bbd-4ca7-9b56-787d22a5b747.png" alt="image">
</p>

## Fitness

Our goal in this program is to minimize the difference between the sum of the foreign groups in the division of the input vector. Therefore, we will define the fitness of each individual and consider it in the following way:
The sum of the values of group "1" minus the sum of the values of group "0" in absolute value.
We will do this by going over the cells of the individual's representation vector and if the i-th cell value is "0" the i-th cell value in the input vector will be added to the group sum "0" and likewise for a cell whose value is "1".

<p align="center">
  <img src="https://user-images.githubusercontent.com/79116144/210153261-eca094d7-ec33-45df-b69b-8601f29941a1.png" alt="image">
</p>

## Selection Method – 

We tested both elitism selection and tournament selection and got better results in Tournament Selection:

Elitist selection is a selection strategy where a limited number of individuals with the best fitness values are chosen to pass to the next generation, avoiding the crossover and mutation operators. Elitism prevents the random destruction by crossover or mutation operators of individuals with good genetics. On the other hand,"Tournament Selection" does not prevents the random destruction by crossover or mutation operators of individuals and as a result sometimes yielded better results.

Tournament selection also has several benefits over alternative selection methods for genetic algorithms: it is efficient to code, works on parallel architectures and allows the selection pressure to be easily adjusted.


## Experimental setup

 1. Installing all the dependencies (EC-KITY - https://github.com/EC-KitY/EC-KitY)
 2. Extract the files to the project folder
 3. Under the PartitionEvaluator class set the constants of the program. (more in 'short usage tutorial').

## Live Graph Feature -
We have added a new feature to the EC-KITY library.
This feature is given in the "LiveGraphStatistics" class.

#### Purpose: 
Allow the user to view live the algorithm's statistics in a visual way.

#### The graph: 
Is a bar graph where the columns show the index of each sample, and the height of the columns represents the fitness given to it in each generation.
In the live graph, you can see live while the algorithm is running the variation of the finesses of the samples depending on the generation. The graph also shows the generation number, the maximum, minimum and average fitness in each generation. In addition, the graph will interactively mark the column with the maximum fitness in each iteration of the algorithm. 

#### Arguments:
- max_fitness_to_display (int): What is the upper limit of the y values to be displayed
- population_size (int): How many columns will be displayed in the graph
- save_result (bool) :save the results in a dedicated folder

#### Results:
If the 'save_result' argument receives the value true, for each run of the program, the results of the program will be saved as images in a dedicated folder that will be created in the project folder.

<p align="center">
  <img src="https://user-images.githubusercontent.com/79116144/210181634-8cec9c22-009a-4519-a6e6-03431fb4d8ed.gif" alt="animation">
</p>

## Short usage tutorial  - 

PartitionEvaluator – define the constants the algorithm will use:
- NUM_ITEMS :  The length of the program's input vector
- POPULATION_SIZE : The number of individuals in each subpopulation.
- ELITISM_RATE : What percentage of the sub-population's individuals should be kept as elites for the next generation.
- CROSSOVER_PROB : The probability to execute crossover on random vector.
- CROSSOVER_CELL_NUM : How many cells to perform the crossover
- MUTATION_PROB : The probability to execute mutation on random vector.
- MAX_GENERATION : How many generation the algorithm will operate.
- ONLY_INT_NUMS : True if the input vector contains only integers
- RANDOM_UPPER_BOUND : The maximum value that the input vector will contain.
- RANDOM_LOWER_BOUND : The minimum value that the input vector will contain.
- SAVE_RESULT : If we want to save the photos of the generations.

Default : 

![image](https://user-images.githubusercontent.com/79116144/210181656-5cfe8756-de7a-43c0-a2f9-166bfc924410.png)

Main – explanation:
- creators :  Define which data structure to use and how many items in the main group. In our algorithm – GA bit string vector.
- population_size : The number of individuals in each subpopulation.
- evaluator : User-defined fitness evaluation method.
- higher_is_better : false. In our algorithm it’s a minimize problem – absolute subtraction of the values between 2 groups, smaller fitness is better.
- elitism_rate : What percentage of the sub-population's individuals should be kept as elites for the next generation.
- operators_sequence : genetic operators sequence to be applied in each generation. In our algorithm its VectorKPointsCrossover and BitStringVectorFlipMutation.
- selection_methods : In out algorithm we used tournament selection - tournament between individuals and the winner is the one with the lowest fitness and it continues to the next generation.
- breeder : The simple breeder - Responsible for the execution of genetic operators and selection in each generation.
- max_workers : we want just one worker node for the executor object that evaluates the fitness of the individuals.
- max_genertaion : how many generation.
- statistics : we called to a method that generate our statistics and create the graph that we present.

## Results – 
In this part we wanted to test the algorithm for solving a difficult partition problem and to test the influence of the variables of the problem on the time of finding the optimal solution. In this part we examined the algorithm that solves the partition problem so that each time we changed a different parameter and examined the extent of its effect on the results.

The specific problem we will work on - an array with 10,000 elements, so the elements in the array are integers between 0 and 100,000. The algorithm needs to find a division into 2 foreign groups so that the sum of the members in one group minus the sum of the members in the other group in absolute value will be minimal. In particular, in this problem it is possible to reach fitness 0. In this part we set the seed of the random to be 1 in order to get the same vector with the same values every time.

Description of the experiments - a set of constant control variables were used so that each time we tested the influence of a different parameter on the running time and left the rest of the parameters as constant.
The running time in each experiment is determined to be the time needed for the algorithm to find an optimal solution – i.e. 0, or until it performs a maximum of 45 minutes of running.

The control variables we used:

![image](https://user-images.githubusercontent.com/79116144/210181675-6b4a3480-0ea2-499d-b0b1-694994e84fc1.png)

<p align="center">
  <img src="https://user-images.githubusercontent.com/79116144/210181681-062db94e-3b84-49a7-a5e0-36b685fa0cb2.png" alt="image">
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/79116144/210181698-610bd0d3-49cd-4aee-9232-898bfc4818f0.png" alt="image">
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/79116144/210181705-04c1ac40-236b-4728-9a05-25a448f56407.png" alt="image">
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/79116144/210181708-8abf3bb6-cced-4dbd-aec1-24255778a25b.png" alt="image">
</p>


## Conclusions -

#### population size:
In this parameter there is a trade-off between the running time needed to calculate each iteration in the run, the running time of each generation increases, against the iteration in which the optimal solution is found. In the experiment we discovered that the algorithm finds the optimal solution faster as we increase the population size. Although the running time of each iteration increases significantly, the total time needed to find the optimal solution is small depending on the population size.

#### crossover probability:
This parameter defines the probability we want to perform a crossover operation on the array. The crossover operation is usually sometimes creates better results for us in the next generation, but on the other hand, if we perform the operation with too high probability, we can also lose good results. In the experiment we performed, we see that as we increase the probability of crossover operation, the running time decreases until a probability of 0.7 and from there the running time increases. However, the change in running time is not significant enough after a probability of 0.5.

#### crossover cell number:
This parameter defines on how many cells to perform the crossover when this operation is performed. We can assume that when the amount of cells on which this operation is performed is too small depending on the size of the input, the changes that are made are not significant enough. But if we increase the number of cells to be too large, we may lose good results. As we can see in the graph we received, when we increase the number of cells, we get a significant improvement in the running time up to 500 where the parameter is optimal

#### mutation probability:
This parameter defines the probability of performing a mutation operation on the vector. As we learned, mutation can in some cases produce new results with lower fitness, but in many cases can also be harmful and to produce results with bigger fitness. As we can see in the graph, when the probability is between 0 and 0.3 we get good running times, but as we keep increasing the probability, the running time increases significantly
