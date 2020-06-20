"""
1933. 간단한 N 의 약수
"""
import sys
sys.stdin = open('1933_input.txt')
a = int(input())
answer = "1 "
for i in range(2, a):
    if a % i == 0:
        answer += str(i) + " "
answer += str(a)
print(answer)
