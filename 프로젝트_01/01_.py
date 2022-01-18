### !pip install xmltodict

import pandas as pd
import numpy as np
import requests
import xmltodict

from google.colab import drive
drive.mount('/content/drive')

oecd = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/실습/Data폴더/oecd_killed.csv')
oecd
# 2020년 자료/ oecd 65세 이상 보행자 교통사고 사망자
# 그래프에 //단위: 명/10만명// 이라는 설명을 추가할 것
# oecd국들의 평균도 추가해볼 것

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

# 평균값을 구한 average 평균선 추가해보기
plt.figure(figsize=(20,5))
n_data = len(Country)
index = np.arange(len(Country))
plt.bar(Country,Per)

plt.legend()
plt.ylabel('사망자 비율')
plt.grid(True, alpha = 0.5, axis = 'y')

plt.axhline( y = average, color='r', linewidth = 1, label='평균') 
plt.title('OECD국가별 10만명당 노인보행 중 사망자 수')
plt.show() 

# average값으로 평균선 추가하기
# 그래프 내의 여백 정리
# 그래프 내에 텍스트를 추가하여 설명 보충
plt.figure(figsize=(23,5))
n_data = len(Country)
index = np.arange(len(Country))
plt.bar(Country,Per)

plt.legend()
plt.ylabel('사망자 비율')
plt.grid(True, alpha = 0.5, axis = 'y')
plt.margins(x=0.01)

plt.axhline( y = average, color='r', linewidth = 1) 
plt.title('OECD국가별 10만명당 노인보행 중 사망자 수')

plt.text(19.6, 6.5,'OECD 평균: 6.2명', color='r', verticalalignment='bottom' , horizontalalignment='center' )

plt.show() 

# average값으로 평균선 추가하기
# 값을 소수점 첫째자리까지 표시
# 그래프 내에 텍스트를 추가하여 설명 보충
plt.figure(figsize=(23,5))
n_data = len(Country)
index = np.arange(len(Country))
plt.bar(Country,Per)

plt.legend()
plt.ylabel('사망자 비율')
plt.grid(True, alpha = 0.5, axis = 'y')
plt.margins(x=0.01)

plt.axhline( y = average, color='r', linewidth = 1) 
plt.title('OECD국가별 10만명당 노인보행 중 사망자 수')

for i in range( len(Country)):
  plt.text( i, Per[i]/2, '%.1f'% Per[i], ha = 'center', va='bottom', color = 'w', size=15)

plt.text(19.6, 6.5,'OECD 평균: 6.2명', color='r', verticalalignment='bottom' , horizontalalignment='center' )
plt.text(19.7, 16.3,'노인: 65세 이상', verticalalignment='bottom' , horizontalalignment='center' )
plt.text(19.74, 15.1,'단위: 명/10만 명', verticalalignment='bottom' , horizontalalignment='center' )

plt.show() 









# 연습

s

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

plt.figure(figsize=(20,5))
n_data = len(Country)
index = np.arange(len(Country))
sns.countplot(x = index, data = oecd1)

plt.ylabel('사망자 비율')
plt.show()

oecd2 = oecd.sort_values('Per',ascending=True)
oecd2



Country2 = oecd2['Country'].values.tolist()
Country2

Per2 = oecd2['Per'].values.tolist()
Per2

Per

plt.barh( average)
plt.show()


fig, ax1 = plt.subplots()

ax1.plot(Country, Per, '-s', color='green', markersize=7, linewidth=5, alpha=0.7, )
ax1.set_ylim(0, 18)
ax1.set_xlabel('Country')
ax1.set_ylabel('Per')
ax1.tick_params(axis='both', direction='in')

ax2 = ax1.twinx()
ax2.bar(Counrty, average, color='deeppink', label='Demand', alpha=0.7, width=0.7)
ax2.set_ylim(0, 18)
ax2.set_ylabel(r'Demand ($\times10^6$)')
ax2.tick_params(axis='y', direction='in')







fig = plt.figure(figsize=(20,5))
ax = fig.add_subplot()
n_data = len(Country)
index = np.arange(len(Country))
sns.barplot(Country,Per)

plt.legend()
plt.ylabel('사망자 비율')
plt.grid(True, alpha = 0.5, axis = 'y')

for i, b in enumerate(Country):
    ax.text(b.get_x()+b.get_width()*(1/2),b.get_height()+0.1, \
            Per[i],ha='center',fontsize=13)

# 평균값을 구한 average 평균선 추가하기
plt.axhline( y = average, color='r', linewidth = 1 )
plt.show() 

for i, b in enumerate(bars):
    ax.text(b.get_x()+b.get_width()*(1/2),b.get_height()+0.1, \
            num_patient[i],ha='center',fontsize=13)

fig = plt.figure(figsize=(20,5))

x = Country
y = Per
bar = sns.barplot(x, y)
plt.ylim(0,18)

for i in len(index):
  height = rect.get_height()
  plt.text(rect.get_x() + rect.get_width() / 2.0, height, '%.1f'% height, ha='center', va = 'bottom', size = 12)

# 평균값을 구한 average 평균선 추가하기
plt.axhline( y = average, color='r', linewidth = 1 )
plt.show() 

fig = plt.figure(figsize=(20,5))
ax = fig.add_subplot()
n_data = len(Country)
index = np.arange(len(Country))
sns.barplot(Country,Per)

plt.legend()
plt.ylabel('사망자 비율')
plt.grid(True, alpha = 0.5, axis = 'y')

for rec in bar:
  height = rect.get_height()
  plt.text(rect.get_x() + rect.get_width() / 2.0, height, '%.1f'% height, ha='center', va = 'bottom', size = 12)

# 평균값을 구한 average 평균선 추가하기
plt.axhline( y = average, color='r', linewidth = 1 )
plt.show() 

fig = plt.figure(figsize=(20,5))

x = Country
y = Per
bar = sns.barplot(x, y)
plt.ylim(0,18)

for i in range( len(Country)):
  Per_r = Per[i]
  plt.text( i, 'Per/2', 'Per', va = 'center', ha='center')
  
#for i in range(len(Country)):
  
  #plt.text(i, 'Per/2', "Per", va='center', ha='center')

# 평균값을 구한 average 평균선 추가하기
plt.axhline( y = average, color='r', linewidth = 1 )
plt.show() 



