#Code Written by : John Nixon
#Date: 15:08:2023  Time: 12:32:38
#Copyrights are applicable
import sys
import os
sys.setrecursionlimit(10000)
try:
    sys.stdin = open('./input.txt', 'r')
    sys.stdout = open('./output.txt', 'w')
except:
    pass


n = int(input())
arr = list(map(int,input().split()))

min = sys.maxsize
max = 0

for num in arr:
    if num > max:
        max = num 
    if num < min:
        min = num

print(min,max)