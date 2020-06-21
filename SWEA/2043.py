"""
2043. 서랍의 비밀번호
"""
import sys

sys.stdin = open("2043_input.txt")
a, b = map(int, input().split())
print(a - b + 1)
