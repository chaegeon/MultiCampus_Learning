# 순차검색. 무작위로 있는 상태에서?
import random
## 함수
def seqSearch(ary, fData):
    pos = -1
    for i in range(len(ary)):
        if ary[i] == fData:
            pos = i
            break
    return pos # 못찾으면 -1

## 전역
dataAry = [ random.randint(1, 99) for _ in range(20)]
findData = dataAry[random.randint(0, 19)]


## 메인
print( '배열 --> ', dataAry)
position = seqSearch(dataAry, findData) # DA에서 FD를 찾아 돌려줘라
if position == -1:
    print( findData, '없음')
else : 
    print(findData, '는', position, '위치에 있음')
