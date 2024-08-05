"""
I have a power outage so I can't test the code so I gotta do it manually lol
"""
import heapq
def minCostConnectPointsPrims(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """

    numPoints = len(points)
    totalCost = 0
    visited = set()
    minHeap = [(0, 0)]

    while len(visited) < numPoints:
        cost, pointsIndex = heapq.heappop(minHeap)

        if pointsIndex in visited:
            continue

        visited.add(pointsIndex)
        totalCost += cost

        x2, y2 = points[pointsIndex]

        for nextIndex in range(numPoints):
            if nextIndex not in visited:
                x1, y1 = points[nextIndex]
                dist = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(minHeap, (dist, nextIndex))
    
    return totalCost

class UnionFind():
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = list(range(n))

    def find(self, a):
        if self.parents[a] != a:
            return self.find(self.parents[a])
        return a

    def union(self, a, b):
        parentA = self.find(a)
        parentB = self.find(b)

        if parentA != parentB:
            if self.rank[parentA] > self.rank[parentB]:
                self.parents[parentB] = parentA
            elif self.rank[parentA] < self.rank[parentB]:
                self.parents[parentA] = parentB
            else:
                self.parents[parentA] = parentB
                self.rank[parentB] += 1
            return True
        return False # they are the same
def minCostConnectPointsKrushkals(points):

    edgeList = []
    for index in range(len(points)):
        for index1 in range(index, len(points)):
            x1, y1 = points[index]
            x2, y2 = points[index1]

            dist = abs(x1 - x2) + abs(y1 - y2)
            edgeList.append((dist, index, index1))
    totalSum = 0
    numEdges = 0
    heapq.heapify(edgeList)
    uf = UnionFind(len(points))

    while numEdges != len(points) - 1:
        dist, index, index1 = heapq.heappop(edgeList)
        
        if uf.union(index, index1):
            totalSum += dist
            numEdges += 1
    return totalSum


    
def test():
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    print(minCostConnectPointsPrims(points))
    print(minCostConnectPointsKrushkals(points))
    print()
    points = [[3,12],[-2,5],[-4,1]]
    print(minCostConnectPointsPrims(points))
    print(minCostConnectPointsKrushkals(points))
    print()
    points = [[0,0]]
    print(minCostConnectPointsPrims(points))
    print(minCostConnectPointsKrushkals(points))
    print()
    points = [[2,-3],[-17,-8],[13,8],[-17,-15]]
    print(minCostConnectPointsPrims(points))
    print(minCostConnectPointsKrushkals(points))
    print()
    points = [[-1000000,-1000000],[1000000,1000000]]
    print(minCostConnectPointsPrims(points))
    print(minCostConnectPointsKrushkals(points))
    print()
test()

    


