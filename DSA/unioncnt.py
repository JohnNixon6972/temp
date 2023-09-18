#Code Written by : John Nixon
#Date: 15:08:2023  Time: 15:40:35
#Copyrights are applicable
import sys
import os
sys.setrecursionlimit(10000)
try:
    sys.stdin = open('./input.txt', 'r')
    sys.stdout = open('./output.txt', 'w')
except:
    pass

m,n = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

a = a + b 

ans = len(set(a))
print(ans)
