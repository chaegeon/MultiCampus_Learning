
## 함수
def addNumber(num): # 100이라면
    if num <= 1 : # num이 1보다 작으면
        return 1 # 1 반환
    return num + addNumber(num-1) # 100 + 99

print(addNumber(100))

# 교재 재귀 p.10 참고
# 1부터 10 까지 더한다 하면
# 10+9+addNum()
# 10+9+8 addNum()
# ... 10 + 9 + 8 + ... + addNum(1) 이런 느낌?