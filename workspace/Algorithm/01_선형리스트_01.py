# 선형 리스트 추가

## 함수부
def  add_data(friend) :
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend

## 전역변수부
katok = [] # 선형 리스트

## 메인코드부
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(katok)
add_data('모모')
print(katok)