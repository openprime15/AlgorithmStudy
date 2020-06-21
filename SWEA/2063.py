"""
2063. 중간값 찾기
"""
import sys

sys.stdin = open("2063_input.txt")

import statistics

a = int(input())
b = list(map(int, input().split()))
print(statistics.median(b))
