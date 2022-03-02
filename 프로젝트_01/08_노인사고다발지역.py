# (예린님 자료)

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd

oldman = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/실습/01_프로젝트/20_oldman.csv')

oldman

oldman.columns

# 불필요한 컬럼 제거
oldman.drop(['사고다발지FID', '사고다발지ID', '법정동코드', '지점코드', '부상신고자수', '다발지역폴리곤'], axis=1, inplace=True)

oldman.head()

# 시도시군구명에서 서울특별시 삭제
oldman['시도시군구명'] = oldman['시도시군구명'].str.replace('서울특별시', '')
oldman.head()

# 문자열 데이터를 숫자로 변환

oldman['발생건수'] = pd.to_numeric(oldman['발생건수'])
oldman['사상자수'] = pd.to_numeric(oldman['사상자수'])
oldman['사망자수'] = pd.to_numeric(oldman['사망자수'])
oldman['중상자수'] = pd.to_numeric(oldman['중상자수'])
oldman['경도'] = pd.to_numeric(oldman['경도'])
oldman['위도'] = pd.to_numeric(oldman['위도'])

## 지역별 사고다발 지점, 발생건수, 사상자수, 사망자수

oldman

# 전체 데이터의 평균, 표준편차, 사분위수, 최소값, 최대값 확인
oldman.describe()

oldman_set = oldman.set_index(['시도시군구명', '지점명'])
oldman_set

# 각 지역별 사고다발지점에서의 사고 발생건수 및 사상자수의 합
oldman_sum = oldman.groupby('시도시군구명').sum()
oldman_sum = oldman_sum.reset_index()
oldman_sum

### 서울시 전체 데이터와 비교

accident = pd.read_csv('/content/drive/MyDrive/[D9&10] 데이터시각화 프로젝트_5조/Data/2020_노인교통사고현황.csv')
accident.head()

# 사망자수와 부상자수를 합하여 사상자수 컬럼 생성
accident['사상자수'] = accident['사망자수']+accident['부상자수']
accident.head()

# 연산을 위해 '지역'컬럼을 오름차순 정렬 후 reset_index 후 'index' 컬럼 제거
accident = accident.sort_values('지역').reset_index().drop('index', axis=1)
accident.head()

# (사고다발지역 사상자수)/(전체 사상자수) -> 사고다발지역의 사상자수가 전체 사상자수에서 차지하는 비율
oldman_sum['사고다발지역 사상자수 비율'] = round(oldman_sum['사상자수'] / accident['사상자수'] * 100, 2)
oldman_sum

## 그래프

import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib import font_manager, rcParams
!apt-get install fonts-nanum*
rcParams['font.family'] = 'NanumGothicCoding'
rcParams['axes.unicode_minus'] = False
font_manager._rebuild()

### 지역별 발생건수, 사상자수, 사망자수

oldman.groupby('시도시군구명').sum()['발생건수'].sort_values(ascending=False)

oldman.groupby('시도시군구명').sum()['사상자수'].sort_values(ascending=False)

### 지역별 사고다발지역 수

# 각 구별 사고다발지역 수 확인

oldman_count = oldman.groupby('시도시군구명').count()
oldman_count = oldman_count.reset_index()
oldman_count

plt.figure( figsize=(30,5) )
sns.barplot(data=oldman_count, x='시도시군구명', y='지점명', ci=False)
plt.show()

oldman_count['지점명'].sort_values(ascending=False)

# 사고다발지역수 상위 3구

print(oldman['시도시군구명'][24], oldman['시도시군구명'][16], oldman['시도시군구명'][10])


### 지점별 사고발생건수, 사상자수

oldman.sort_values(['발생건수'], ascending=False)

oldman.sort_values(['사상자수'], ascending=False)

plt.hist(oldman['발생건수'], bins=11)
plt.show()

### 사고다발지역 사상자수 비율

plt.figure( figsize=(30,5) )
sns.barplot(data=oldman_sum, x='시도시군구명', y='사고다발지역 사상자수 비율', ci=False)
plt.show()

## 사고다발지역 지점 지도 시각화

import folium

from folium.plugins import MarkerCluster

location = []

for i in oldman.index:
  location.append([oldman.loc[i,'위도'], oldman.loc[i,'경도'] ])

map = folium.Map( location = [37.53, 127], zoom_start=12, tiles="cartodbpositron" )
MarkerCluster( location, overlay=True).add_to(map)
map

### 사고 발생건수+사상자수
- 사고 발생건수와 사상자수의 합 상위 13개 지점을 로드뷰를 통하여 분석하였으며 주로 다음과 같은 특징이 존재
 - 교차로
 - 시장(전통시장, 도매시장, 상가)
 - 신호등이 없는 횡단보도(무신호 횡단로)
 - 병원
 - 기타(주택가에 위치, 고가도로)

- 이러한 특징들을 변수로 하여 보행노인사고와의 인과관계를 분석해 볼 수 있지 않을까?
- (사고발생지점의 특징이 주어졌을 때 노인보행자 교통사고가 발생할 확률을 구해보는 것도 재미있을 것 같다. 근데 할 수 있을진 모르겠음)

