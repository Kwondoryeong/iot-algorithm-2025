# da10_bussiness_card_management.py

# 클래스, 함수 선언
class Node():
    def __init__ (self):
        self.data = None
        self.link = None

def printNodes(start):
    curr = start
    if curr == None:
        return
    print(curr.data, end = '')
    while curr.link != None:
        curr = curr.link
        print(curr.data, end = ' ')
    print()

def makeSimpleLinkedList(namePhone) :
    global memory, head, curr, prev
    printNodes(head)

    node = Node()
    node.data = namePhone
    memory.append(node)

    if head == None :   # 첫 번째 노드일 때
        head = node
        return
    
    if head.data[0] > namePhone[0]: # 첫 번째 노드보다 작을 때
        node.link = head
        head = node
        return
    
    # 중간 노드로 삽입하는 경우
    curr = head
    while curr.link != None:
        prev = curr
        curr = curr.link
        if curr.data[0] > namePhone[0]:
            prev.link = node
            node.link = curr
            return
    
    # 삽입하는 노드가 가장 큰 경우
    curr.link = node

## 전역 변수 선언
memory = []
head, curr, prev = None, None, None
dataArray = [['지민', '010-1111-1111'],['정국', '010-2222-2222'], ['뷔', '010-3333-3333']]

## 메인 코드 부분 ##
if __name__ == "__main__" :

    for data in dataArray :
        print('DataArray : ', dataArray, ' ||  Data : ', data)
        makeSimpleLinkedList(data)

    printNodes(head)