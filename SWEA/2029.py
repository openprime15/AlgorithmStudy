"""
2029. 몫과 나머지 출력하기
"""

import sys
sys.stdin = open('2029_input.txt')

N = int(input())

for tc in range(1, N+1):
    a, b = map(int, input().split())
    print(f'#{tc} {a//b} {a%b}')
