"""
2072. 홀수만 더하기
"""
import sys
sys.stdin = open('2072_input.txt')
N = int(input())
sum = 0
for tc in range(1, N+1):
    questions = list(map(int, input().split()))
    for question in questions:
        if question % 2:
            sum += question
    print(f'#{tc} {sum}')
    sum = 0
