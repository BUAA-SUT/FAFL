import operator
import math
from decimal import *
import random
random.seed(1)


class Mutant1:

    def __init__(self):
        # Configuration
        self.trainingSet = []
        self.testSet = []
        self.accuracy = 0
        self.k = 3
        self.default_label = "Iris-setosa"

    def setDefaultLabelabel(self, default_label):
        self.default_label = default_label

    def printInfo(self):
        print('Accuracy: ' + repr(self.accuracy) + '%')

    def setInput(self, trainingSet, testSet):
        self.trainingSet = trainingSet
        self.testSet = testSet

    def euclideanDistance(self, instance1, instance2, length):
        distance = 0
        for x in range(length):
            distance += pow((Decimal(instance1[x]) + Decimal(instance2[x])), 2)  # - ---> +
        return math.sqrt(distance)

    def getNeighbors(self, testInstance):
        distances = []
        length = len(testInstance) - 1
        for x in range(len(self.trainingSet)):
            dist = self.euclideanDistance(testInstance, self.trainingSet[x], length)
            distances.append((self.trainingSet[x], dist))
        distances.sort(key=operator.itemgetter(1))
        neighbors = []
        for x in range(self.k):
            neighbors.append(distances[x][0])
        return neighbors

    def getResponse(self, neighbors):
        classVotes = {}
        for x in range(len(neighbors)):
            response = neighbors[x][-1]
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
        if sortedVotes[0][1] == 1:
            return self.default_label
        else:
            return sortedVotes[0][0]

    def getPredications(self):
        predictions = []
        for x in range(len(self.testSet)):
            neighbors = self.getNeighbors(self.testSet[x])
            result = self.getResponse(neighbors)
            predictions.append(result)
        return predictions

