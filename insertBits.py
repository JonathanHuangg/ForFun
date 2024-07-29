"""
You are given 2 32 bit numbers, N and M, and 2 bit positions,
i and j. Write a method to insert M into N such that M starts
at bit j and ends at bit i.

Example: N = 10000000000, 
         M = 10011
         i = 2, j = 6
        output: 10001001100
"""

def insertBitString(N, M, i, j):
    # all ones
    ones = ~0

    # 1110000000 (fills zeros from 0-j)
    leftMask = ones << (j + 1)
                            #1110000000

    # fills up to i with ones 000000011 
    rightMask = (1 << i) - 1

    mask = leftMask | rightMask
    clearN = mask & N
    shiftedM = M << i

    return clearN | shiftedM


def testOutput():

    answer = insertBitString(0b10000000000, 0b10011, 2, 6)

    return answer == 0b10001001100

print(testOutput())