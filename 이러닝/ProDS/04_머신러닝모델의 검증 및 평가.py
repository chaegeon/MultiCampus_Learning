# 머신러닝 모델의 검증 및 평가

```
#과대적합 #훈련자료 #검증자료 #평가자료 #교차검증 #편향 #분산
```

## 머신러닝 모델의 분석절차
- 머신러닝 모델과 일반통계모델의 차이점
    - 아주 복잡한 패턴이 학습 가능
    - 좋아보이지만 예측성능 면에서는 그렇지 않음
    - 모든 패턴을 학습하려 시도
    - 작은 이상치나 노이즈마저도 모델링해버림
    - 이러다 보면 예측력이 떨어짐 이런 경우를 **과대적합**(과적합)이라고 표현한다
    - 이 과적합을 이해하고 잘 컨트롤하는 것이 머신러닝의 성공여부를 결정


### 모델 기반 지도학습 알고리즘의 일반적인 분석절차

- X에 따른 레이블 y. 어떤 x들이 어떻게 y에 영향을 끼치는지 그 F를 학습하는데

1. 주어진 데이터 전처리 및 탐색

2. 적절한 모델을 선택

3. 주어진 데이터로 모델을 **훈련**시킴
4. 훈련된 모델을 적용하여 **새로운 데이터**에 대한 **예측**을 수행 ( 새로운 데이터에 대한 예측력 : 일반화 능력)1. 

- ![image-20220210234643716](C:\Users\chgeo\AppData\Roaming\Typora\typora-user-images\image-20220210234643716.png)

- Feature1, 2는 특성변수 X1, X2

- 세모와 네모는 레이블 Y

- 세모와 네오의 경계면을 찾는 분류형 모델
- 점선(분류경계면)이 찾은 모델
- X로 표시된 것이 새로운 데이터
- 이 데이터가 어느 경계면에 위치하는지 그 주변에 뭐가 있는지 이런 것들을 이용해서 X가 무엇인지 예측하는 것
- 경계면 안 쪽에 다 세모인데 X도 경계면 안쪽이니 얘도 세모


### (overfitting)의 문제

- **주어진 자료는 거의 완벽한 예측이 가능하지만, 미래의 새로운 자료에 대한 예측력이 떨어지는 문제**
- 복잡한 알고리즘을 사용하여 데이터를 훈련하는 경우 과대적합 문제를 항상 염두에 두어야 함
- 머신러닝의 알고리즘은 거의 대부분 발생한다고 보면 됨
- 
- <img src="C:\Users\chgeo\AppData\Roaming\Typora\typora-user-images\image-20220210235625996.png" alt="image-20220210235625996" style="zoom: 50%;" />

- 완벽하게 분류가 가능한 깔끔한 데이터는 별로 없음
- 빨강과 파랑처럼 경계면에서 섞여있음
- 까만선은 이상적인 분류경계면.. 굉장히 복잡한 알고리즘을 훈련하기 때문에, 완벽한 예측을 시도하기 때문에 초록색선처럼 됨
- 파란점지역(까만선 )이지만, 실제로는 빨간점 경계면(초록색 선)이라, 이런 식으로 새로운 데이터가 들어왔을 때 예측력이 떨어질 수 있음

- <img src="C:\Users\chgeo\AppData\Roaming\Typora\typora-user-images\image-20220210235647285.png" alt="image-20220210235647285" style="zoom:50%;" />

- 회귀 문제용도 마찬가지
- X에 대한 Y의 값을 적으로 찍었는데
- 까만직선이 이상적인..
- 머신러닝 알고리즘을 적용하면, 복잡한 할고리즘을 훈련하기 때문에 모든 까만점을 연결하려고 함. 
- 그래서 파란 선의 함수를 추정하게 됨
- 현재 주어진 훈련용 자료는 오차없이 모두 다 맞춤
- 근데 새로운 데이터가 주어졌을 때 오차가 발생. 예측력이 떨어지게 됨



### 의 검증 및 평가 개요

