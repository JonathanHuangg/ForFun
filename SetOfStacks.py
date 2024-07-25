"""
From the very popular, cracking the coding interview.

Imagine a literal stack of plates. If the stack gets too high, it might topple.
In real life, you would start a new stack when the previous stack exceeds that threshold.
Implement a data structure that mimics this. SetOfStacks should be composed of several stack
and create new stack once previous exceeds capacity
"""

# thoughts
# Feels like a pretty easy 2D array
class SetOfStacks():
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
        self.currStack = []
    
    """
    Assume that you are pushing things that can go into lists. 
    """
    def push(self, item):
        if len(self.currStack) == self.capacity:
            self.resize()
        self.currStack.append(item)

    def resize(self):
        self.stack.append(self.currStack[:])
        self.currStack = []

    def pop(self):
        if not self.stack:
            print("Nothing to pop")
            return
        return self.stack.pop()
    
    def returnAllStacks(self):
        combined = self.stack[:]
        combined.append(self.currStack[:])
        return combined

def NormalTest():
    setOfStacks = SetOfStacks(5)
    setOfStacks.push(5)
    setOfStacks.push(5)
    setOfStacks.push(5)
    setOfStacks.push(5)
    setOfStacks.push(5)
    setOfStacks.push(5)
    x = setOfStacks.returnAllStacks()
    print(x)

def NothingToPopTest():
    setOfStacks = SetOfStacks(5)
    setOfStacks.pop()

   
