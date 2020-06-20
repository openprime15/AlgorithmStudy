"""
2019. 더블더블
"""
import sys
sys.stdin = open('2019_input.txt')
a = int(input())
check = 1
answer = "1 "
for i in range(1, a+1):
    check *= 2
    answer += str(check)+" "
print(answer.rstrip())
