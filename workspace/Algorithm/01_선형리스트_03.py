## 선형리스트 삭제
# 선형리스트는 빈 칸을 두면 안 됨
# 삭제한 후 뒤의 데이터들을 앞으로 땡김

## 함수부
def add_data(friend):
  katok.append(None)
  kLen = len(katok)
  katok[kLen-1] = friend

def insert_data(position, friend):
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

## 전역부
katok = []

## 메인부
print(katok)
delete_data(4)
print(katok)