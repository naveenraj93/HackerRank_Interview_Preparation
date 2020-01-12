# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

total_number,list_of_socks = input(), Counter(input().split())
print( sum([ list_of_socks[key]//2 for key in list_of_socks]))