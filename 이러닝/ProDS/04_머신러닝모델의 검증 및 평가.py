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
4. 훈련된 모델을 적용하여 **새로운 데이터**에 대한 **예측**을 수행 ( 새로운 데이터에 대한 예측력 : 일반화 능력)