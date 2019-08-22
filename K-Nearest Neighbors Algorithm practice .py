#!/usr/bin/env python
# coding: utf-8

# In[1]:


###Function to split data set with splite range variable "splite"
import csv
import random
import math

#function loads the dataset file, "filename",
#and split it into trainingset and testset with splite ration "splite"

def loadSplitDataSet(filename, splite, trainingSet=[], testSet=[]):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        
        #splitting dataset 
        for x in range(len(dataset)-1):  #number of raws of the dataset
            for y in range(4):           #number of columns in the dataset
                dataset[x][y] = float(dataset[x][y])   #change the cell value into float
            if random.random() < splite:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])
    return trainingSet, testSet


#Function that calculate euclidean distance
def euclideanDistance(instance1, instance2, fields):
    distance = 0
    for x in range(fields-1):  #"-1" is because we don't need to iterate till the last field
                               #which is string and doesn't matter for this calculation
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)

###Main Algorithm code 
import operator
def getNeighbors(trainingSet, testInstance, K):
    distances = []
    length = len(testInstance)  #number of fields in the instanceSet

    for x in range(len(trainingSet)):  #get the euclidean dist between isntance and every element in the trainingSet
        dist = euclideanDistance(trainingSet[x], testInstance, length)
        print(dist)
        print(trainingSet[x])
        distances.append((trainingSet[x], dist))  #store distances in list
     
    distances.sort(key=operator.itemgetter(1))  #sort trainingSet according to thier distance from instanceSet
    neighbors = []
    for x in range(k-1):
        neighbors.append(distances[x][0])
    return neighbors                      #as a list


# In[2]:


#test code for the algorithm
trainSet= [[2,2,2,'a'], [4,4,4,'b'], [7,7,7,'c'], [9,9,9,'d'], [1,1,1,'e'], [6,6,6,'f']]
testSet = [5,5,5,'y']
k =3
neighbors = getNeighbors(trainSet, testSet, 2)
print(neighbors)


# In[ ]:




