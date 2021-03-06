# 필수 라이브러리

- numpy 넘파이
- pandas 판다스
- matplotlib

## numpy

- 교재 : '파이썬 철저입문' - p.214
- 수치해석용으로 만들어진 모듈이라고 보면 됨
  - 수치해석용이라, 따로 머신러닝과 같은 데이터분석을 위해서 만들어진 건 아니다.
  - 보통 연구실에서 많이 사용됨. 분야 막론
  - 특히 머신러닝, 딥러닝 분야에서 많이 사용
  - 판다스도 자료의 기본 타입은 numpy를 사용하기 때문에 알아두면 좋음
- 수학적 계산을 돕기 위해 만들어진 라이브러리

In [ ]:

```
# 보통 배열을 생성할 때 이렇게 생성함  ' np '
# numpy는 일반전으로 np로 줄어서 사용
import numpy as np
```

## 넘파이에서 지원하는 타입

1. array(배열)
   - 주로 통계분석이나, ML/DL에서 사용하는 타입
   - 배열이라고 부름
   - 파이썬의 리스트와는 다름 -> 그래서 배열이라고 부름
2. matrix
   - 수학적 계산이 필요한 경우에 많이 사용
   - 수업시간에는 사용하지 않는다

### 배열의 기본속성

- ndim 엔디멘셔널
  - 배열의 차원을 나타내는 속성
- shape 셰입
  - 배열의 크기를 나타내고, 배열의 크기는 원소의 개수와 동일
  - 1차원 배열인 경우 행이 1, 열이 n인 배열을 의미한다.
  - 배열의 모양은 튜플로 표현이 된다

#### 1차원 배열

- 파이썬의 리스트와 거의 동일

In [ ]:

```
# 리스트를 원소로 하는 배열객체 정도로 이해
arr1D = np.array([1, 2, 3, 4])
arr1D
```

Out[ ]:

```
array([1, 2, 3, 4])
```

In [ ]:

```
#배열의 차원을 확인하는 법
```

In [ ]:

```
arr1D.ndim
```

Out[ ]:

```
1
```

In [ ]:

```
# 1차원이라 행은 없고 열의 개수만 나온 것
arr1D.shape
```

Out[ ]:

```
(4,)
```

In [ ]:

```
arr2D = np.array([[1,2,3], [4,5,6], [7, 8, 9] ])
arr2D.ndim
```

Out[ ]:

```
2
```

In [ ]:

```
# (행, 열)
# 행은 자료의 갯수, 열은 변수의 갯수를 의미
arr2D.shape
```

Out[ ]:

```
(3, 3)
```

In [ ]:

```

```

# 배열의 특징

- **인덱싱, 슬라이싱**
- 팬시 인덱싱
- 배열의 타입
- 넘파이에서만 정의되는 특별한 타입

## 배열의 인덱싱과 슬라이싱

- 리스트와 비슷한데, 표현이 다름
- 기본적으로 개념은 리스트와 동일
- 나중에 판다스나 넘어가도 동일하게 사용됨(?)

In [ ]:

```
# print를 쓰면 리스트처럼 나와서 헷갈리니까 display사용
print( arr1D)
display( arr1D )
[1 2 3 4]
array([1, 2, 3, 4])
```

In [ ]:

```
display( arr1D )
display( arr1D[0])
display( arr1D[1])
display( arr1D[-1])
#out of bound error 주의
# 리스트에서는 아웃 오브 뭐였지 범위 넘어간 것 같은데
display( arr1D[4])
array([1, 2, 3, 4])
1
2
4
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-60-53eda374e375> in <module>()
      6 #out of bound error 주의
      7 # 리스트에서는 아웃 오브 뭐였지 범위 넘어간 것 같은데
----> 8 display( arr1D[4])

IndexError: index 4 is out of bounds for axis 0 with size 4
```

In [ ]:

