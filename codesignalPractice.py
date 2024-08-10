"""
Given an array a, your task is to output an array b of the same length by applying the 
following transformation: 
– For each i from 0 to a.length - 1 inclusive, b[i] = a[i - 1] + a[i] + a[i + 1]
– If an element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, use 0 in its place
– For instance, b[0] = 0 + a[0] + a[1]

"""

def arrays(a):
    b = [0] * len(a)

    for index in range(len(a)):
        b[index] += a[index]
        if index + 1 != len(a):
            b[index] += a[index + 1]
        if index - 1 >= 0:
            b[index] += a[index - 1]

    return b

def TestArrays():
    a = [4, 0, 1, -2, 3]
    b = arrays(a)
    print(b)


"""
You are given two strings: pattern and source. 
The first string pattern contains only the symbols 0 and 1, 
and the second string source contains only lowercase English letters.

Your task is to calculate the number of substrings of source that match pattern. 

We’ll say that a substring source[l..r] matches pattern if the following three conditions are met:
– The pattern and substring are equal in length.
– Where there is a 0 in the pattern, there is a vowel in the substring. 
– Where there is a 1 in the pattern, there is a consonant in the substring. 

Vowels are ‘a‘, ‘e‘, ‘i‘, ‘o‘, ‘u‘, and ‘y‘. All other letters are consonants.
"""

# there does not seem to be a o(n) approac
import collections
def strings(pattern, source):

    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

    def checkMatch(window):
        for index, item in enumerate(window):
            if (pattern[index] == "1" and item in vowels) or (pattern[index] == "0" and item not in vowels):
                return False
        return True
    count = 0
    
    window = collections.deque()
    for index in range(len(pattern)):
        window.append(source[index])

    if checkMatch(window):
        count += 1

    for index in range(len(window), len(source)):
        window.popleft()
        window.append(source[index])
        if checkMatch(window):
            count += 1
    return count

def TestStrings():
    pattern = "010"
    source = "amazing"
    count = strings(pattern, source)
    print(count)

"""
Given an array of unique integers numbers, your task is to find the number of pairs of indices (i, j) 
such that i ≤ j and the sum numbers[i] + numbers[j] is equal to some power of 2.
"""

def LookupTable(arr):
    largest = max(arr)
    largestPossible = largest * 2

    powers = set()

    i = 0
    while (1 << i) <= largestPossible:
        powers.add(1 << i)
        i += 1
    
    findNumbers = collections.defaultdict(int)
    count = 0
    for item in arr:
        for power in powers:
            need = power - item
            findNumbers[need] += 1
        if item in findNumbers:
            count += findNumbers[item]
    return count

def TestLookupTable():
    arr = [1, -1, 2, 3]
    print(LookupTable(arr))

    arr = [-2, -1, 0, 1, 2]
    print(LookupTable(arr))


"""
You are given a matrix of integers field of size height × width representing a game field, 
and also a matrix of integers figure of size 3 × 3 representing a figure. 
Both matrices contain only 0s and 1s, where 1 means that the cell is occupied, 
and 0 means that the cell is free.

You choose a position at the top of the game field where you put the figure and then drop it down. 
The figure falls down until it either reaches the ground (bottom of the field) or lands on an occupied cell, 
which blocks it from falling further. After the figure has stopped falling, some of the rows in the field may 
become fully occupied.

Gave up
"""

def fallingTetris(field, figure):
    numCols = len(field)
    numRows = len(field[0])

    for dropColumn in range(0, numCols - 2):
        # get the first row hit
        
        hitOne = False
        while not hitOne:
            # if rowContinue == 
            rowContinue = 2 # bottom-most 3 x 3
            
            for hitColumn in range(dropColumn, dropColumn + 3):
                if figure[rowContinue][hitColumn % 3] == 1:
                    return -1
            
            #rowContinue += 1

"""
given an array of numbers, count the number of combinations that sum to a certain number
"""

def countCombinations(arr, target):
    def dfs(index, currTotal):
        if currTotal == target:
            return 1
        elif index == len(arr):
            return 0

        return dfs(index + 1, currTotal) + dfs(index + 1, currTotal + arr[index])
    
    return dfs(0, 0)

# new restriction: list them
def countCombinationsArr(arr, target):
    final = []
    def dfs(index, currArr, currTotal):
        if currTotal == target:
            final.append(currArr[:])
            return
        elif index == len(arr):
            return 

        currArr.append(arr[index])
        dfs(index + 1, currArr, currTotal + arr[index])
        currArr.pop()
        dfs(index + 1, currArr, currTotal)

    dfs(0, [], 0)
    return final

# new restriction: must be of length 3

def countCombinations3(arr, target):
    final = []

    def dfs(index, currArr, currTotal):
        if len(currArr) == 3:
            if currTotal == target:
                final.append(currArr[:])    
            return
        elif index == len(arr):
            return
        currArr.append(arr[index])
        dfs(index + 1, currArr, currTotal + arr[index])
        currArr.pop()
        dfs(index + 1, currArr, currTotal)

    dfs(0, [], 0)
    return final

def testCountCombinations():
    arr = [4, 5, 6, 4, 2, 1, 1]
    target = 6
    print(countCombinations(arr, target))
    print()
    print(countCombinationsArr(arr, target))
    print()
    print(countCombinations3(arr, target))

testCountCombinations()
