#Code Written by : John Nixon
#Date: 15:08:2023  Time: 14:30:14
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
arr =list(map(int,input().split()))
k = int(input())

new_Arr = list(set(arr))
print(new_Arr)
print(new_Arr[k-1])
    # print(new_arr)

