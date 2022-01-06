## 함수
def isStackFull() :
    global SIZE, stack, top
    if (top >= SIZE-1):
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if ( isStackFull() ) :
        print('스택 풀')
        return
    top += 1
    stack[top] = data

##전역
SIZE = 5
stack = [ None for _ in range(SIZE) ]
top = -1

## 메인
# stack = ['커피', '녹차', '꿀물', '콜라', '환타']
# top = 4

stack = ['커피', '녹차', '꿀물', '콜라', None]
top = 3

push('보리차')
print(stack)
push('사이다')
print(stack)
