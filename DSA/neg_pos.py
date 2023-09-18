#Code Written by : John Nixon
#Date: 15:08:2023  Time: 15:26:55
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

pos_arr = []
neg_arr = []

for num in arr:
    if num >= 0:
        pos_arr.append(num)
    else:
        neg_arr.append(num)


arr = pos_arr + neg_arr
print(arr)