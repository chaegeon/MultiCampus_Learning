## 함수
class Node() :
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData) : 
    global memory, head, current, pre

    # 첫 노드 앞에 데이터 추가( head가 바뀜)
    if head.data == findData :  #내가 찾고자 하는 데이터가 헤드라면
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    # 헤드가 아닌 중간에 데이터 삽입
    # '사나' 앞에 '솔라'를 추가
    current = head # head에서 시작해서 current 노드가 사나인지 확인
    while current.link != None :
        pre = current # pre는 current로
        current = current.link # 그 다음 current는 다음노드로(링크로 연결된 다음 노드)
        if current.data == findData : # 현재 노드가 내가 찾는 데이터(사나)라면
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
    # 마지막에 추가
    node = Node()
    node.data = insertData
    current.link = node
    return


## 전역
memory=[]
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

## 메인
node = Node()  # 첫 노드
node.data = dataArray[0]
head = node
memory.append(node)

for data in dataArray[1:] :  # 정연부터 끝까지 data로 들어감
    pre = node # 노드는 pre가 되고, 다음 data가 node 가 됨 -> pre가 node를 링크하도록
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)
printNodes(head)

insertNode('다현', '화사')
printNodes(head)
insertNode('사나', '솔라')
printNodes(head)
insertNode('재남', '문별')
printNodes(head)