"""
2050. 알파벳을 숫자로 변환
"""
import sys
sys.stdin = open('2050_input.txt')
a = input()
answer = ""
for i in range(0, len(a)):
    answer += str(ord(a[i])-64) + " "

print(answer)
