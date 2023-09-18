#Code Written by : John Nixon
#Date: 08:09:2023  Time: 07:39:13
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

tri = []

for i in range(n):
    col = []
    for j in range(i):
        if j == 0 or j == i-1:
            col.append(1)

        elif i > 1:
            val = tri[i-1][j-1] + tri[i-1][j]
            col.append(val)
        
    tri.append(col)

tri.pop(0)
print(tri)

# binary search
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid-1, x)
        else:
            return binary_search(arr, mid+1, high, x)
    else:
        return -1