### 사고다발지역+노인보호구역

silverzone = pd.read_csv('/content/drive/MyDrive/[D9&10] 데이터시각화 프로젝트_5조/Data/silverzone.csv')
silverzone.head()

len(silverzone)

from folium import Circle

m = folium.Map(location=[37.58, 127.0], tiles="cartodbpositron", zoom_start=11)

# 지도에 사고다발지점 표시(빨간색 원, 반경 200미터)
for i in oldman.index :
    folium.Circle(
        location = oldman.loc[i, ['위도', '경도']],
        radius = 200,
        color = 'red'
    ).add_to(m)

# 지도에 노인보호구역 표시(파란색 원, 반경 300미터)
for i in silverzone.index :
    folium.Circle(
        location = silverzone.loc[i, ['위도', '경도']],
        radius = 300,
        color = 'dodgerblue'
    ).add_to(m)


m

- 서울시 전체 노인보호구역 145곳 중 17곳이 사고다발지역을 포함
 - 사고다발지역에 추가로 노인보호구역을 지정할 필요가 있음 
- 노인보호구역으로 지정되었음에도 불구하고 사고다발지역인 지점 존재
 - 노인보호구역에 대한 인식 재고 및 사후관리 필요

 ### 사고다발지역 + 고령인구비율

population = pd.read_csv('/content/drive/MyDrive/[D9&10] 데이터시각화 프로젝트_5조/Data/2020_고령인구비율.csv', encoding='cp949')
population 

import json
geojson = json.load(open('/content/drive/MyDrive/멀티캠퍼스/seoulsigungu.geojson'))

# 행정구역별 고령인구비율

m = folium.Map(location=[37.58, 127.0], tiles="cartodbpositron", zoom_start=11)

folium.Choropleth(
  geo_data = geojson,
  data = population,
  columns = ['행정구역별', '고령인구비율'],
  fill_color='YlOrBr',
  key_on = 'properties.SIG_KOR_NM'
).add_to(m)

# 사고다발지점(빨간색 원)
for i in oldman.index :
    folium.Circle(
        location = oldman.loc[i, ['위도', '경도']],
        radius = 100,
        color = 'red'
    ).add_to(m)

m

plt.scatter(x=population['고령인구비율'], y=oldman_count['지점명'])
plt.xlabel('지역별 고령인구비율')
plt.ylabel('지역별 사고다발지점수')
plt.show()


- 산점도를 그려본 결과 지역별 '고령인구비율'과 '사고다발지역 지점수'간에 상관관계는 없는 것으로 보인다.

### 사고다발지역 + 65세이상 인구수

m = folium.Map(location=[37.58, 127.0], tiles="cartodbpositron", zoom_start=11)

# 행정구역별 65세이상 인구수
#folium.Choropleth(
#  geo_data = geojson,
#  data = population,
#  columns = ['행정구역별', '65세이상인구'],
#  fill_color='YlOrBr',
#  key_on = 'properties.SIG_KOR_NM'
#).add_to(m)

# 사고다발지점(빨간색 원)
for i in oldman.index :
    folium.Circle(
        location = oldman.loc[i, ['위도', '경도']],
        radius = 100,
        color = 'red'
    ).add_to(m)

m




plt.scatter(x=population['65세이상인구'], y=oldman_count['지점명'])
plt.xlabel('지역별 65세이상 인구수')
plt.ylabel('지역별 사고다발 지점수')
plt.show()

- 산점도를 그려본 결과 마찬가지로 지역별 '65세이상 인구수'와 '사고다발지역 지점수'간에 상관관계는 없는 것으로 보인다. 
 - 특정 지점에서의 잦은 사고발생이 노인 인구 분포와는 상관이 없으며, 다른 연관된 변수가 존재한다고 볼 수 있을 것 같다.


 ## 데이터 설명
- 사고다발지점의 위도,경도 데이터를 이용하여 구글 지도에서 스트리트뷰를 확인하여 변수를 정성분석.
- '교차로', '시장', '무신호 횡단로', '병원'을 독립변수, '사고발생건수'를 종속변수로 하여 분석을 시행해보자.

```
발생건수가 4 이상인 지점을 정성분석한 데이터
(사고다발지점 전체데이터의 발생건수의 평균이 약 '4.12'이기 때문에 발생건수가 4 이상인 지점까지 분석.)
- 독립변수는 모두 범주형 변수이며 변수가 존재하는 경우 1, 그렇지 않은 경우 0으로 표기
- 보행노인사고다발지역 데이터(2020)와 구글 지도에서 제공하는 스트리트뷰에는 시차가 존재하고, 
  지마음대로 변수 설정하고 정성분석 했기 때문에 통계적으로는 무의미...
  따라서 '이런 식으로 노인보행자 교통사고의 원인을 찾아볼 수도 있겠구나! 근데 머리가 나쁘면 몸이 고생하는구나!'하고 참고해주시면 됩니다 흑흑
```

### 데이터 확인

