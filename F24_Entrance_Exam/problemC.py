"""
Problem C: 
https://codeforces.com/group/vVrQkGaspd/contest/551192/problem/C

Run with:
Get-Content problemC.txt | python problemC.py

Expected Output:
1
"""

"""
Notes:
Case 1: First difference is valid.
    Return first invalid
Case 2: First difference is invalid.
"""

def main():
    stepCount = int(input())
    steps = [int(input()) for _ in range(stepCount)]

    firstDiff = steps[1]-steps[0]
    secondDiff = steps[2] - steps[1]
    
    if firstDiff == secondDiff:
        for i in range(3, len(steps)):
            if steps[i]-steps[i-1] != firstDiff:
                print(i+1)
                break
                # return
    else:
        # first Diff no match second diff is off, must return 0, 1, or 2.
        # We know step3 is correct
        thirdDiff = steps[3]-steps[2] # must be correct
        if thirdDiff == secondDiff:
            print(1)
        # either 1 or 2, 0 is right
        else:
            diff = (steps[3]-steps[0]) / 3
            if steps[0] + diff == steps[1]:
                print(3)
            else:
                print(2)

    
    #print(steps)
    #print("Number of steps:", stepCount)

if __name__ == "__main__":
    main()