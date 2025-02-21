# da12_goldenmaze.py
# 황금미로 길 표시하기


def printMaze(arr):
    for i in range(ROW):
        for j in range(COL):
            print(f'{arr[i][j]:>3d}',end = ' ')
        print()
    print()


# 미모이제이션에서 계속 행열 비교하며 큰값과 황금미로 큰값 더함
# 더한 이후 미모이제이션 행열 비교위치 이동
def growRich():
    memo = [[0 for _ in range(COL)] for _ in range(ROW)]
    memo[0][0] = goldenMaze[0][0]

    rowSum = goldenMaze[0][0]
    for i in range(1, ROW):
        rowSum += goldenMaze[0][i]
        memo[0][i] = rowSum # 행 누적 합
    
    colSum = goldenMaze[0][0]
    for i in range(1, COL):
        colSum += goldenMaze[i][0]
        memo[i][0] = colSum # 열 누적 합
      
    print('----- 황금 미로 -----')
    for row in range(1, ROW):
        for col in range(1, len(goldenMaze[row])):
            if (memo[row][col-1] > memo[row-1][col]):   # (1,1)시작 시 --> (1,0) (0,1) 부터 비교해서 (1,0)이 (0,1)보다 크면 
                memo[row][col] = memo[row][col-1] + goldenMaze[row][col] # memo(1,1)에 GoldenMaze(1,1)+ (1,0) : 큰값(행값) 더해서 저장
            else:
                memo[row][col] = memo[row-1][col] + goldenMaze[row][col] # memo(1,1)에 GoldenMaze(1,1)+ (0,1) : 큰값(열값) 더해서 저장

    retValue = memo[ROW-1][COL-1]

    print('## 메모이제이션 ##')
    printMaze(memo)

    row, col = ROW - 1, COL - 1
    memo[row][col] = 0
    while row != 0 or col !=0:
        if row-1 >= 0 and col-1 >= 0:
            if memo[row-1][col] > memo[row][col-1]:
                row -= 1
            else:
                col -= 1
        elif row-1 < 0 and col-1 >= 0:
            col -= 1
        else:
            row -= 1
        memo[row][col] = 0

    print('## 메모이제이션(황금 미로 길) ##')
    printMaze(memo)

    return retValue

# 전역 변수
goldenMaze = [[1, 4, 4, 2, 2],
              [1, 3, 3, 0, 5],
              [1, 2, 4, 3, 0],
              [3, 3, 0, 4, 2],
              [1, 3, 4, 5, 3]]
ROW, COL = 5, 5

# 메인 코드
macolGold = growRich()
print(f'황금 미로에서 얻은 최대 황금 개수 --> {macolGold}')