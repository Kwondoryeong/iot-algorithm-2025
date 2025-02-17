# da11_address_book.py

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

def makeSimpleLinkedList(nameEmail) :
    global memory, head, curr, prev

    node = Node()
    node.data = nameEmail
    memory.append(node)

    if head == None :   # 첫 번째 노드일 때
        head = node
        return
    
    if head.data[1] > nameEmail[1]: 
        node.link = head
        head = node
        return
    
    # 중간 노드로 삽입하는 경우
    curr = head
    while curr.link != None:
        prev = curr
        curr = curr.link
        if curr.data[1] > nameEmail[1]:
            prev.link = node
            node.link = curr
            return
    
    # 삽입하는 노드가 가장 큰 경우
    curr.link = node

## 전역 변수 선언
memory = []
head, curr, prev = None, None, None

## 메인 코드 부분 ##
if __name__ == "__main__" :
    
    while True :
        name = input('이름 --> ')
        if name == '' or name == None :
            break
        email = input('이메일 --> ')
        makeSimpleLinkedList([name, email])
        printNodes(head)