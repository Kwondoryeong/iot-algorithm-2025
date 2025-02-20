# da13_sort_practice_score.py
# 성적별로 조 편성

def scoreSort(ary):
    n = len(ary)
    for end in range(1, n):
        for cur in range(end, 0, -1):
            if (ary[cur-1][1] > ary[cur][1]):
                ary[cur-1], ary[cur] = ary[cur], ary[cur-1]
                print(f'정렬 중({end}회차, 현재(Idx):{cur}, arr[cur-1]:{ary[cur-1]}, arr[cur]:{ary[cur]}) --> 변경O')
            else:
                print(f'정렬 중({end}회차, 현재(Idx):{cur}, arr[cur-1]:{ary[cur-1]}, arr[cur]:{ary[cur]}) --> 변경X')
        
        print(f'정렬 중({end}회) --> {ary}')
        print()

    return ary

# 전역변수
scoreAry = [['선미', 88], ['초아',99], ['화사', 71], ['영탁', 78], ['영웅', 67], ['민호',92]] # 길이 6

# 메인 코드
print(f'정렬 전 --> {scoreAry}')
scoreAry = scoreSort(scoreAry)
print(f'정렬 후 --> {scoreAry}')