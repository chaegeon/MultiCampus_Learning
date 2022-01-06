
## 함수
from typing import Counter


def openBox() :
    global count
    print('상자열기')
    count -= 1
    if count == 0:
        print('##반지##')
        return
    openBox()
    print('상자닫기')
    return

## 메인
count = 5
openBox() 
# 5번 열었는데 4번 닫는 이유? -> 교재 재귀 p.8 참고

