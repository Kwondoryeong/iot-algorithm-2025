# da03_fractal02.py
# 시에르핀스키 삼각형

from tkinter import *

## 함수선언
def drawTriangle(x, y, size):
    if size >= 20: # 삼각형 개수 조절
        drawTriangle(x, y, size/2) # 왼쪽 아래 작은 삼각형
        drawTriangle(x+size/2, y, size/2) # 오른쪽 아래 작은 삼각형
        drawTriangle(x+size/4, int(y-size*(3**0.5)/4), size/2) # 중심 위쪽 아래 작은 삼각형
    else:
        canvas.create_polygon(x, y, x+size, y, x+size/2, y-size*(3**0.5)/2, # 3**0.5 : 1.5
                              fill='#FADD00', outline='#FADD00')

## 전역 변수 선언
wSize = 1000
radius = 400

## 메인 코드
root = Tk()
root.title('시에르핀스키 삼각형')
canvas = Canvas(root, height=wSize, width = wSize, bg='white')

drawTriangle(wSize/5, wSize/5*4, wSize*2/3)

canvas.pack()
root.mainloop()
