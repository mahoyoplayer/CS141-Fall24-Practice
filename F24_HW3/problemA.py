"""
Problem X: 


Run with:
Get-Content problemA.txt | python problemA.py

Expected Output:
?
"""

from sys import stdin, stdout 
from typing import List

# This problem needs a heap
from heapq import heapify, heappop, heappush

def getInt() -> int:
    return int(stdin.readline())

def getInts() -> List[int]:
    return [int(s) for s in stdin.readline().split()]

def getStr() -> str:
    return stdin.readline()

def getStrs() -> str:
    return stdin.readline().split()

def main():
    bagCount = getInt()
    heap = []
    for _ in range(bagCount):
        heap.append(getInt())

    heapify(heap)
    totalCounts = 0
    while len(heap) > 1:
        bag1, bag2 = heappop(heap), heappop(heap)
        newBag = bag1 + bag2
        totalCounts += 2 * newBag
        heappush(heap, newBag)


    print(totalCounts)
    #stdout.write("Hello World")

if __name__ == "__main__":
    main()

