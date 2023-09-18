#Code Written by : John Nixon
#Date: 15:08:2023  Time: 15:48:47
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

tmp = arr[-1]
for i in range(n-1,-1,-1):
    arr[i] = arr[i-1]

arr[0] = tmp 
print(arr)