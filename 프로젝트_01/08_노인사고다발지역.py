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

 ## 참조

###[지정하면 뭐하나…'있으나마나' 노인보호구역](https://imnews.imbc.com/replay/2021/nwdesk/article/6078947_34936.html)
- 도로교통법은 노인보호구역에서 운전자가 노인 또는 장애인의 안전에 유의해 운행하도록 권고할 뿐 단속용 장비 설치 등을 강제하지는 않습니다.
- 사고 지점도 통행량이 많다는 이유로 제한속도가 시속 30km가 아닌 50km로 완화됐고, 과속 단속 카메라가 설치돼 있지 않았습니다.
- 노인보호구역의 경우 과속을 하더라도 가중처벌도 없습니다,
- "노인보호구역에서 어르신 치상 사고는요 단서조항도 있지 않아서 형사처벌에 대한 별도 규정은 제정돼있지 않습니다."

[② 노인 보호 못 하는 노인보호구역](https://news.sbs.co.kr/news/endPage.do?news_id=N1005877565)

[서울시, 전통시장 노인보호구역 청사진 내놓고 6개월째 무소식](https://bravo.etoday.co.kr/view/atc_view.php?varAtcId=12827)

### [늘어나는 노인 교통사고 안전대책 강화해야](http://www.ggilbo.com/news/articleView.html?idxno=853022)
- 도로교통공단의 자료에 따르면 2019년 노인 보행자 교통사고는 어린이 대비 3.2배에 달하고 사망자는 무려 37배가 넘는다. 

- 올해(2021년) 스쿨존 개선 예산이 1983억 원 실버존 개선에는 60억 원의 예산

- 2019년 기준 어린이보호구역은 1만 6912개인 데 반해 노인보호구역은 고작 1932개만 지정

- 우리나라 인구변화 추이를 보면 앞으로 노인인구는 꾸준히 증가해 고령자 비중이 높아질 것으로 전망 ... 우리나라는 앞으로 4년 안에 초고령 사회에 진입할 것으로 예상
 - 고령자 교통사고도 늘어날 가능성 증가

- 실버존 지정을 확대하는 한편 감시카메라 설치 등 관리를 강화하는 등 노인 교통안전 대책 필요. 
- 노인 생활과 보행 속도에 맞는 보호장치 개선

### [횡단보도 신호시간 늘렸더니…"노인 보행자 사고 예방에 효과"](https://www.yna.co.kr/view/AKR20200707154800061)
- 경기남부청에 따르면 보행 신호 연장 이후(19년 4월 6일∼20년 4월 5일) 이들 횡단보도에서 발생한 노인 보행자 교통사고는 416건으로, 연장 이전(18년 4월 6일∼19년 4월 5일)에 발생한 407건보다 9건(2.2%)이 감소

- 사망자는 28명에서 24명으로 14.3%, 부상자는 381명에서 378명으로 0.8% 정도 감소

- 정책이 추진된 지 약 1년밖에 되지 않아 수치로 봤을 때 감소 폭이 작아 보일 수 있으나, 사고 예방 효과 기대

- 한국교통연구원에 따르면 우리나라 노인 10만명당 교통사고 사망자 수는 22명으로 14세 이하 어린이(0.6명)와 15∼64세 청·장년(5.5명)보다 많음.

- 노인 교통사고 사망자의 절반 이상은 '보행 중' 사고를 당한 것으로 집계


### 고령자 보행특성 분석 및 교통사고 예방대책 연구(2016-0104-067)
```
7) 지역별 고령보행자 교통사고
2005년부터 2014년까지 고령보행자 교통사고를 지역별로 살펴보면 발생건수는 서
울 1,580건(18.2%), 경기 1,426건(16.5%), 부산 652건(7.5%), 경북 651건(7.5%), 경남 614
건(7.1%) 순으로 많은 것으로 나타났으며, 울산 154건(1.8%), 제주 152건(1.8%), 세종
14건(0.2%)으로 가장 적었다. 사망자수는 경기 158명(16.7%), 서울 95명(10.0%), 경북
94명(9.9%), 경남 79명(7.1%) 순으로 많이 발생했으며, 제주 20명(2.1%), 울산 16명
(1.7%), 세종 1명(0.1%)으로 가장 적었다. 이와 같은 결과는 서울, 부산 등 대도시에서
는 인구와 차량이 집중되어 발생건수 및 사망자수가 많은 것으로 볼 수 있다. 그러
나 치사율은 충남 17.4, 전남 16.1, 충북 15.0, 경북 14.5, 제주 13.0 순이었으며, 대구
7.5, 부산 7.0, 서울 6.0으로 가장 적었다. 이는 대도시에서 발생건수 및 사망자수가
많고, 치사율이 낮은 것은 지방 중소도시보다 상대적으로 인구와 운행되는 차량이
많아 도로정체 구간이 많고 차량의 속도도 낮기 때문인 것으로 보인다.
```
- 노인 보행자 교통사고 감소를 위해 차량 속도 제한이 필요할 것으로 생각

```
2005년부터 2014년까지 전체 보행 교통사고와 고령보행자 교통사고를 도로형태별
로 구분하여 <표 2-23>에 제시하였다. 발생건수는 고령보행자 교통사고와 마찬가지
로 단일로에서 34,328건(69,7%)으로 가장 많았고, 이어서 교차로 12,037건(24.4%), 기
타/불명 2,873건(5.8%)를 차지하고 있다. 사망자수 역시 단일로에서 1,574명(72,8%)으
로 가장 많았고, 이어서 교차로 510명(23.6%), 기타/불명 75명(3.5%)를 차지하고 있다.
치사율은 단일로 4.6, 교차로 4.2으로 비슷했으며, 기타/불명 2.6으로 나타났다. 단일
로에서의 교통사고를 세부적으로 살펴보면 발생건수 및 사망자수 모두 기타 단일로,
횡단보도상, 횡단보도 부근, 교량위, 터널안 순으로 나타나 고령보행자 교통사고와
비슷한 경향을 보이고 있으며 각각의 비중도 비슷하다. 반면에 치사율은 교량위에서
9.8, 터널안에서 9.1, 기타 단일로에서 4.8이었고, 횡단보도 부근에서 4.7, 횡단보도상
에서 3.4 순으로 나타났다. 전체 보행 교통사고와 고령보행자 교통사고의 치사율을
비교할 때 터널안을 제외하고 횡단보도상, 횡단보도 부근이나 기타 단일로에서는 고
령보행자 교통사고의 치사율이 2배 이상 높았다. 이는 고령보행자의 신체능력 저하
가 영향을 미친 것으로 보인다. 또한 고령보행자가 횡단보도 부근에서 무단횡단을
많이 하는 것도 원인 중 하나라고 볼 수 있다.
```
- 횡단 중에 주로 교통사고가 발생하며, 고령보행자의 신체능력 저하로 인한 도로 횡단시간 증가, 무단횡단 등이 주요 원인으로 보임
 - 보행신호의 시간을 늘리고, 무단횡단을 막을 수 있는 방안이 필요해 보임

### 고령보행자 교통사고 유발행동 분석 및 교통사고 감소방안(수시-18-01.)
```
2) 보행행태
 1. 보행시간 및 보행목적
고령자의 보행 시간은 하루 평균 60분 이상 갖는다고 응답한 사람이 많은
반면, 비고령자는 15~30분 보행한다고 응답한 사람이 많았다.
각각의 목적으로는 비고령자의 경우 기타를 제외했을 때 통근(통학)이라고
응답한 반면, 고령자의 경우 운동이 보행의 목적이라고 응답하였다.
 2. 횡단보도 횡단횟수
비고령자와 고령자의 일평균 횡단보도 횡단 횟수를 조사한 결과, 비고령자
는 4.4회, 고령자는 6.3회로 나타났다.
```
```
3) 횡단 교통사고 위험성
 3. 횡단 중 교통사고 경험
최근 5년 간 횡단 교통사고를 경험한 응답자는 비고령자 18명(7.2%), 고령
자 34명(18.9%)으로 비고령자의 비중이 높게 나타났다.
```

```
다. 종합 분석 및 시사점
고령보행자의 교통사고 유발행동 설문조사 및 현장 실태조사 결과 다음과
같은 고령보행자의 특성을 도출할 수 있었다.

- 고령보행자는 교통사고에 대한 노출도가 더 높다
- 고령보행자는 건강목적의 보행활동이 많다.
- 고령보행자는 보행활동 중 판단오류를 일으킬 가능성이 높다.
- 고령자의 무단횡단 횟수가 더 많다.
- 고령자의 보행경로가 다양하고 주거지 인근의 사고가 많다.
- 횡단보도 상에 횡단쉼터를 설치하면 보다 안전한 보행행태를 보인다.
- 횡단쉼터에 별도로 신호를 설치하는 것이 더 안전한 보행환경을 제공한다.
- 횡단거리가 긴 횡단보도에서 고령자는 매우 불안정한 횡단행태를 보인다.
```
- 고령 보행자들이 건강목적의 보행을 위해 주로 어떤 곳을 방문할까?
 - 이러한 곳을 보호구역으로 설정하는 것은 어떨까

```
나. 고령보행자 교통사고 감소 방안
1) 보행섬의 설치 확대
현행 어린이·노인·장애인 보호구역 통합지침에 노인 보호구역 내 우선 고려
할 시설에 보행섬을 추가할 필요가 있다. 보행섬은 횡단보도를 건널 때 안전하
게 대피할 수 있도록 공간을 제공하며, 도로를 다 건너지 못했을 때는 대기공
간에서 안전하게 쉬었다가 건널 수 있게 한다. 또한, 보행섬을 설치하면 좁아
진 차로로 인해 차량들의 속도를 낮추도록 유도할 수도 있다.

2) 노인 보호구역의 설치 기준 설정
현재 어린이·노인·장애인 보호구역 통합지침에서는 고령자 수용인구 또는
고령 보행 교통량 등을 기준으로 제시하고 있지 않기 때문에, 노인 보호구역의
설치 우선순위에 대한 정량적 기준을 제시하여, 고령보행자와 교통량이 많은
곳에 고령보행자에게 특화된 교통안전 시설을 설치하는 방안이 필요하다.
```
- 사고다발지역+노인보호구역 시각화 자료를 이용하여 고령보행자와 교통량이 많은
곳에 보호구역을 설치하자고 주장하자

```
라. 무단횡단
무단횡단은 법적으로 정의되는 행동은 아니지만, 일반적으로 횡단보도에서
접근 차량이 없으면 적색신호에 횡단을 하는 경우와 횡단보도가 아닌 곳에서
의 횡단으로 규정하고 두 가지 문항에 대해 5점 척도로 조사하였다. 무단횡단
의 경우 운전자의 입장에서는 예상치 못한 돌발 상황으로 인해 사고로 이어질
가능성이 매우 높다는 점에서 이에 대해 질문하였다.
그 결과 두 가지 경우 모두에서 전반적으로 무단횡단을 적게 하는 것으로
응답하였으나, 집단 간의 차이에서는 비고령자가 고령자에 비해 무단횡단을
더 많이 하는 것으로 나타났다. 일반적으로는 고령자 집단의 무단횡단 사고
비율이 높은 것으로 알려져 있다. 그러나 본 설문의 결과에서 보면 전반적으로
는 적게 하는 것으로 평가되었으나, 고령자가 비고령자에 비해 더욱더 적게
하는 것으로 나타났다. 이러한 결과는 실제 행동패턴에 대한 확인이 필요하나,
**무단횡단 비율이 낮은 고령자가 사고비율이 높다는 점에서 운동능력 등 신체
기능의 저하를 유추할 수 있을 것으로 보인다.**
```
- 놀랍게도 고령자가 비고령자보다 무단횡단을 적게한다..!!! 앞선 논문에서 내렸던 결론과는 달리, 무단횡단이 높은 노인보행자 교통사고에 가장 주요한 변수가 아닐 수도 있겠다는 생각이 들었다.
 - 노인의 신체 능력 저하가 가장 주요한 변수일까?

```
<고령자의 보행경로가 다양하고 주거지 인근의 사고가 많다.>
제2장 제2절에서 살펴 본 고령자의 보행 통행 특성에 관한 일본의 조사 결
과를 보면 고령보행자는 외출목적이 다양하고 활용하는 도로가 다양하다. 고
령보행자는 상대적으로 여가시간이 많으므로 비고령보행자 보다 활동 범위가
다양하고 보행 목적에 따라 매일 다른 도로를 횡단하는 것으로 나타난다. 또한
고령보행자의 교통사고가 가장 많이 발생하는 지역은 자택반경 500m 이내 인
것으로 조사되었다. 이와 같은 일본의 사례를 볼 때, 고령보행자의 교통사고
예방 대책은 특정 지점이나 경로를 중심으로 시행하는 것의 효과가 떨어지며
전체 보행자 관점에서 개선대책을 세울 필요가 있음을 시사한다. 지역적으로
는 통행의 출발점이 되고 통행 빈도가 가장 높은 주거지역의 보행 교통사고
대책에 중점을 둘 필요가 있음을 보여 주고 있다.
```
- 노인의 주거비율이 높은 지역에 보호구역을 설치하는 방안?