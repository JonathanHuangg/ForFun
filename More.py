"""
Problem Statement -: Street Lights are installed at every position along a 1-D road of length n. 
Locations[] (an array) represents the coverage limit of these lights.
 The ith light has a coverage limit of locations[i] that can range from the position 
 max((i – locations[i]), 1) to min((i + locations[i]), n ) (Closed intervals). 
 Initially all the lights are switched off. 
 Find the minimum number of fountains that must be switched on to cover the road.

Intervals!
"""

def minStreetLights(arr):
    intervals = []

    for index, num in enumerate(arr):
        intervals.append((max(index - num, 0), min(index + num, len(arr) - 1)))
    intervals.sort(key=lambda x: x[0])

    count = 0
    i = 0
    last_covered = -1
    
    while last_covered < len(arr) - 1:
        max_reach = -1
        while i < len(arr) and intervals[i][0] <= last_covered + 1:
            max_reach = max(max_reach, intervals[i][1])
            i += 1
        
        if max_reach <= last_covered:
            return -1  
        
        last_covered = max_reach
        count += 1
    return count
        

def testMinStreetLights():
    def run_test(arr, expected):
        result = minStreetLights(arr)
        if result == expected:
            print(f"Pass")
        else:
            print(f"Fail: Expected {expected}, but got {result}")

    # Test Case 1
    arr = [1, 2, 1, 3, 2, 1, 1, 1, 1]
    run_test(arr, 2)  # Expected output: 3

    # Test Case 2
    arr = [0, 2, 3]
    run_test(arr, 1)  # Expected output: 1
    
    # Test Case 3
    arr = [0, 0, 0, 0]
    run_test(arr, 4)  # Expected output: -1
    
    # Test Case 4
    arr = [2, 2, 2, 2, 2]
    run_test(arr, 1)  # Expected output: 1
    
    # Test Case 5
    arr = [1, 1, 1, 1, 1]
    run_test(arr, 2)  # Expected output: 3
    
    # Test Case 6
    arr = [1, 0, 1, 0, 1, 0, 1]
    run_test(arr, 4)  # Expected output: 4
    
    # Test Case 7
    arr = [3, 0, 0, 0, 3]
    run_test(arr, 2)  # Expected output: 2
    
    # Test Case 8
    arr = [1, 2, 1, 2, 1, 2, 1, 2, 1]
    run_test(arr, 3)  
    
    # Test Case 9
    arr = [0, 0, 0, 0, 1]
    run_test(arr, 4)  # Expected output: -1
    
    # Test Case 10
    arr = [2, 1, 0, 1, 2]
    run_test(arr, 2)  # Expected output: 2

# Example usage:
testMinStreetLights()
