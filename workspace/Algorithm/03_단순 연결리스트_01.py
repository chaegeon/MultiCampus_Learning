## 함수
class Node() :
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    print(current.data, end= ' ')
    while current.link != None :
        current = current.link
        print(current.data, end=' ')
    print()

## 전역
memory=[]
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

## 메인
node = Node() # 첫번째 노드
node.data = dataArray[0]
head = node # head는 반드시 첫번째 노드
memory.append(node)
# 'node'를 재사용

for data in dataArray[1:]: # 정연부터 끝까지 data로 들어감
    pre = node # 노드는 pre가 되고, 다음 data가 node 가 됨 -> pre가 node를 링크하도록
    node = Node()
    node.data = data 
    pre.link = node
    memory.append(node)

printNodes(head)
