def isQueueFull():
    global SIZE, queue, front, rear
    if (rear == SIZE-1) : # 꽉찼
        return True
    else:
        return False

def enQueue(data): # 데이터를 넘겨받
    global SIZE, queue, front, rear
    if ( isQueueFull( )):
        print('큐 풀')
        return 
    
    rear += 1
    queue[rear] = data

def isQueueEmpty() :
    global SIZE, queue, front, rear
    if front == rear :
        return True
    else: 
        return False

def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print( '큐 텅텅')
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1 #머리와 꼬리가 -1

## 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print('출구<--', queue, '<--입구')
enQueue('재남') # 꽉찬 상태에서 데이터를 삽입하면
print('출구<--', queue, '<--입구')

print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
print('출구<--', queue, '<--입구')
print(deQueue())
print('출구<--', queue, '<--입구')