"""
2071. 평균값 구하기
"""
import statistics
import sys
sys.stdin = open('2071_input.txt')
N = int(input())
questions = []
for tc in range(1, N+1):
    questions = list(map(int, input().split()))
    print(f'#{tc} {round(statistics.mean(questions))}')
