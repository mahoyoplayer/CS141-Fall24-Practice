"""
Problem B: 
https://codeforces.com/group/vVrQkGaspd/contest/552084/problem/B

Run with:
Get-Content problemB.txt | python problemB.py

Expected Output:
7
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
    money, itemCount = getInts()

    itemPrices = getInts()
    itemPrices.sort()
    
    bought = 0
    for price in itemPrices:
        if money >= price:
            money -= price
            bought += 1
        else:
            break

    stdout.write(str(bought))

if __name__ == "__main__":
    main()





