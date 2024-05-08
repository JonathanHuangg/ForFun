# This is based off a question given from my cousin where you have to sort an input based on 1) the number of circles in the number and 
# 2), the number itself

import random

def generateArr(size):


    mu = 1000
    stdev = 250

    arr = [0] * size

    for index in range(size):
        arr[index] = int(random.normalvariate(mu, stdev))

    return arr

def parse(arr):
    for item in arr:
        print(item)

def zeroSort(input):
               #0  1  2  3  4  5  6  7  8  9
    numZeros = [1, 0, 0, 0, 1, 0, 1, 0, 2, 1]

    def process(input):
        
        num = 0
        for char in str(input):
            num += numZeros[int(char)]
        return num

    input.sort(key = lambda number : (process(number), number))
    return input

def main():
    inputSize = 100
    parse(zeroSort(generateArr(inputSize)))

main()