# da10_fractal_practice.py
# 프랙탈 원 그리기
# da02_fractal01.py
# 프랙탈

from tkinter import *
import random

# 전역 변수 선언
colors = ['red','green', 'blue', 'black', 'orange', 'indigo', 'violet']
wSize = 1000
radius = 450

# 2. 프랙탈 원그리기 재귀함수 선언
def drawCircle(x, y, r):
    canvas.create_oval(x-r, y-r, x+r, y+r, width=2, outline=random.choice(colors),fill='#FAFAFA')
    if r >= 5:
        drawCircle(x+r//2, y, r//2)
        drawCircle(x-r//2, y, r//2)

# 메인 코드
root = Tk()
root.title('원 모양의 프랙탈')
canvas = Canvas(root, height=wSize, width=wSize, bg='white')

drawCircle(wSize//2, wSize//2, radius)

canvas.pack()
root.mainloop()