"""
1545. 거꾸로 출력해 보아요
"""
import sys

sys.stdin = open("1545_input.txt")
a = int(input())
answer = ""
for i in range(a, -1, -1):
    answer += str(i) + " "
print(answer.rstrip())
