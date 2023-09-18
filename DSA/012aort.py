#Code Written by : John Nixon
#Date: 15:08:2023  Time: 15:10:26
#Copyrights are applicable
import sys
import os
sys.setrecursionlimit(10000)
try:
    sys.stdin = open('./input.txt', 'r')
    sys.stdout = open('./output.txt', 'w')
except:
    pass

arr_0 = []
arr_1 = []
arr_2 = []

n = int(input())
arr = list(map(int,input().split()))

# for num in arr:
#     if num == 1:
#         arr_1.append(num)
#     elif