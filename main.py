# Import our packages
import random
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn")
from scipy import stats
import math

# initialize the class
random.seed(0)
class NewClass:
    def __init__(self, RandomNumber = np.random.randint(low=1, high=100, size=20)): # Generate Random Integers Between 1 and 100
        self.RandomNumber = RandomNumber
        
# return the max value in the list 
    def Max(self):
        return max(self.RandomNumber)
    pass

# return the min value in the list 
    def Min(self):
        return min(self.RandomNumber)
    pass

# return the max value squared 
    def MaxSquared(self):
         return max(self.RandomNumber)**0.5
    pass

# return lenght in the list 
    def lenght(self):
        return len(self.RandomNumber)
    pass

# return the sum of all positive numbers only
    def SumPositiveNumber(self):
        sum = 0
        for x in self.RandomNumber:
            if x >= 0:
                sum += x
        return sum
    
 # return the count of all negative numbers
    def count_negative(self):
        neg_count = 0
        for x in self.RandomNumber:
            if x <= 0:
                neg_count += 1
        print("Negative numbers in the list: ", neg_count)
 # return the squart root of all numbers in the lest

    def Squar(self):
        return (self.RandomNumber)**0.5
    pass

# return the mean of the list 

    def mean(self):
        return sum(self.RandomNumber)/len(self.RandomNumber)
    
if __name__ == "__main__":
    NewClass()
        
        

 
