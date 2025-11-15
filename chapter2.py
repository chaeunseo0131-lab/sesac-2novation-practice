# 배열의 주어진 범위의 합을 2로 나눈 몫을 구하세요.
import random

random.seed(42) # 디버깅용 난수값 고정

testcase = 5
tests = [
    (1, 3),(2, 5),(7, 9),(0, 2),(4, 7)
]

A=[0]*(10001) # 2.오류수정 : 배열 크기를 초기화 반복문 범위와 맞춤

for i in range(0, 10001):  
    A[i] = random.randrange(1,101)

for t in range(1, testcase+1):
    answer = 0  # 1. 오류 수정 (초기화) : answer을 for안에 넣어줌
    start, end = tests[t-1]

    for i in range(start, end + 1):
        answer = answer + A[i]
    
    print(str(testcase) + " " + str(answer/2))
    
    # 4. 몫을 구하는 //연산자 이용하면 int됨 
    #3. 오류수정 : 몇 번째 테스트 케이스의 답이 무엇이다.를 출력하고 싶음
    # testcase는 총 개수
    # t는 현재가 몇 번째 케이스인지 나타내는 번호