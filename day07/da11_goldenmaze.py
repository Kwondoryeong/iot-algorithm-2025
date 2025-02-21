# da11_goldenmaze.py
# 동적 계획법 응용 황금 미로

# 미모이제이션에서 계속 행열 비교하며 큰값과 황금미로 큰값 더함
# 더한 이후 미모이제이션 행열 비교위치 이동
def growRich():
    memo = [[0 for _ in range(COL)] for _ in range(ROW)]
    memo[0][0] = goldenMaze[0][0]

    rowSum = goldenMaze[0][0]
    for i in range(1, ROW):
        rowSum += goldenMaze[0][i]
        memo[0][i] = rowSum # 행 누적 합
        # print(f'rowSum : {rowSum} goldenMaze[{i}][0] : {goldenMaze[i][0]} memo[{i}][0] : {memo[i][0]}\n',end='')
    
    # for i in range(0, ROW):
    #     print(f'{memo[i]}')

    colSum = goldenMaze[0][0]
    for i in range(1, COL):
        colSum += goldenMaze[i][0]
        memo[i][0] = colSum # 열 누적 합
        # print(f'colSum : {colSum} goldenMaze[{i}][0] : {goldenMaze[i][0]} memo[{i}][0] : {memo[i][0]}\n', end='')

    print('----- 황금 미로 -----')
    for row in range(1, ROW):
        for col in range(1, COL):
            if (memo[row][col-1] > memo[row-1][col]):   # (1,1)시작 시 --> (1,0) (0,1) 부터 비교해서 (1,0)이 (0,1)보다 크면 
                memo[row][col] = memo[row][col-1] + goldenMaze[row][col] # memo(1,1)에 GoldenMaze(1,1)+ (1,0) : 큰값(행값) 더해서 저장
            else:
                memo[row][col] = memo[row-1][col] + goldenMaze[row][col] # memo(1,1)에 GoldenMaze(1,1)+ (0,1) : 큰값(열값) 더해서 저장
            print(f'{memo[row][col]}', end=' ')
        print()

    # for i in range(0, ROW):
    #     for j in range(0, ROW):
    #         print(f'{memo[i][j]}',end=' ')
    #     print()

    # # 테스트 시작
    # print('\n## 테스트 시작 ##\n')
    # memo = [[0 for _ in range(COL)] for _ in range(ROW)]
    # for row in range(0, ROW):
    #     for col in range(0, COL):
    #         if (memo[row][col-1] > memo[row-1][col]):   # (1,1)시작 시 --> (1,0) (0,1) 부터 비교해서 (1,0)이 (0,1)보다 크면 
    #             memo[row][col] = memo[row][col-1] + goldenMaze[row][col] # memo(1,1)에 GoldenMaze(1,1)+ (1,0) : 큰값(행값) 더해서 저장
    #         else:
    #             memo[row][col] = memo[row-1][col] + goldenMaze[row][col] # memo(1,1)에 GoldenMaze(1,1)+ (0,1) : 큰값(열값) 더해서 저장
    #         print(f'{memo[row][col]}', end=' ')
    #     print()
    # print('\n## 테스트 완료 ## \n')
    # # 테스트 끝

    return memo[ROW-1][COL-1]

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