- 모델 평가의 필요성

    - 과대적합을 막고 **일반화 오차**를 줄이기 위해서는, 새로운 데이터에 얼마나 잘 일반화될지를 파악해야 함

        - 일반화 오차: 새로운 데이터에 대한 오차

        - 새로운 데이터는 Y값이 관찰되지 않은 상태로, X만 우리에게 주어짐

        - Y가 없으니 이게 맞는지 틀리는지 모름..

        - 이때 트릭을 사용하는데, 훈련용 자료는 Y가  관찰이 된 상태

        - 이 중 일부를 마치 새로운 자료인 것처럼 미리 떼어 놓음

        - 나중에 이걸로 모형을 평가해보고, 이 떼어놓은 값과 예측된 값을 비교해봄

        - 이럼으로써 모형이 얼마나 일반화 능력이 있는지 평가할 수 있음 

        - 그래서 모델 적합을 위해서 훈련용 자료를 전부 다 쓰는 게 아니라, 그 중 일부를 평가용 자료로 따로 떼어놓고 이 자료는 모델을 학습하는데에 사용되지 않는 것
    
    - 모델 적합에 사용된 자료를 평가를 위해 재활용하지 않고, 평가만을 위한 데이터를 확보할 필요가 있음




### 모델 검증 및 평가를 위한 데이터의 구분

#### Hold-Out 방식

- 주어진 자료를 다음의 세 그룹으로 랜덤하게 분할한 뒤, 주어진 목적에 따라 각각 모델의 훈련, 검증, 평가에 활용함
- <img src="C:\Users\chgeo\AppData\Roaming\Typora\typora-user-images\image-20220211002247706.png" alt="image-20220211002247706" style="zoom:50%;" />
  - 2개로 쪼갤 때엔 Traning/Test
  - 3개로 쪼갤 떄엔 Trainig/Test/Validation

1. 훈련데이터 (Training data)

    - 모델의 **학습**을 위해 사용되는 자료. X를 가지고 Y를 찾는, 즉 f()를 찾는데 쓰이는 데이터

2. 검증 데이터 (Validation)

    - 훈련자료로 적합되는 모델을 최적의 성능으로 **튜닝**하기 위해 사용되는 자료
    - 훈련에 필요한 하이퍼파라미터를 조정하거나, 변수 선택 등에 이용
        - 하이퍼파라미터: 학습을 통해서 찾아내고자하는 모델의 모수가 아니라, 그 모델의 정확한 f함수값이 아니라, f함수를 정의하기 위한 계수가 아니라
        - 이 모델을 훈련하기 전에 사전에 주어지는 파라미터
        - 학습은 하지 않지만, 이 값으로 인해서 모델의 성능이 달라질 수 있음
        - 주어진 파라미터고, 학습의 대상은 아니지만 성능에는 영향을 미치는 것을 하이퍼파라미터라고 함

    - 거의 대부분은 모델이, 동일한 모델 안에서도 그 모델을 튜닝해줌으로써 성능을 개선할 수 있는 여지가 있음
    - 이 때 모델을 어떻게 튜닝할까를 위해서도 따로 떼어놓음
    - Training 데이터라고 해도, f를 찾는 훈련용 데이터가 있고, 내 모델을 튜닝하는데 사용하는 validation 데이터가 있게 되는 것

    - ![image-20220211001843164](C:\Users\chgeo\AppData\Roaming\Typora\typora-user-images\image-20220211001843164.png)

    - 알파가 0인 경우의 f(), 0.5인 경우의 f(), 1인 경우의 f()

    - 이 3가지 모델을 각각 training으로 학습을 하고, 어떤 알파를 써야 가장 좋을까를 평가할 때 이 Validation 데이터를 사용함

    - x를 f에 넣어서 y를 예측하고, 그 값을 validation의 y와 비교하면 어떤 알파값이 가장 적절한 하이퍼파라미터값인지 알아낼 수 있음
    - 똑같은 모델을 사용해도 x를 어떤 조합을 해서 만들까도 결정해줘야 함 이럴 때 검증용 데이터를 사용하는 사례


3. 평가 데이터 (Test data)

    - 훈련 및 검증 자료로 적합된 최종 모형이 미래에 주어질 새로운 자료에 대해 얼마나 좋은 성과를 갖는지를 평가하는데 사용되는 자료
    - 모델을 학습할 땐 관찰되면 안 됨
    - 학습을 통한 정확도(Accuracy)가 있고, 평가 데이터를 기준으로 계산한 Accuracy가 있음
    - 일반적으로 평가 데이터의 정확도는 훈련데이터보다 낮음. 성능이 일반적으로 떨어짐