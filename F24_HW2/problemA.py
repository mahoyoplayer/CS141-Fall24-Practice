"""
Problem A: 
https://codeforces.com/group/vVrQkGaspd/contest/552084/problem/A

Run with:
Get-Content problemA.txt | python problemA.py

Expected Output:
1391
"""

from sys import stdin, stdout 
from typing import List

def getInt() -> int:
    return int(stdin.readline())

def getInts() -> List[int]:
    return [int(s) for s in stdin.readline().split()]

def getStr() -> str:
    return stdin.readline()

def getStrs() -> str:
    return stdin.readline().split()

def main():
    intCount = getInt()
    arr = []
    for _ in range(intCount):
        arr.append(getInt())
    #arr = [2,2,3,3,4,4,1,1]
    
    def mergeSort(l, r):
        if l==r:
            return (arr[l], arr[l], 0)

        mid= (l+r)//2
        min1, max1, c1 = mergeSort(l, mid)
        min2, max2, c2 = mergeSort(mid+1, r)
        totalMin, totalMax = min(min1, min2), max(max1, max2)
        return (totalMin, totalMax, totalMax - totalMin + c1 + c2)

    stdout.write(str(mergeSort(0, len(arr)-1)   [-1]))

if __name__ == "__main__":
    main()





