"""
2056. 연월일 달력
"""
import sys

sys.stdin = open("2056_input.txt")
import datetime

N = int(input())
for tc in range(1, N + 1):
    a = input()
    try:
        b = datetime.datetime(int(a[:4]), int(a[4:6]), int(a[6:]))
        print(f"#{tc} {a[:4]}/{a[4:6]}/{a[6:]}")
    except ValueError:
        print(f"#{tc} -1")

