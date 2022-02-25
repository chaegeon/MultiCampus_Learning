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