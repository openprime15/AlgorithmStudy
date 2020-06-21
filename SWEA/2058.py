"""
2058. 자릿수 더하기
"""
import sys

sys.stdin = open("2058_input.txt")
a = input()
sum = 0
for i in range(len(a)):
    sum += int(a[i])
print(sum)
