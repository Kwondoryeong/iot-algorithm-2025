# da12_search_practice.py
# 순차 검색과 이진 검색의 성능 비교

import random
# 클래스와 함수 선언

def seqSearch(ary, data):
    global count
    pos = -1
    for i in range(len(ary)):
        count += 1
        if ary[i] == data:
            pos = i
            break
    return pos

def binSearch(ary, data):
    global count
    start = 0
    end = len(ary) - 1

    while (start <= end):
        count += 1
        mid = (start + end) // 2

        if data == ary[mid]:
            return mid
        elif data > ary[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# 전역 변수
dataAry, sortedAry = [], []
findData = 7878
count = 0

# 메인 로직
dataAry = [ random.randint(0, 999999) for _ in range(1000000)]
dataAry.insert(random.randint(0, 1000000), findData)
sortedAry = sorted(dataAry)

print(f'# 비정렬 배열(100만개) > {dataAry[0:5]} ~~~~ {dataAry[-5:len(dataAry)]}')
print(f'# 정렬 배열(30만개) > {sortedAry[0:5]} ~~~~ {sortedAry[-5:len(sortedAry)]}')

count = 0
pos = seqSearch(dataAry, findData)
if pos != -1:
    print(f'순차 검색(비정렬 데이터) --> {count}회')

count = 0
pos = binSearch(sortedAry, findData)
if pos != -1:
    print(f'이진 검색(정렬 데이터) --> {count}회')