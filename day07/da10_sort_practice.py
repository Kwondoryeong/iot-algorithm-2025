# da10_sort_practice.py
# 이미 정렬된 줄에 끼어들기

import random
import time

# 클래스와 함수 선언 부분

def bubbleSort(ary):
    n = len(ary)
    for end in range(n-1, 0, -1):
        changeYN = False
        for cur in range(0, end):
            if (ary[cur] > ary[cur+1]):
                ary[cur], ary[cur+1] = ary[cur+1], ary[cur]
                changeYN = True
            if not changeYN:
                break
    
    return ary

def qSort(arr, start, end):
    if end <= start:
        return
    
    low = start
    high = end
    
    pivot = arr[(low + high) // 2] # 작은 값은 왼쪽, 큰 값은 오른쪽으로 분리
    while low <= high :
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low + 1, high - 1
    mid = low # 모든 정렬을 한바퀴 돌면 low는 리스트 중간 쯤 가있는다
    
    qSort(arr, start, mid-1) # 왼쪽 그룹 다시 정렬(재귀호출)
    qSort(arr, mid, end) # 오른쪽 그룹 다시 정렬(재귀호출)
    
def quickSort(ary):
    qSort(ary, 0, len(ary)-1)

# 메인 코드
tempAry = [random.randint(10000, 99999) for _ in range(1000000)]
tempAry.sort()

rndPos = random.randint(0, len(tempAry)-1)
print(f'데이터 개수 --> {len(tempAry)}')
print(f'끼어든 위치 --> {rndPos}')
tempAry.insert(rndPos, tempAry[-1])

bubbleAry = tempAry[:]
quickAry = tempAry[:]

start = time.time()
bubbleSort(bubbleAry)
end = time.time()
print(f'다시 정렬 시간(버블 정렬) --> {end-start:>10.3f}초')

start = time.time()
quickSort(quickAry)
end = time.time()
print(f'다시 정렬 시간(퀵 정렬) --> {end-start:>10.3f}초')