```
#배열도 이터레이블 객체임 -> 반복이 가능하다는 뜻
# 리스트가 아니기 때문에, 리스트에서 제공되는 메소드들은 사용될 수 없음
# Ex). sort, reverse 등 저거 메소드 이름 맞나?
for x in arr1D:
  print(x)
1
2
3
4
```

In [ ]:

```
# 다만 붙박이 함수(내장함수) 들은 사용가능 함
display(min(arr1D))
display(max(arr1D))
1
4
```

In [ ]:

```
# 리스트 때처럼 슬라이스도 동일하게 가능
display( arr1D[:])
display( arr1D[::-1])
display( arr1D[1:3])
display( arr1D[1:4])
array([1, 2, 3, 4])
array([4, 3, 2, 1])
array([2, 3])
array([2, 3, 4])
```

### 2차원 배열의 인덱싱과 슬라이스

- 인덱싱은 다음오가 같이 표현됨
  - 리스트에서도 마찬가지로 행과 열을 표현행열array[행,열]
- 슬라이스는 행과 열을 각각 슬라이스 할 수 있다행시작행끝열시작열끝arry[행시작:행끝,열시작:열끝]

In [ ]:

```
# 2차원 배열의 인덱스
display(arr2D)
display(arr2D[0,0])
display(arr2D[0,1])
display(arr2D[1,1])
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
1
2
5
```

In [ ]:

```
# 배열운 행우선 인덱스를 제공한다
# 하나만 있으면 행을 처리한다는 뜻
# 열만 인덱싱할 수는 없음. -> 슬라이스를 활용해야 함
# 나중에 판다스는 열우선 인덱스를 제공한다.
display(arr2D[0])
display(arr2D[0, ])
display(arr2D[0, :])
array([1, 2, 3])
array([1, 2, 3])
array([1, 2, 3])
```

In [ ]:

```
#만약 2, 5, 8을 선택하고 싶다면?
# 전체 행에 대해서 슬라이스를 한 후에 열을 선택
display(arr2D)
display(arr2D[:, 1]) #0행부터 끝까지 슬라이스 한 후 각 행의 [1]을 뽑아낸건가
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
array([2, 5, 8])
```

In [ ]:

```
#슬라이스를 잘 활용하면 행과 열을 동시에 슬ㄹ라이스
display(arr2D)
display(arr2D[1:, 1:])
# 0,1,2행 중 1행부터 끝까지 슬라이스 후 그 중에서 [1]부터 끝까지들을 뽑아냄ㄴ 듯
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
array([[5, 6],
       [8, 9]])
```

In [ ]:

```
# 코든느 다음에 알려줄테니 
# 다음을 이용해 인덱싱, 슬라이스 연습해볼 것
arrN= np.arange(1, 31).reshape(3, 10)
arrN
```

Out[ ]:

```
array([[ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10],
       [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]])
```

In [ ]:

```
# 다음수들을 인덱싱 또는 슬라이스 해볼 것

# 16 
display(arrN[1, 5])

# 29
display(arrN[2, 8])

# 14, 15, 16
display(arrN[1, 3:6])

# 18, 28
display(arrN[1:, 7])

# 9, 10, 19, 20
display(arrN[:2, 8:])
16
29
array([14, 15, 16])
array([18, 28])
array([[ 9, 10],
       [19, 20]])
```

In [ ]:

```
arrn = np.arange(1, 51).reshape(5, 10)
arrn
```

Out[ ]:

```
array([[ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10],
       [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
       [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
       [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]])
```

In [ ]:

```
# 14, 15, 16, 17, 24, 25, 26, 27, 34, 35, 36, 37
display(arrn[1:4, 3:7])

# 12, 22, 32
display(arrn[1:4, 1])
array([[14, 15, 16, 17],
       [24, 25, 26, 27],
       [34, 35, 36, 37]])
array([12, 22, 32])
```

In [ ]:

