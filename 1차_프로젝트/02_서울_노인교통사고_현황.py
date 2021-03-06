# 전처리

## !pip install xmltodict

import pandas as pd
import requests
import xmltodict

from google.colab import drive
drive.mount('/content/drive')

accident = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/실습/Data폴더/서울시 노인 교통사고 현황.csv')
accident
# 2020년 만 65세 이상의 노인 교통사고

# 출처: TAAS 교통사고분석시스템(http://taas.koroad.or.kr/)

accident.columns

# 컬럼명 수정
accident.columns=['Unnamed', '기간', '지역', '노인교통사고_발생건수', '노인교통사고_사망자수', '노인교통사고_부상자수', '노인운전자교통사고_발생건수', '노인운전자교통사고_사망자수', '노인운전자교통사고_부상자수', '노인보행자_사망자수', '노인보행자_부상자수']

accident.head(5)

# 불필요한 컬럼 삭제
accident = accident.drop(columns = ['Unnamed', '기간'])

accident.head(5)

# 컬럼명과 중복되는 행 삭제
accident = accident.drop(index=[0])

accident.head(5)

# 인덱스 변경
# accident = accident.set_index(['지역'])

accident.head(5) 

accident['노인교통사고_사망자수'].unique()

def func(x):
    if x == '-' :
      x = '0'

# 결측치가 문자열 '-'로 되어있다.
# 일단 결측치인 '-'값들을 같은 문자열 '0'으로 변경
accident = accident.apply(lambda x: x.replace('-','0'), axis=1)
accident

accident.dtypes

# 데이터들을 숫자타입으로 변경
# accident = accident.apply(pd.to_numeric) -> 한 번에 바꾸려 했으나 '지역' 때문에 불가능
accident = accident.astype({'노인교통사고_발생건수':int, '노인교통사고_사망자수':int, '노인교통사고_부상자수':int, '노인운전자교통사고_발생건수':int, '노인운전자교통사고_부상자수':int, '노인운전자교통사고_사망자수':int, '노인보행자_사망자수':int, '노인보행자_부상자수':int})

accident.dtypes

accident.info()

accident


# 시각화

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#한글화 설정
from matplotlib import font_manager, rcParams
!apt-get install fonts-nanum*
rcParams['font.family'] = 'NanumGothicCoding'
rcParams['axes.unicode_minus'] = False
font_manager._rebuild()

rawData = accident.drop(index=[1])
rawData.head(5)

rawData['지역']

rawData.columns

# '지역' 컬럼의 값들을 리스트로 변환
region = rawData['지역'].values.tolist()
region

death = rawData['노인보행자_사망자수'].values.tolist()
death

injury = rawData['노인보행자_부상자수'].values.tolist()
injury

# 지역별 부상자
plt.figure(figsize=(20,5))
n_data = len(region)
index = np.arange(len(region))
plt.bar(region,injury)
plt.show()
 
# 지역별 사망자
plt.figure(figsize=(20,5))
n_data = len(region)
index = np.arange(len(region))
plt.bar(region,death, color='r')
plt.show()

# 지역별 부상자 와 지역별 사망자 그래프 합치기
plt.figure(figsize=(28,5))
barWidth = 0.5
plt.bar(index, injury, color='c', width = barWidth, label='부상자')
plt.bar(index, death, color='r', width = barWidth, label='사망자')

plt.xticks( index, region )
plt.legend()
plt.xlabel('지역')
plt.ylabel('사상자수')
#plt.title('노인보행사고_사상자수')
plt.show()

# "부상자, 사망자"로 값을 표시
plt.figure(figsize=(25,10))
barWidth = 0.5
plt.bar(index, injury, color='c', width = barWidth, label='부상자')
plt.bar(index, death, color='r', width = barWidth, label='사망자')
plt.grid(True, alpha = 0.5, axis = 'y')

for i in range( len(region)):
  injury_r = injury[i]
  death_r = death[i]
  # plt.text( i+0.3, death[i], injury[i], '%d %/ %d')
  # plt.text( i-1, injury[i]+2, f'{death[i]}명 사망 / {injury[i]}명 부상')
  plt.text( i-0.6, injury[i]+2, f'부상{injury[i]},사망{death[i]}')


plt.xticks( index, region )
plt.legend()
plt.xlabel('지역')
plt.ylabel('사상자수')
plt.title('노인보행사고_사상자수')
plt.show()