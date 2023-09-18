#Code Written by : John Nixon
#Date: 15:08:2023  Time: 12:12:52
#Copyrights are applicable
import sys
import os
sys.setrecursionlimit(10000)
try:
    sys.stdin = open('./input.txt', 'r')
    sys.stdout = open('./output.txt', 'w')
except:
    pass


S = input()
words = S.split('.')
words = words[::-1]
ans = ""
for word in words:
    ans+= word+"."
ans = ans[:-1]
print(ans)