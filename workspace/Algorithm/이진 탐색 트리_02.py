## 함수/클래스
class TreeNode() :
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

## 전역
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']


## 메인
node1 = TreeNode()
node1.data = nameAry[0] # 루트
root = node1
memory.append(node1) # 필수는 아니지만? 메모리에 모아놓자

# 첫 루트만 node1로 지정해주고 나머지는 for문으로 node n 생성(대용량 대비)
for name in nameAry[1:]: # 레드벨벳부터 끝까지
    node = TreeNode()
    node.data = name

    
    current = root
    while True:
        if name < current.data : # 작으면 왼쪽에 위치. 가나다 순?
        # 무조건 왼쪽으로 보내면 덮어씌여지니까. 비었을 때만 하도록
        # 왼쪽에 데이터가 있다면 current가 밑으로 내려감(자식노드로). 교재 트리 p.25 참고
            if current.left == None: # 왼쪽이 비었다면
                current.left = node
                break
            current = current.left

        else:
            if current.right == None:
                current.right = node
                break
            current = current.right
    memory.append(node)
print('이진 탐색 트리 구성 완료')

        