"""
Problem D: 
https://codeforces.com/group/vVrQkGaspd/contest/551192/problem/D

Run with:
Get-Content problemD.txt | python problemD.py

Expected Output:
1 3
5 2
100 2
2000 1
"""

def main():
    cardDict = {}
    for _ in range(int(input())):
        card = int(input())
        if card in cardDict:
            cardDict[card] += 1
        else:
            cardDict[card] = 1

    for card in sorted(cardDict):
        print(card, cardDict[card])

    return 0

if __name__ == "__main__":
    main()
