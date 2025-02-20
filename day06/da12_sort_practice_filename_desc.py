# da12_sort_practice_filename_desc.py
# 파일명 내림차순 정렬

import os
# 클래스와 함수 선언
def makeFileList(folderName):
    fnameAry = []
    for dirName, subDirList, fnames in os.walk(folderName):
        for fname in fnames:
            fnameAry.append(fname)
    return fnameAry

def insertionSort(ary):
    n = len(ary)
    for end in range(1, n):
        for cur in range(end, 0, -1):
            if (ary[cur-1] < ary[cur]):
                ary[cur-1], ary[cur] = ary[cur], ary[cur-1]
    
    return ary

# 전역 변수 선언
fileAry = []

# 메인 코드
fileAry = makeFileList('C:/Program Files/Common FIles')
fileAry = insertionSort(fileAry)
print(f'파일명 역순 정렬({len(fileAry)}개) --> {fileAry}')
