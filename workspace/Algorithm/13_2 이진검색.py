# 이진 검색
# 정렬된 데이터
# 반띵해서 처리
import random
## 함수
def binSearch(ary,fData):
    pos = -1
    start = 0
    end = len(ary)-1
    while (start <= end) : #시작보다 끝이 커야 됨
        mid = (start+end) // 2 # 중앙
        if fData == ary[mid] :
            return mid
        elif fData > ary[mid]:
            start = mid + 1
        else: # 아니면 끝쪽을 버림
            end = mid-1

    return pos # 못찾으면 -1

## 전역
dataAry = [ random.randint(1, 999) for _ in range(10)]
findData = dataAry[random.randint(0, 9)]
dataAry.sort() # 데이터 정렬

## 메인
print( '배열 --> ', dataAry)
position = binSearch(dataAry, findData) # DA에서 FD를 찾아 돌려줘라
if position == -1:
    print( findData, '없음')
else : 
    print(findData, '는', position, '위치에 있음')