```
## 팬시 인덱싱(배열 인덱싱)
- 인덱스로 배열을 사용
  - 불리언배열 : 배열이 불리언(True,False)로 이루어진 배열을 인덱스로 쓴다
  - 정수배열 : 정수로 이루어진 배열을 인덱스로 쓴다
  - 많이 쓰임. 특시 불리언배열. 조건검색 등에 많이 사용
  File "<ipython-input-72-501ba0e8476f>", line 2
    - 인덱스로 배열을 사용
             ^
SyntaxError: invalid syntax
```

### 불리언 인덱스

- 배열에서 True에 해당하는 값만 선택
- 추후에는 불리언 배열을 조건에 부합하는 결과만 선택할 수 있도록

In [ ]:

```
display(arr1D)
arr1D[ np.array([True, False, False, False]) ]
# 이 때 중요한 것은 배열의 크기와 인덱스 배열의 크기는 동일해야 사용할 수 있음
array([1, 2, 3, 4])
```

Out[ ]:

```
array([1])
```

In [ ]:

```
# 배열에서 조건에 맞는 값만 검색
display(arr1D>2)
display( arr1D[ arr1D > 2 ])
array([False, False,  True,  True])
array([3, 4])
```

In [ ]:

```
# 그냥 나혼자 해본 거..,,
display( arr1D[ arr1D % 2 != 0 ])
array([1, 3])
```

### 정수배열

- 배열에서 원하는 인덱스를 배열로 생성
- **중복 선택이 가능**, 배열의 크기과 인덱스 배열의 크기가 달라도 상관이 없음

In [ ]:

```
idx = np.array([1,1,1,1,1,1,1,1,1,0,0,0,0,2,2,2,2,2,2,3,3,3,3,3,3,2,2,2,1,1,1])
arr1D[idx]
# 이거 무슨 뜻이냐면
# idx 처음의 1 은 -> arr1D의 인덱스 [1] 을 의미하는 것
arr1D의 [1]은 2 라서 2가 나온 것
```

Out[ ]:

```
array([2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 4, 4, 4,
       4, 4, 4, 3, 3, 3, 2, 2, 2])
```

## 배열의 타입

- 리스트와는 다르게 배열은 타입을 가진다
  - 리스트는 여러개의 타입을 원소로 가질 수 있다
  - 배열은 하나의 타입만 원소로 가질 수 있다
- 배열은, 배열이 생성될 떄, 원소들의 타입을 보고 기본적인 자료의 타입을 결정하게 된다.

In [ ]:

```
# 리스트는 여러 타입을 가짐
[1, 2, 1.0, 'string', [1, 2, 3] ]
```

Out[ ]:

```
[1, 2, 1.0, 'string', [1, 2, 3]]
```

In [ ]:

```
arr1D.dtype
# integer이고, 최대 64비트까지 사용이 가능하다 라는 뜻
```

Out[ ]:

```
dtype('int64')
```

In [ ]:

```
# 원소의 타입이 여러개라면 가장 큰 타입이 기본타입이 됨
# 타입이 결정되면, 나머지 값들도 결정된 기본타입을 따르게 된다
arr = np.array([1, 2, 3, 4, 5.0] )
display(arr)
display(arr.dtype)
array([1., 2., 3., 4., 5.])
dtype('float64')
```

In [ ]:

```
# 배열을 생성할 때, 타입을 직접 결정할 수도 있다
arr = np.array([1, 2, 3, 4, 5,], dtype=np.float64)
display(arr)
display(arr.dtype)
#정수로 입력을 했어도 기본타입으로 변경됨
array([1., 2., 3., 4., 5.])
dtype('float64')
```

#### 문자와 정수가 같이 있는 경우에는 문자열이 가장 큰 타입이 됨

- 정수는 문자를 표현할 수 없지만 문자는 숫자도 표현이 가능하기 때문?

