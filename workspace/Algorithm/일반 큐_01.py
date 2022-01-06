## 함수


## 전역
#queue = [None, None, None, None, None, ]
# 스택과 같네?-> 같은 배열 구조인데 이걸 어떻게 조작하느냐에 따라 달라짐
# 출구와 입구를 같게 할 것인지, 다르게 할 것인지
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1 #머리와 꼬리가 -1

## 메인

#enQueue
rear += 1 #꼬리증가
queue[rear] = '화사' # 꼬리에 자리

rear += 1 #꼬리증가
queue[rear] = '솔라' # 꼬리에 자리

rear += 1 #꼬리증가
queue[rear] = '문별' # 꼬리에 자리

print( '출구 <--', queue, '<-- 입구')

#deQueue
front += 1
data = queue[front]
queue[front] = None
print('식사할 손님:', data)

front += 1
data = queue[front]
queue[front] = None
print('식사할 손님:', data)

front += 1
data = queue[front]
queue[front] = None
print('식사할 손님:', data)
