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