#### 텐서플로우를 사용하는 경우에는 자료의 차원과 타입에 매우 민감하기 때문에 중요하다

In [ ]:

```
@## 넘파이에서만 정의되어있는 특별한 타입
- 파이썬은 이런 타입을 갖지 않는다
- inf 무한
  - 표현할 수 없는 값
  함수를 사용했는데 함수가 수렴하지 않고 발산하는 경우(inf, -inf)
-Nan ( Not a Number)
  - 숫자가 아니라는 뜻
  - 결측치(비어있는 값)를 표현할 때 
  값을 표현할 수 없는 경우
```

In [ ]:

```
#참고만 하자 일단
display( type(np.NaN) )
display(np.array([0]) / np.array([0]) ) #0을 0으로 나눔
float
/usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py:3: RuntimeWarning: invalid value encountered in true_divide
  This is separate from the ipykernel package so we can avoid doing imports until
array([nan])
```

In [ ]:

```
#참고만 하자 일단
display( type(np.inf) )
display(np.log(0) )
float
/usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py:3: RuntimeWarning: divide by zero encountered in log
  This is separate from the ipykernel package so we can avoid doing imports until
-inf
```

In [ ]:

```

```

## 배역을 생성하는 방법

- p.215

### 초기화된 배열

- 0과 1은 특별히 취급함
- 원소가 전부 0이거나 전부 1인 경우에는 선형대수에서는 특별하게 취급함
- 0과 1로 초기화된 배열을 만들 수 있음

In [ ]:

```
# 0으로 초기화된 배열
# 기본타입은 실수 형태로 지정 됨 -> 실수로 정수도 표현이 가능해서?
np.zeros(10)
```

Out[ ]:

```
array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
```

In [ ]:

```
# 1로 초기화된 배열
np.ones(10)
```

Out[ ]:

```
array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])
```

In [ ]:

```
# 0과 1이 아닌 다른 값으로 초기화 하고 싶은 경우
np.full(10, 5)
# 두번째 파라미터로 초기값을 지정해주면 됨
# full을 쓸 일이 자주 있진 않음
```

Out[ ]:

```
array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
```

## 수열을 생성하는 방법

- range와 같은 역할

  - range는 자연수만 가능함

- arange

  ## - 실수(소수)에 대한 수열도 만들 수 있음

In [ ]:

```
np.arange(1, 10)
```

Out[ ]:

```
array([1, 2, 3, 4, 5, 6, 7, 8, 9])
```

In [ ]:

```
np.arange(1, 2, 0.1)
```

Out[ ]:

```
array([1. , 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9])
```

In [ ]:

```
# linspace는 주어진 구간에서 갯수만큼 균등한 간격으로 수열을 생성
# arange와 다르게 마지막 원소를 포함
display(np.linspace(0, 10, 11) )
# 0에서 10까지 11개의 구간으로 
display(np.linspace(1, 2, 100) ) # 1에서 2까지 100등분한다는 뜻
array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])
array([1.        , 1.01010101, 1.02020202, 1.03030303, 1.04040404,
       1.05050505, 1.06060606, 1.07070707, 1.08080808, 1.09090909,
       1.1010101 , 1.11111111, 1.12121212, 1.13131313, 1.14141414,
       1.15151515, 1.16161616, 1.17171717, 1.18181818, 1.19191919,
       1.2020202 , 1.21212121, 1.22222222, 1.23232323, 1.24242424,
       1.25252525, 1.26262626, 1.27272727, 1.28282828, 1.29292929,
       1.3030303 , 1.31313131, 1.32323232, 1.33333333, 1.34343434,
       1.35353535, 1.36363636, 1.37373737, 1.38383838, 1.39393939,
       1.4040404 , 1.41414141, 1.42424242, 1.43434343, 1.44444444,
       1.45454545, 1.46464646, 1.47474747, 1.48484848, 1.49494949,
       1.50505051, 1.51515152, 1.52525253, 1.53535354, 1.54545455,
       1.55555556, 1.56565657, 1.57575758, 1.58585859, 1.5959596 ,
       1.60606061, 1.61616162, 1.62626263, 1.63636364, 1.64646465,
       1.65656566, 1.66666667, 1.67676768, 1.68686869, 1.6969697 ,
       1.70707071, 1.71717172, 1.72727273, 1.73737374, 1.74747475,
       1.75757576, 1.76767677, 1.77777778, 1.78787879, 1.7979798 ,
       1.80808081, 1.81818182, 1.82828283, 1.83838384, 1.84848485,
       1.85858586, 1.86868687, 1.87878788, 1.88888889, 1.8989899 ,
       1.90909091, 1.91919192, 1.92929293, 1.93939394, 1.94949495,
       1.95959596, 1.96969697, 1.97979798, 1.98989899, 2.        ])
```

