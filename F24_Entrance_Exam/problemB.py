"""
Problem B: 
https://codeforces.com/group/vVrQkGaspd/contest/551192/problem/B

Run with:
Get-Content problemB.txt | python problemB.py

Expected Output:
0 0
1 2
"""

"""
Notes:

5x6 grid
x = 6
y = 5
"""

def main():
    top, bottom = input(), input()
    rows = [input() for _ in range(5)]
    found = []

    for i in range(4):
        row = rows[i]
        for z in range(6-1):
            if row[z:z+2] == top and rows[i+1][z:z+2] == bottom:
                #print(i, z)
                found.append([i, z])
                    
    for x, y in found:
        print(x, y)

if __name__ == "__main__":
    main()
