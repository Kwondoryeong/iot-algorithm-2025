# da02_image_process.py
# 이미지 처리(정렬 알고리즘)

from tkinter import *
#import tkinter
# import tkinter 사용시 root = tkinter.Tk()

# 일반 퀵정렬 코드
def qSort(arr, start, end):
    if end <= start: # 재귀호출 종료 조건, end는 작아지고 start는 커지면서 서로 만나면 종료
        return
    
    # 시작점
    low = start 
    high = end

    pivot = arr[(low + high) // 2] # 리스트 중간 값을 기준 값으로
    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low + 1, high - 1

    qSort(arr, start, low-1) # 왼쪽 그룹 다시 정렬(재귀호출)
    qSort(arr, low, end) # 오른쪽 그룹 다시 정렬(재귀호출)
    
def quickSort(ary) : 
    qSort(ary, 0, len(ary)-1)


root = Tk()
root.geometry('600x600')
root.title('이미지 처리(정렬)')

photo = PhotoImage(file='./image/cupdog.png')

photoAry = []
h = photo.height() # 600
w = photo.width() # 600

for i in range(h): # 행렬 row와 동일
    for k in range(w): # 행렬 col과 동일
        r, g, b = photo.get(i, k) # x, y 좌표(i행, k열)
        value = (r + g + b // 3)
        photoAry.append(value)
    
print(len(photoAry)) # 360000 리스트 생성

# 퀵소트 사용
dataAry = photoAry[:]
quickSort(dataAry)
midValue = dataAry[h*w // 2]

# 색상 정리, 127보다 작으면 검정색, 127보다 크면 흰색
for i in range(len(photoAry)):
    if photoAry[i] <= midValue:
        photoAry[i] = 0 # black
    else:
        photoAry[i] = 255 # white

# 흑백 이미지로 변경
pos = 0

for i in range(h):
    for k in range(w):
        r = g = b = photoAry[pos]
        pos += 1
        photo.put('#%02x%02x%02x' % (r, g, b), (i, k))
       # photo.put(f'#{r:02x}{g:02x}{b:02x}', (i, k)) # photo에 각 위치의 색상을 photoAry에 들어있는 값으로 변경

paper = Label(root, image=photo)
paper.pack(expand=1, anchor=CENTER)


root.mainloop()