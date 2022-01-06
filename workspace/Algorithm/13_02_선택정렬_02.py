import random
## 함수
def selectionSort(ary):
    n = len(ary)
    for cy in range(0, n-1): # 만약 4개면 3번 싸이클 비교
        minIdx = cy # 싸이클의 가장 앞의 값이 일단은 최소값
        for i in range(cy+1, n): # cy 다음 값부터 끝까지 
            if(ary[minIdx] > ary[i] ): # 0보다 i가 크면 
                minIdx = i # 최소값을 i로 변경
        ary[cy], ary[minIdx] = ary[minIdx], ary[cy]
    return ary
## 전역
dataAry = [ random.randint(1, 99) for _ in range(20)]


## 메인
print( '정렬 전-->', dataAry)
dataAry = selectionSort(dataAry)

print( '정렬 후-->', dataAry)



