# da02_fractal01.py
# 프랙탈

from tkinter import *
import random

# 전역 변수
count = 0
wSize = 800
radius = 300

# 캔버스 생성 이후

# 1. 기본 원 그리기
# cx = 1000//2
# cy = 1000//2
# r = 400
# canvas.create_oval(cx-r, cy-r, cx+r, cy+r, width=2, outline='red')


# 2. 프랙탈 원그리기 재귀함수 선언
def drawCircle(x, y, r):
    global count
    count += 1
    canvas.create_oval(x-r, y-r, x+r, y+r,fill='#FAFAFA')
    canvas.create_text(x, y-r, text=str(count), font=('',30))
    if r >= radius/2: # 아직 매개변수로 받는 반지름이 기본사이즈보다 크면
        drawCircle(x-r//2, y, r//2) # 중심의 왼쪽을 계속 그림(재귀호출)
        drawCircle(x+r//2, y, r//2) # 중심의 오른쪽을 계속 그림

# 메인 코드
root = Tk()
# 윈도우 창을 다 덮음 -> 그림을 그림(캔버스 밖으로는 그릴 수 없음)
canvas = Canvas(root, height=800, width=800, bg='white')

drawCircle(wSize//2, wSize//2, radius)

canvas.pack()
root.mainloop()