### 무작위 배열을 생성하는 방법

- 랜덤
  - 파이썬도 램덤이 있고 넘파이도 랜덤이 있는데
  - 랜덤은 '균등분포'를 의미한다
- 주로 표본추출, 샘플링 등에 많이 쓰임

In [ ]:

```
# 균등분포를 통해서 정해진 갯수만큼 수를 랜덤하게 생성
# 랜덤이기 때문에, 실행할 때마다 매번 다른 값이 생성됨
np.random.rand(10)
```

Out[ ]:

```
array([0.55554715, 0.28616018, 0.16718228, 0.48878082, 0.04976387,
       0.89068289, 0.76404692, 0.41610231, 0.5059761 , 0.45058493])
```

In [ ]:

```
#정수 형태로 무작위수를 생성하고 싶다면
np.random.randint(0, 10, size=10)
# 10진수로, 10개만큼 ?
```

Out[ ]:

```
array([4, 0, 0, 1, 3, 7, 5, 3, 1, 6])
```

In [ ]:

```
# 무작위로 생성되는 수를 고정
np.random.seed(100) # 시드값은 의미없음 그냥 아무거나. 적은 시드값에 고정된다는 뜻
np.random.rand(10)
```

Out[ ]:

```
array([0.54340494, 0.27836939, 0.42451759, 0.84477613, 0.00471886,
       0.12156912, 0.67074908, 0.82585276, 0.13670659, 0.57509333])
```

In [ ]:

```
# 중복되지 않는 무작위 수를 생성하려면
arr = np.arange(1, 11)
np.random.choice(arr, size = 5)
#주어진 배열에서 사이즈만큼 랜덤하게 선택
#중복가능
# 중복없이 선택하려면
# np.random.choice(arr, size = 5, relpace=False) 이렇게 적으면 됨. 기본값은 True인가 봄
```

Out[ ]:

```
array([5, 4, 8, 2, 2])
```

In [ ]:

```
# 실습
# 로또 번호 생성기
```

### 실습 - 로또번호 생성하기

- 로또는 1부터 45까지의 수 중에서 6자리의 수가 무작위로 선택
- 중복은 허용하지 않음
  - 수업에서는 전통적으로 제일 처음 생성된 로또 번호를 구매!!!!!!!

In [ ]:

```
arr = np.arange(1, 46)
np.random.choice(arr, size=6, replace=False)
```

Out[ ]:

```
array([26,  2, 25,  6, 42, 12])
```

## 배열의 모양

- 고차원의 배열을 저차원의 배열로
- 저차원의 배열을 고차원의 배열로
  - 저차원은 1차원 배열로 변경이 가능
- 변경전의 크기와 변경 후의 크기가 달리지면 안 됨
  - 자료의 개수가 반드시 일치해야 함

### 저차원의 배열을 고차원의 배열로 변경

In [ ]:

```
arr1D = np.random.randint(0, 10, size=4)
arr1D
```

Out[ ]:

```
array([4, 9, 1, 3])
```

In [ ]:

