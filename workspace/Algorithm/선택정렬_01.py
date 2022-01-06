# 효율은 좀 떨어져도 실무에서도 사용 가능
import random

## 함수
def findMinIndex(ary):
    minIdx = 0 # 일단 0으로 설정?
    for i in range(1,len(ary)): # 최소값을 0으로 설정했으니, 1부터 끝까지 비교
        if(ary[minIdx] > ary[i] ): # 0보다 i가 크면 
            minIdx = i # 최소값을 i로 변경
    return minIdx

## 전역
before = [ random.randint(1, 99) for _ in range(20)] # 정렬 전의 방
after = [] # 정렬 후의 방

## 메인
print( '정렬 전-->', before)
for i in range(len(before)):
    minPos = findMinIndex(before) # 최소값을 찾아서
    after.append(before[minPos]) # after로 옮기고
    del ( before[minPos]) # 옮겨진 건 지우고 ( 복사 후 붙여넣기 개념이라 원본 삭제?)

print( '정렬 후-->', after)


