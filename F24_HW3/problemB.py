"""
Problem X: 


Run with:
Get-Content problemB.txt | python problemB.py

Expected Output:
?
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
    weightBudget, itemCount = getInts()
    itemArr = []
    for _ in range(itemCount):
        weight, value = getInts()
        itemArr.append((weight, value))
    #print(itemArr)
    highestValue = 0
    """
    buying most value-efficient doesn't work
    """
    
    memo = {}
    def dfs(budget, index):
        if index >= itemCount: return 0
        if budget <= 0: return 0
        if (budget, index) in memo:
            return memo[(budget, index)]

        weight, value = itemArr[index][0], itemArr[index][1]

        buy, noBuy = 0, dfs(budget, index + 1)

        # Buy
        if budget - weight >= 0:
            buy = value + dfs(budget - weight, index + 1)
        res = max(buy, noBuy)
        memo[(budget, index)] = res
        return res

    print(dfs(weightBudget, 0))

    #print(weightBudget, itemCount)

    #print(highestValue)
    #stdout.write("Hello World")

if __name__ == "__main__":
    main()

