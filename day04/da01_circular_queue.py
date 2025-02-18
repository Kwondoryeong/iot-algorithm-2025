# da02_circular_queue
# 원형 큐 구현



def isQueueFull():
    global SIZE, front, rear, queue
    if (rear+1) % SIZE == front:
        return True
    else:
        return False
    
def isQueueEmpty():
    global SIZE, front, rear, queue
    if (front == rear):
        return True
    else:
        return False

def enQueue(data):
    global SIZE, front, rear, queue
    if (isQueueFull()):
        print('Queue is Full!')
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data

def deQueue():
    global SIZE, front, rear, queue
    if (isQueueEmpty()):
        print('Queue is Empty')
        return None
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, front, rear, queue
    if (isQueueEmpty()):
        print('큐가 비었습니다.')
        return None
    return queue[(front+1) % SIZE]

# 전역 변수 선언
SIZE = int(input('큐 크기를 입력하세요 > '))
queue = [None for _ in range(SIZE)]
front = rear = 0

# 메인 코드
if __name__ == '__main__':
    while True:
        select = input('삽입(I)/추출(E)/확인(V)/종료(Q) --> ').upper()

        if select == 'Q':
            break
        elif select == 'I':
            data = input('데이터 입력 > ')
            enQueue(data)
            print(f'큐 상태 : {queue}')
            print(f'front : {front}, rear : {rear}')
        elif select == 'E':
            data = deQueue()
            print(f'추출한 데이터 : {data}')
            print(f'큐 상태 : {queue}')
            print(f'front : {front}, rear : {rear}')
        
        elif select == 'V':
            data = peek()
            print(f'확인 데이터 : {data}')
            print(f'큐 상태 : {queue}')
            print(f'front : {front}, rear : {rear}')

        else:
            print('나머지 동작')