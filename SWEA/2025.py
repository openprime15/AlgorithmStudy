"""
2025. N줄덧셈
"""
import sys
sys.stdin = open('2025_input.txt')
a = int(input())
sum = 0
for i in range(1, a+1):
    sum += i
print(sum)
