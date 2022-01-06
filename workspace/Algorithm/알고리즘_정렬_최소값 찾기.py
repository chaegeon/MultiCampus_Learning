# 맨 앞의 값이 제일 작은 값이라고 가정. 그 다음과 비교
# 비교한 값이 더 작으면 최소값으로.

import random
## 함수
def findMinIndex(ary):
    minIdx = 0 # 일단 0으로 설정?
    for i in range(1,len(ary)): # 1부터 끝까지 비교
        if(ary[minIdx] > ary[i] ): # 0보다 i가 크면 
            minIdx = i # 최소값을 i로 변경
    return minIdx


## 전역
# testAry = [55, 88, 33, 77]
testAry = [ random.randint(1, 99) for _ in range(20)]

## 메인
print(testAry)
minPos = findMinIndex(testAry)
print( '최소값-->', testAry[minPos])
