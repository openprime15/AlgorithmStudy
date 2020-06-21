"""
2068. 최대수 구하기
"""
import sys

sys.stdin = open("2068_input.txt")
N = int(input())
for tc in range(1, N + 1):
    q = list(map(int, input().split()))
    print(f"#{tc} {max(q)}")