```
display(arr1D.reshape(2, 2))
display(arr1D.reshape(-1, 2))
display(arr1D.reshape(4, 1))
display(arr1D.reshape(-1, 1))
# 행에 -1 을 하고, 열의 크기만 지정해주면, 열에 맞춰서 자동으로 계산 해준다
array([[4, 9],
       [1, 3]])
array([[4, 9],
       [1, 3]])
array([[4],
       [9],
       [1],
       [3]])
array([[4],
       [9],
       [1],
       [3]])
```

### 고차원의 배열을 저차원으로

In [ ]:

```
arr2D = np.random.randint(1, 10, size=(3, 3))
arr2D
```

Out[ ]:

```
array([[4, 8, 9],
       [8, 9, 4],
       [9, 1, 8]])
```

In [ ]:

```
display(arr2D.flatten() ) #납작하게
display(arr2D.ravel() )
# 열기준으로 변경
display(arr2D.flatten(order='F') ) # 오더 파라미터를 이용하면 열 기준으로
array([4, 8, 9, 8, 9, 4, 9, 1, 8])
array([4, 8, 9, 8, 9, 4, 9, 1, 8])
array([4, 8, 9, 8, 9, 1, 9, 4, 8])
```

In [ ]:

```

```

## 넘파이를 이용한 연산

- 기본적인 연산

## 자료의 형태

- 스칼라(Scalar)
- 벡터(Vector)
- 행렬(Matrix)

### 스칼라

- 물리학에서는 양(Volumn, Magnitude)을 표현
- 방향이 없고, 물리적인 `양`만을 표현
- 파이썬에서는 변하지 않는 상수(숫자) 정도로 이해

10,[[1]]

### 벡터

- 물리학에서는 방향성을 가지고 있는 형태

- 파이썬에서는

   

  행이 n개이고, 열이 1인 형태의 배열

  을 벡터라고 합니다.

  - 행벡터와 열벡터가 있는데, 일반적으로 벡터라고 하면 열벡터를 의미합니다.

In [ ]:

```
#넘파이에서는 1차원 배열이 행벡터가 된다.
vector = np.random.randint(1, 10, size = 5)
vector
```

Out[ ]:

```
array([3, 4, 6, 7, 6])
```

In [ ]:

```
vector.reshape(-1, 1)
```

Out[ ]:

```
array([[3],
       [4],
       [6],
       [7],
       [6]])
```

In [ ]:

```
#몇가지 특별한 벡터. = 영벡터와 일벡터
# 벡터인데 모든 원소가 0이거나 1인 경우
display(np.zeros((4,1)) )
display(np.ones((4,1)) )
array([[0.],
       [0.],
       [0.],
       [0.]])
array([[1.],
       [1.],
       [1.],
       [1.]])
```

### 행렬(Matrix)

- 여러개의 벡터가 모여서 행렬을 이루게 된다.
- 행이 n개이고, 열이 m개인 배열을 행령이라고 보면 된다.

In [ ]:

```
mat = np.random.randint(1, 10, size=(3, 5) )
mat
```

Out[ ]:

```
array([[9, 9, 7, 5, 2],
       [8, 4, 5, 8, 4],
       [4, 7, 3, 9, 7]])
```

## 타입이 다른 피연산자간의 연산

```
- 내적이라거나 외적이라거나 그런 건 안 다룸..
```

- 일반적인 사칙연산만 다룰 것
- 배열 타입과 배열타입의 사칙연산이 가능
- 크기가 서로 같기만 하다면, 문제가 없는데
- 크기가 다른 경우에는 문제가 된다.
  - 브로드캐스팅이 되는 경우와 그렇지 않은 경우로 보면 됨

In [ ]:

```
# 스칼라와 벡터의 연산
# 작은 쪽의 크기를 큰 쪽의 크기에 맞춰서 확장(브로드캐스팅)
# 같은 위치의 값들끼리 연산
vector = np.random.randint(1, 10, size = (4, 1) )
vector
```

