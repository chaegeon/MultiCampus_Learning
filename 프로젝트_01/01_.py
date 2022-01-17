# !pip install xmltodict #

import pandas as pd
import numpy as np
import requests
import xmltodict

from google.colab import drive
drive.mount('/content/drive')

oecd = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/실습/Data폴더/oecd_killed.csv')
oecd
# 2020년 자료/ oecd 65세 이상 보행자 교통사고 사망자
# 그래프에 //단위: 명/10만명// 추가할 것
# 가능하면 oecd국들의 평균도 추가할 것

# 출처: https://stats.oecd.org/

# 불필요한 컬럼 삭제
oecd = oecd.drop(columns=['AGE_GROUP', 'Year'])

oecd

# 컬럼이름이 너무 길어서 편의상 줄임
oecd = oecd.rename(columns={'Per 100000 inhabitants' : 'Per'})
oecd

oecd.columns

# 그래프 그리기를 대비해 데이터 정렬
oecd = oecd.sort_values('Per',ascending=False)
oecd

Country = oecd['Country'].values.tolist()
Country

Per = oecd['Per'].values.tolist()
Per





# 시각화
- 그래프에 **단위: 명/10만명** 추가할 것
- 가능하면 oecd국들의 **평균**도 추가할 것

import matplotlib.pyplot as plt
import seaborn as sns

#한글화 설정
from matplotlib import font_manager, rcParams
!apt-get install fonts-nanum*
rcParams['font.family'] = 'NanumGothicCoding'
rcParams['axes.unicode_minus'] = False
font_manager._rebuild()

plt.figure(figsize=(20,5))
n_data = len(Country)
index = np.arange(len(Country))
sns.barplot(Country,Per)

plt.ylabel('사망자 비율')
plt.grid(True, alpha = 0.5, axis = 'y')
plt.show() 

# 그래프에 추가할 평균선 평균 구하기
import numpy
arr = Per
average = numpy.mean(arr)
print(average)


average

plt.figure(figsize=(20,5))
n_data = len(Country)
index = np.arange(len(Country))
plt.bar(Country,Per)

plt.legend()
plt.ylabel('사망자 비율')
plt.grid(True, alpha = 0.5, axis = 'y')

plt.axhline( y = average, color='r', linewidth = 1, label='평균') # 평균값을 구한 average 평균선 추가하기
plt.title('OECD국가별 10만명당 노인보행 중 사망자 수')
plt.show() 

# 텍스트를 추가항 설명 보충
plt.figure(figsize=(20,5))
n_data = len(Country)
index = np.arange(len(Country))
plt.bar(Country,Per)

plt.legend()
plt.ylabel('사망자 비율')
plt.grid(True, alpha = 0.5, axis = 'y')

plt.axhline( y = average, color='r', linewidth = 1) # 평균값을 구한 average 평균선 추가하기
plt.title('OECD국가별 10만명당 노인보행 중 사망자 수')

plt.text(20.3 ,6.5,'OECD 평균: 6.2명', color='r', verticalalignment='bottom' , horizontalalignment='center' )
plt.text(20.3 ,16.5,'단위: 명/10만 명', verticalalignment='bottom' , horizontalalignment='center' )

plt.show() 



# 테스트

plt.figure(figsize=(20,5))
n_data = len(Country)
index = np.arange(len(Country))
sns.countplot(x = 'Country', data = oecd, order = oecd['Country'].value_counts().index)

plt.ylabel('사망자 비율')
plt.show()

oecd1 =  oecd.set_index([Country])
oecd1 = oecd1.drop( columns = ['Country'])

oecd1

plt.figure(figsize=(20,5))
n_data = len(Country2)
index = np.arange(len(Country2))
sns.barplot(Country2,Per2)

plt.ylabel('사망자 비율')
plt.show()