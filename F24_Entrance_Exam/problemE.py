"""
Problem C: 
https://codeforces.com/group/vVrQkGaspd/contest/551192/problem/C

Run with:
Get-Content problemE.txt | python problemE.py

Expected Output:
1
"""

from collections import deque
from re import I, L

def convertTile(tile):
    x = ord(tile[0]) - ord("a")
    y = ord(tile[1]) - ord("1")
    #print(x, y)
    return (x, y)

def main():
    # walrus operator
    board = 1
    directions = [
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1),
        (1, 2),
        (1, -2),
        (-1, 2),
        (-1, -2)
    ]
    valid = lambda x, y: 0 <= x < 8 and 0 <= y < 8

    while True:
        banCount = int(input())
        if banCount == -1: return

        # set up bans
        bans = set()

        s = input().split()
        for ban in s:
            bans.add(convertTile(ban))

        # set up start and ends
        s = input().split(" ")
        start, target = convertTile(s[0]), convertTile(s[1])
        

        q = deque( [[start[0], start[1], 0]])
        found = False
        visited = {start}

        while q:
            x, y, moveCount = q.popleft()
            if x == target[0] and y == target[1]:
                print(f"Board {board}: {moveCount} moves")
                found = True
                break
            for deltaX, deltaY in directions:
                newX, newY = x + deltaX, y + deltaY
                if valid(newX, newY) and (newX, newY) not in bans and (newX, newY) not in visited:
                    q.append([newX, newY, moveCount + 1])
                    visited.add((newX, newY))

        if not found:
            print(f"Board {board}: not reachable")
        board += 1


if __name__ == "__main__":
    main()