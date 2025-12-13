"""
Problem C: 
https://codeforces.com/group/vVrQkGaspd/contest/551192/problem/C

Run with:
Get-Content problemC.txt | python problemC.py

Expected Output:
0 0
1 2
"""

"""
Notes:
"""

def main():
    stepCount = int(input())
    steps = [int(input()) for _ in range(stepCount)]
    for i in range(stepCount):

    
    print(steps)
    print("Number of steps:", stepCount)

if __name__ == "__main__":
    main()