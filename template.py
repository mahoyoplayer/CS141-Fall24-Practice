"""
Problem X: 


Run with:
Get-Content problemX.txt | python problemX.py

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
    stdout.write("Hello World")

if __name__ == "__main__":
    main()

