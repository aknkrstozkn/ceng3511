# starter code for solving knapsack problem using genetic algorithm
import random

fc = open('./c.txt', 'r')
fw = open('./w.txt', 'r')
fv = open('./v.txt', 'r')
fout = open('./out.txt', 'w')


c = int(fc.readline())
w = []
v = []
for line in fw:
    w.append(int(line))
for line in fv:
    v.append(int(line))

print('Capacity :', c)
print('Weight :', w)
print('Value : ', v)

popSize = int(input('Size of population : '))
genNumber = int(input('Max number of generation : '))
print('\nParent Selection\n---------------------------')
print('(1) Roulette-wheel Selection')
print('(2) K-Tournament Selection')
parentSelection = int(input('Which one? '))
k = 0
if parentSelection == 2:
    k = int(input('k=? (between 1 and ' + str(len(w)) + ') '))

print('\nN-point Crossover\n---------------------------')
n = int(input('n=? (between 1 and ' + str(len(w) - 1) + ') '))

print('\nMutation Probability\n---------------------------')
mutProb = float(input('prob=? (between 0 and 1) '))

print('\nSurvival Selection\n---------------------------')
print('(1) Age-based Selection')
print('(2) Fitness-based Selection')
survivalSelection = int(input('Which one? '))
elitism = bool(input('Elitism? (Y or N) '))


print('\n----------------------------------------------------------')
print('initalizing population...')
old_population = []
for i in range(popSize):
    temp = []
    for j in range(len(w)):
        temp.append(random.randint(0, 1))
    old_population.append(temp)


print('evaluating fitnesses...')
ft = 0
wt = 0
population = {}
for i, chrom in enumerate(old_population):
    ft = 0
    wt = 0
    for j, gene in enumerate(chrom):
        ft += gene * int(v[j])
        wt += gene * int(w[j])
    population[chrom] = ft
    print(i + 1, chrom, ft, wt)
##################################################################

####---Selection---#####

def roulette_wheel_selection():
    max = sum([int(population[chrom]) for chrom in population])
    pick = random.uniform(0, max)
    current = 0
    for chromosome in population:
        current += population[chromosome]
        if current > pick:
            return chromosome

def k_tournament_selection():
    best_c = []
    best_ft = 0
    for i in range(0, k):
        initial_c = random.choice(list(population.keys()))
        random_ft = population[initial_c]
        if random_ft > best_ft:
            best_ft = random_ft
            best_c = initial_c
    return best_c


fout.write('chromosome: 101010111000011\n')
fout.write('weight: 749\n')
fout.write('value: 1458')
fout.close() 
