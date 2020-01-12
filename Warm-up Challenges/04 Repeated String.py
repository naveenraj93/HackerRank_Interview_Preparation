# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

output = 0
s = input()
n = int(input())

toBeMultipliedBy = (n  // len(s))
countOfAinInput = s.count('a')

output = toBeMultipliedBy * countOfAinInput

if (toBeMultipliedBy * len(s)) != n:
    remainingChar = n - (toBeMultipliedBy * len(s))
    output += s[:remainingChar].count('a')

print(output)
