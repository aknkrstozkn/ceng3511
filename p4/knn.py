# k-nearest neighbors on the Iris Flowers Dataset
from random import seed
import os
from random import randrange
from csv import reader
from math import sqrt
import matplotlib.pyplot as plt

# Load a CSV file
def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        next(file)
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset

# Convert string column to float
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

# Convert string column to integer
def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
    for row in dataset:
        row[column] = lookup[row[column]]
    return lookup

# Find the min and max values for each column
def dataset_minmax(dataset):
    minmax = list()
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        value_min = min(col_values)
        value_max = max(col_values)
        minmax.append([value_min, value_max])
    return minmax

# Rescale dataset columns to the range 0-1
def normalize_dataset(dataset, minmax):
    for row in dataset:
        for i in range(len(row)):
            row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])

# Split a dataset into k folds
def cross_validation_split(dataset, n_folds):
    dataset_split = list()
    dataset_copy = list(dataset)
    fold_size = int(len(dataset) / n_folds)
    for _ in range(n_folds):
        fold = list()
        while len(fold) < fold_size:
            index = randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        dataset_split.append(fold)
    return dataset_split

# Calculate accuracy percentage
def accuracy_metric(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / float(len(actual)) * 100.0

# Evaluate an algorithm using a cross validation split
def evaluate_algorithm(train_data, test_data, algorithm, *args):
   
    scores = list()
    predicted = algorithm(train_data, test_data, *args)
    actual = [test[-1] for test in test_data]
    accuracy = accuracy_metric(actual, predicted)
    scores.append(accuracy)
    return scores

# Calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1)-1):
        distance += (row1[i] - row2[i])**2
    return sqrt(distance)

# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    for train_row in train:
        dist = euclidean_distance(test_row, train_row)
        distances.append((train_row, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors

# Make a prediction with neighbors
def predict_classification(train, test_row, num_neighbors):
    neighbors = get_neighbors(train, test_row, num_neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction

# kNN Algorithm
def k_nearest_neighbors(train, test, num_neighbors):
    predictions = list()
    for row in test:
        output = predict_classification(train, row, num_neighbors)
        predictions.append(output)
    return(predictions)

# Test the kNN on the Iris Flowers dataset
seed(1)
filename = 'train.txt'
test_file_name = 'test.txt'
dataset = load_csv(filename)
test_data = load_csv(test_file_name)
for i in range(len(dataset[0])-1):
    str_column_to_float(dataset, i)
# convert class column to integers
str_column_to_int(dataset, len(dataset[0])-1)
# evaluate algorithm
for i in range(len(test_data[0])-1):
    str_column_to_float(test_data, i)
# convert class column to integers
str_column_to_int(test_data, len(test_data[0])-1)
# evaluate algorithm

n_folds = 5
num_neighbors = 1
k_range = []
all_scores = []
for num_neigh in range(1,26):
    k_range.append(num_neigh)
    all_scores.append(evaluate_algorithm(dataset, test_data, k_nearest_neighbors, num_neigh)[0])
    print('Loading %' + str(int(int(num_neigh) * 4)))

#asda 
#%matplotlib inline

# plot the relationship between K and testing accuracy
# plt.plot(x_axis, y_axis)
print(all_scores)

f = plt.figure()
plt.plot(k_range, all_scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Testing Accuracy')
strFile = "plot.pdf"
if os.path.isfile(strFile):
   os.remove(strFile)   # Opt.: os.system("rm "+strFile)
f.savefig(strFile, bbox_inches='tight')
plt.close()