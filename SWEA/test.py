# test 2046이라고 입력을 받았을때,

# 2046.py 실행 결과와 2046_output.txt의 결과가 같을때
# => '맞았습니다' 출력
# else
# => '틀렸습니다' 출력


# 파일 비교 shell 명령어: cmp / diff

# 2063_result.txt 와 2063_output.txt를 비교하여
# 아무일도 없으면
# => '맞았습니다' 출력
# else
# => '틀렸습니다' 출력

import os
import sys

if len(sys.argv) == 1:
    print("문제번호 넣으셔야합니다.")
    sys.exit(1)

problem_number = sys.argv[-1]

os.system(f"python {problem_number}.py > {problem_number}_result.txt")

result = os.system(f"cmp {problem_number}_output.txt {problem_number}_result.txt")

if not result:
    print("정답입니다.")
else:
    print("틀렸습니다.")

# .py 제거 방법: .bash_profile로 들어가서 바꿈
# git bash 홈에서 code . 입력하면 .bash_profile로 들어갈 수 있음
# alias tt="python test.py" 이걸 추가해서 변경하면 됨
# source ~/.bash_profile 입력해서 수정 완료해야함
