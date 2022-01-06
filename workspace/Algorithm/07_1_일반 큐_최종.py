## 함수
def isQueueFull() : # 여길 수정할 거
    global SIZE, queue, front, rear
    if ( rear != SIZE-1) :
        return False
    elif (rear == SIZE-1) and (front == -1): 
        return True
    else :
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i] # 큐 i-1을 큐i로 떙김
            queue[i] = None # 비우고
        front -= 1
        rear -= 1
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print('큐 꽉!')
        return
    rear += 1
    queue[rear] = data

def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (front == rear) :
        return True
    else :
        return False

def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅~')
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅~')
        return None
    return queue[front+1]

## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front=rear=-1

## 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print('출구<--', queue, '<--입구')
print('입장손님:', deQueue())
print('입장손님:', deQueue())
print('출구<--', queue, '<--입구')
enQueue('재남')
print('출구<--', queue, '<--입구')
enQueue('BTS')
print('출구<--', queue, '<--입구')
enQueue('울랄라세션')
print('출구<--', queue, '<--입구')

# 2명이 나갔는데도 왜 꽉찼을까? 
# => rear 꼬리가 마지막에 가 있음
# => 그렇다고 앞으로 땡기면 오버헤드가 발생하게 됨
# 교재 큐 p.23 참고