Out[ ]:

```
array([[2],
       [6],
       [6],
       [5]])
```

In [ ]:

```
# 스칼라를 연산하려는 벡터의 크기에 맞춰서 확장
2 * vector
# 2를 벡터의 크기에 맞춰서 [2 로 만들어서 곱해준다는 뜻
#                         2
#                         2
#                         2]
```

Out[ ]:

```
array([[ 4],
       [12],
       [12],
       [10]])
```

In [ ]:

```
# 스칼라와 행렬의 연산
# 마찬가지로 브로드캐스팅 후에 같은 위치끼리 연산
mat = np.random.randint(1, 10, size=(3, 4))
mat
```

Out[ ]:

```
array([[8, 2, 6, 8],
       [1, 8, 8, 5],
       [2, 3, 7, 2]])
```

In [ ]:

```
2 * mat
```

Out[ ]:

```
array([[16,  4, 12, 16],
       [ 2, 16, 16, 10],
       [ 4,  6, 14,  4]])
```

In [ ]:

```

```

In [ ]:

```
# 벡터와 행렬의 연산
# 벡터가 행렬의 크기에 맞춰서 브로드캐스팅이 가능하면 연산이 가능
display(vector)
display(mat)
array([[1],
       [3],
       [2],
       [9]])
array([[9, 9, 5, 9],
       [2, 9, 3, 1],
       [9, 6, 1, 9]])
```

In [ ]:

```
vector * mat
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-28-faea8dd88a01> in <module>()
----> 1 vector * mat

ValueError: operands could not be broadcast together with shapes (4,1) (3,4) 
```

In [ ]:

```
vector = np.random.randint(1, 10, size=(3,1))
vector
```

Out[ ]:

```
array([[9],
       [2],
       [3]])
```

In [ ]:

```
vector * mat
```

Out[ ]:

```
array([[81, 81, 45, 81],
       [ 4, 18,  6,  2],
       [27, 18,  3, 27]])
```

In [ ]:

```
# 벡터와 벡터의 연산은 브로드캐스팅이 되지 않기 때문에, 크기가 반드시 같아야 합니다.
vec1 = np.random.randint(1, 10, size=(3, 1))
vec2 = np.random.randint(1, 10, size=(4, 1))
display( vec1, vec2 )
array([[4],
       [8],
       [5]])
array([[2],
       [9],
       [8],
       [5]])
```

In [ ]:

```
vec1 * vec2
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-33-8af11b931293> in <module>()
----> 1 vec1 * vec2

ValueError: operands could not be broadcast together with shapes (3,1) (4,1) 
```

In [ ]:

```
# 크기가 같다면, 연산이 가능합니다. 
vec1 = np.random.randint(1, 10, size=(3, 1))
vec2 = np.random.randint(1, 10, size=(3, 1))
display( vec1, vec2 )
array([[4],
       [7],
       [8]])
array([[7],
       [3],
       [9]])
```

In [ ]:

```
vec1 * vec2
```

Out[ ]:

```
array([[28],
       [21],
       [72]])
```

In [ ]:

```
# 행렬과 행렬의 연산
# 차원이 같으면, 벡터와 마찬가지로 브로드 캐스팅 되지 않는다.
# 차원이 다르면, 저차원 행령이 고차원의 행렬로 브로드캐스팅 가능하면 연산이 가능
# 같은 차원이라면, 반드시 두 행렬의 크기가 같아야 한다.
mat1 = np.random.randint(1, 10, size=(2, 2) )
mat2 = np.random.randint(1, 10, size=(2, 2) )
display(mat1, mat2)
array([[1, 9],
       [7, 7]])
array([[3, 2],
       [7, 1]])
```

In [ ]:

```
mat1 * mat2
```

Out[ ]:

```
array([[ 3, 18],
       [49,  7]])
```
