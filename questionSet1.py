"""
Consider a pair of intergers (a,b). The following operations can be performed on a,b in any order, zero or more times

* (a,b) -> (a+b,b)

*(a,b)-> (a,a+b)

Return a string that denotes whether or not (a,b) can be converted to (c,d) 
by performing the operation zero or more times
"""

def isPossible(a, b, c, d):

    def dfs(a, b):
        if a > c or b > d:
            return False
        if a == c and b == d:
            return True
        l = dfs(a + b, b)
        r = dfs(a, a + b)
        return l or r
    
    return dfs(a, b)

def testIsPossible():
    # trues

    # base case
    print(isPossible(1, 1, 1, 1))
    # one recursive step
    print(isPossible(2,5,7, 5))
    # 2 recursive steps
    print(isPossible(2, 5, 12, 5))
    # 3 recursive step including jump to b
    print(isPossible(2, 5, 12, 17))

    # falses
    print(isPossible(2, 4, 12, 5))
    print(isPossible(2, 2, 3, 4))


"""
The Stocks of a company are being surveyed to analyse the net profit of the company over a period

For an analysis parameter k, an interval of k concutive months is said to be hightly profitable 
if the values of the stock prices are strictly increasing for those months. 
Given the stock prices of the company for n months and the analysis parameter k find the number of highly 
profitable intervals.

Example : stockPrices=[5,3,5,7,8], K=3
Here the answer is 2

"""
def highlyProfitableMonths(stockPrices, k):
    index = 1
    inaRow = 0
    count = 0
    while index < len(stockPrices):
        if stockPrices[index] > stockPrices[index - 1]:
            inaRow += 1
            if inaRow == k - 1:
                count += 1
                inaRow -= 1
        else:
            inaRow = 0
        index += 1
    return count

def testHighlyProfitableMonths():
    # should return 2
    print(highlyProfitableMonths([5,3,5,7,8], 3))

    # should return 3
    print(highlyProfitableMonths([5,3,5,7,8, 9], 3))

    # should return 4
    print(highlyProfitableMonths([1,2,3,4,5,6], 2))


"""
A palindrome reads the same from left to right and right to left, e.g., “mom” is a palindrome. 
You are given a palindrome string that must be modified if possible. 
Your task is to change exactly one character in the string to another character from the range 'a' to 'z'
(both inclusive) so that the string meets the following three conditions:

The new string is lower alphabetically than the initial string.
The new string is the lowest value string alphabetically that can be created from the original 
palindrome after making only one change.
The new string is not a palindrome.
If there is no valid way to modify the palindrome string, return the string “IMPOSSIBLE”.
"""
def breakPallindrome(string):
    manipulated = [s for s in string]
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s"
               "t", "u", "v", "w", "x", "y", "z"]
        
    for letter in letters:
        for x in range(len(string) // 2):
            if manipulated[x] != letter:
                manipulated[x] = letter
                return str(manipulated)
    return "IMPOSSIBLE"

def testBreakPallindrome():
    print(breakPallindrome("mom"))
    print(breakPallindrome("abba"))
    print(breakPallindrome("aaaa"))
    print(breakPallindrome("bbb"))


"""
You are given an array nums of n integers. The array can be reduced by 1 element by performing a move. Each move consists of the following three steps:

Pick two different elements num1 and num2 from the array.
Remove the two selected elements from the array.
Add the sum of the two selected elements to the end of the array.
Each move has a cost associated with it: the sum of the two elements removed from the array during the move. Your task is to calculate the minimum total cost of reducing the array to one element.
"""
import heapq
def minCost(array):
    heapq.heapify(array)
    totalCost = 0

    while len(array) >= 2:
        twoSmallest = heapq.heappop(array) + heapq.heappop(array)
        totalCost += (twoSmallest)
        heapq.heappush(array, twoSmallest)
    return totalCost

def testMinCost():
    print(minCost([1, 2, 3, 4, 5]))
    print(minCost([5, 4, 3, 2, 1]))


"""
Given two strings s and t, s being the original string, and t being a subsequence of s, 
your task is to find the words missing in t (case sensitive) and return them in order.

A subsequence of a string occurs when all letters of the first string (s) occur in the same order 
with the second string (t). The words in the strings are space-delimited.
"""
import collections
# assume that repeat words are possible
def missingWords(s, t):
    missingWords = []
    s += (" ")
    t += (" ")
    someWords = collections.defaultdict(int)
    word = ""
    for char in t:
        if char == " ":
            someWords[word] += 1
            word = ""
        else:
            word += char
    for char in s:
        if char == " ":
            if someWords[word] == 0:
                missingWords.append(word)
            else:
                someWords[word] -= 1
            word = ""
        else:
            word += char
    return missingWords

def testMissingWords():
    sentence1 = "Hello my name is Jonathan and this is a sentence"
    sentence1missing = "Hello Jonathan and this"
    sentence2 = "Hello my Hello my Jonathan and This is"
    sentence2missing = "Hello my Jonathan This is"
    sentence3 = "abc a b a bac a a A A"
    sentence3missing = "abc a A"

    print(missingWords(sentence1, sentence1missing))
    print()
    print(missingWords(sentence2, sentence2missing))
    print()
    print(missingWords(sentence3, sentence3missing))
testMissingWords() 


"""
You are given an array of decimal integers. Rearrange the array according to the following rules:

Sort the integers in ascending order of the number of '1's in their binary representations.
For elements having the same number of '1's, sort them in ascending order of their decimal values.

"""

def binarySort(array):
    decimalToOnes = {}

    def countOnes(decimal):
        binaryStr = bin(decimal)[2:]
        count = binaryStr.count()
        decimalToOnes[decimal] = count
    
    for decimal in array:
        if decimal not in decimalToOnes:
            countOnes(decimal)
    
    # lambda x means each element in the array. It returns decimalToOnes[x]
    sortedArr = sorted(array, key = lambda x : decimalToOnes[x])
    return sortedArr
    
    
        