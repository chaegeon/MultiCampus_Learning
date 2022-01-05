def add_data(friend): #선형리스트에 친구를 추가하는 함수
  katok.append(None)
  kLen = len(katok)
  katok[kLen-1] = friend

def insert_data(position, friend): # 지정 자리에 새 데이터를 추가하는
  katok.append(None)
  kLen = len(katok)
  for i in range(kLen-1, position, -1): # 끝부터 지정 자리까지 -1씩
    katok[i] = katok[i-1] # i자리에 i-1 자리의 친구를 이동 => 다르게 말하면 i-1을 i로 옮김
    katok[i-1] = None
  katok[position] = friend

def delete_data(position): # 중간 자리의 데이터를 삭ㅈ[]
  katok[position] = None # 자리 비움 삭제
  kLen = len(katok)
  
  for i in range(position+1, kLen, 1 ): # 자리+1 부터 길이-1까지
    katok[i-1] = katok[i]
    katok[i] = None
  del(katok[kLen-1]) # 남겨진 마지막 칸 삭제

## 전역변수부
katok = [] # 선형 리스트

## 메인코드부
add_data('다현')
add_data('정연')
add_data('쯔의')
add_data('사나')
add_data('지효')
print(katok)
add_data('모모')
print(katok)

insert_data(3, '미나')
print(katok)
insert_data(3, '유정')
print(katok)

delete_data(4)
print(katok)
