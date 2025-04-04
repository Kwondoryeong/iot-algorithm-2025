# da12_stack_apply.py

# 스택 응용_웹 서핑 이전 페이지 돌아가기

import webbrowser
import time
webbrowser.open("http://www.hanbit.co.kr")

## 전역 변수 선언
# SIZE = int(input('스택크기를 결정하세요 > '))
SIZE = 6
stack = [None for _i in range(SIZE)] # 안쓰는변수 _로 대체 가능, None 반복
top = -1

## 함수 선언
def isStackFull(): # 스택이 꽉 찼는지 확인하는 함수
    global SIZE, stack, top
    if (top == SIZE - 1): # FUll, 데이터 추가 불가 / 실무에서 쓰는 스택은 거의 무제한
        return True
    else:
        return False

def isStackEmpty(): # 스택이 비었는지 확인
    global SIZE, stack, top
    if (top == -1): # Empty
        return True
    else:
        return False

def push(data): # 스택에 데이터 추가
    global SIZE, stack, top
    if isStackFull(): # isStackFull() == True와 동일
        print('Stack is full!')
        # return 생략
    else:
        top += 1
        stack[top] = data

def pop(): # 스택에서 데이터 추출
    global SIZE, stack, top
    if isStackEmpty():
        print('Stack is empty.')
        return None
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return data

def peek(): # 스택의 top위치의 데이터 확인(살짝보기)
    global SIZE, stack, top
    if isStackEmpty():
        print('Stack is empty.')
        return None
    else:
        return stack[top]
    
## 메인 코드 부분
if __name__ == '__main__':
    urls = ['naver.com', 'daum.net', 'nate.com']

    for url in urls :
        push(url)
        # print(f'url : {url} / urls : {urls}')
        webbrowser.open('http://' + url)
        print(url, end = '-->')
        time.sleep(1)

    print('방문 종료')
    time.sleep(5)

    while True :
        url = pop()
        if url == None:
            break
        webbrowser.open('http://' + url)
        print(url, end = '-->')
        time.sleep(1)
    print('방문 종료')