variable = pd.read_csv('/content/drive/MyDrive/[D9&10] 데이터시각화 프로젝트_5조/Data/variable.csv')
variable

variable.describe()

round(pd.DataFrame(variable.describe().loc['mean']).T, 2)

round(pd.DataFrame(variable[variable['발생건수'] > 4.98].describe().loc['mean']).T, 2)

variable[variable['발생건수'] < 4.98].mean()

round(pd.DataFrame(variable[variable['발생건수'] < 4.98].describe().loc['mean']).T, 2)

- 발생건수가 평균발생건수(4.98)보다 높은 지점의 경우 평균발생건수보다 낮은 지점에 비해 사고다발지점에 시장이 위치해있는 경우가 상대적으로 더 많음.

variable[variable['발생건수'] < 4.98].describe()

- 발생건수가 평균발생건수(4.98)보다 낮은 지점의 경우 평균발생건수보다 높은 지점에 비해 무신호횡단로가 있는 경우가 상대적으로 더 많음.
 - 무신호횡단로에 신호등을 설치하면 사고발생을 크게 줄일 수 있을 것으로 예상됨

print('시장이 있는 지점의 수:', len(variable[variable['시장'] == 1]))
print('시장과 교차로가 함께 있는 지점의 수:', variable['시장'][variable['교차로'] == 1].sum())

- 인근에 시장이 있는 사고지점에 교차로가 있는 경우 전체에서 약 78.95%의 비율을 차지하며, 노인 유동인구가 많을 것으로 추정되는 지점에 교통량 또한 많을 것으로 예상.
 - 노인 유동인구가 많은 지점에서 노인보행자 보호를 위한 대책이 필요


 #### 다중,,회귀분석,,
- 이건 그냥 재미로 돌려본거라 재미로 보시고 ppt엔 넣지 마세요,,

import statsmodels.api as sm

x_variable = variable[['교차로', '시장', '무신호횡단로', '병원']]

y = variable['발생건수']

multi_model = sm.OLS(y, x_variable)
fitted_multi_model = multi_model.fit()


fitted_multi_model.summary()

from statsmodels.stats.outliers_influence import variance_inflation_factor

vif = pd.DataFrame()
vif['VIF'] = [variance_inflation_factor(x_variable.values, i) for i in range(x_variable.shape[1])]
vif['variable'] = x_variable.columns
vif

- 회귀분석 돌렸더니 모든 변수의 p-value값이 0.05이하다..! 감히 각 변수가 발생건수에 유의미한 영향을 준다고 봐도 되는건지ㅋㅋ
- 수정된 결정계수도 무려 0.762이다. 
- Prob(omnibus)도 유의수준인 0.05를 훨씬 웃도는 수치라 잔차항이 정규분포를 따른다고 볼 수 있다.
- 왜도(Skew), 첨도(Kurtosis)도 정규성을 만족..
- 심지어 VIF도 전부 10 이하.. 다중공선성도 없다고?
- ㅋㅋㅋ웃긴다..

## 도로폭

road = pd.read_csv('/content/drive/MyDrive/[D9&10] 데이터시각화 프로젝트_5조/Data/road.csv')

road.head()

# 불필요한 컬럼 제거
road.drop(['Unnamed: 0', '시군구코드', 'CCTV설치여부', 'CCTV설치대수','제한속도'], axis=1, inplace=True)

road.head()

road.info()

road.describe()

# 도로폭이 평균 이상인 지점
road[road['보호구역도로폭'] > 10.26]

m = folium.Map(location=[37.58, 127.0], tiles="cartodbpositron", zoom_start=11)

# 지도에 사고다발지점 표시(빨간색 원, 반경 200미터)
for i in oldman.index :
    folium.Circle(
        location = oldman.loc[i, ['위도', '경도']],
        radius = 200,
        color = 'red'
    ).add_to(m)

# 지도에 노인보호구역 표시(파란색 원, 반경 300미터)
for i in silverzone.index :
    folium.Circle(
        location = silverzone.loc[i, ['위도', '경도']],
        radius = 300,
        color = 'dodgerblue'
    ).add_to(m)

# 지도에 도로 표시(노란색원)
for i in road.index :
    folium.Circle(
        location = road.loc[i, ['위도', '경도']],
        radius = 100,
        color = 'yellow'
    ).add_to(m)
m

- 사고다발지점과 도로폭 좌표가 있는 지점이 겹치는 곳이 단 7곳!!!!!!!!1111
표본이 무려 7개다 이말이야!!!!!!!!!!!!!!!!!!!!111111111
노인보호구역 원 데이터에는 노인보행자사고 관련 데이터는 없다!!!!!!!!!!!1111
도로폭 좌표는 사고다발지점이 아닌, 노인보호구역좌표라 심지어 정확히 일치하는 것도 아니다!!!!!!!!!!111111111111!!!!!!11111
 - 여러 논문을 보면 도로폭과 노인보행자사고 발생은 상관관계가 있지만 지금 현재 가지고 있는 데이터만으로는 이러한 결론을 이끌어 낼 수 가 없다

 