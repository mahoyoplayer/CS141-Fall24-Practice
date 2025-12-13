"""
Problem A: 
https://codeforces.com/group/vVrQkGaspd/contest/551192/problem/A

Run with:
Get-Content problemA.txt | python problemA.py

Expected Output:
5
"""

def main():
    swaps = int(input())

    # target doll starts at index 2
    currLoc = 3
    for _ in range(swaps):
        a, b = [int(x) for x in input().split(" ")]
        if a == currLoc:
            currLoc = b
        elif b == currLoc:
            currLoc = a
    print(currLoc)


if __name__ == "__main__":
    main()