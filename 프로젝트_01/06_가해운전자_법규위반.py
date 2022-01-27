!pip install xmltodict

import pandas as pd
import requests
import xmltodict

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib import font_manager, rcParams
!apt-get install fonts-nanum*
rcParams['font.family'] = 'NanumGothicCoding'
rcParams['axes.unicode_minus'] = False
font_manager._rebuild()

# 전처리

from google.colab import drive
drive.mount('/content/drive')

rawData = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/실습/Data폴더/과속.csv')
rawData

rawData = rawData.drop(columns=['Unnamed: 0', '2'])
rawData

rawData['0'] = '과속_사고', '과속_사망', '과속_부상'
rawData

rawData1 = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/실습/Data폴더/교차로운행방법위반.csv')
rawData1

rawData1 = rawData1.drop(columns=['Unnamed: 0', '2'])
rawData1

rawData1['0'] = '교차로위반_사고', '교차로위반_사망', '교차로위반_부상'
rawData1



rawData2 = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/실습/Data폴더/기타.csv')
rawData2

rawData2 = rawData2.drop(columns=['Unnamed: 0', '2'])
rawData2

rawData2['0'] = '기타_사고', '기타_사망', '기타_부상'
rawData2



rawData3 = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/실습/Data폴더/보행자보호의무위반.csv')
rawData3

rawData3 = rawData3.drop(columns=['Unnamed: 0', '2'])
rawData3

rawData3['0'] = '보행자보호위반_사고', '보행자보호위반_사망', '보행자보호위반_부상'
rawData3



rawData4 = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/실습/Data폴더/부당한회전.csv')
rawData4

rawData4 = rawData4.drop(columns=['Unnamed: 0', '2'])
rawData4

rawData4['0'] = '부당한회전_사고', '부당한회전_사망', '부당한회전_부상'
rawData4



rawData5 = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/실습/Data폴더/신호위반.csv')
rawData5

rawData5 = rawData5.drop(columns=['Unnamed: 0', '2'])
rawData5

rawData5['0'] = '신호위반_사고', '신호위반_사망', '신호위반_부상'
rawData5



rawData6 = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/실습/Data폴더/안전운전의무불이행.csv')
rawData6

rawData6 = rawData6.drop(columns=['Unnamed: 0', '2'])
rawData6

rawData6['0'] = '안전운전불이행_사고', '안전운전불이행_사망', '안전운전불이행_부상'
rawData6



rawData7 = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/실습/Data폴더/중앙선침범.csv')
rawData7

rawData7 = rawData7.drop(columns=['Unnamed: 0', '2'])
rawData7

rawData7['0'] = '중앙선침범_사고', '중앙선침범_사망', '중앙선침범_부상'
rawData7

rawData = pd.merge(rawData, rawData1, left_index = True, right_index=True)
rawData

rawData = pd.merge(rawData, rawData2, left_index = True, right_index=True)
rawData

rawData = pd.merge(rawData, rawData3, left_index = True, right_index=True)
rawData

rawData = pd.merge(rawData, rawData4, left_index = True, right_index=True)
rawData

rawData = pd.merge(rawData, rawData5, left_index = True, right_index=True)
rawData

rawData = pd.merge(rawData, rawData6, left_index = True, right_index=True)
rawData

rawData = pd.merge(rawData, rawData7, left_index = True, right_index=True)
rawData

rawData.columns

rawData.columns = ['0', '과속', '0', '교차로위반', '0', '기타', '0','보행자보호위반','0','부당한회전','0','신호위반','0','안전운전불이행', '0','중앙선침범']

rawData

rawData = rawData.drop(columns=['0'])
rawData

rawData.index=['사고발생건수', '사망자수', '부상자수']
rawData

rawData = rawData.T
rawData

rawData = rawData.sort_values('사고발생건수',ascending=False)
rawData

rawData = rawData.reset_index()
rawData

rawData.columns=['위반유형', '사고발생건수', '사망자수', '부상자수']
rawData

a_type = rawData['위반유형'].values.tolist()

a_type

num = rawData['사고발생건수'].values.tolist()
num

death = rawData['사망자수'].values.tolist()
death

injury = rawData['부상자수'].values.tolist()
injury

accident = rawData.T
accident

accident.columns = ['안전운전불이행', '신호위반', '중앙선침범', '교차로위반', '기타', '보행자보호위반', '과속', '부당한회전']
accident

accident = accident.loc[['사고발생건수']]
accident

lab = rawData['위반유형']
lab

lab = lab.values.tolist()
lab

# 시각화

plt.figure(figsize=(20,10))
#explode : array-like, default None
wedgeprops = {'width':0.7, 'edgecolor':'w', 'linewidth':1}
explodes =(0.1 ,0,0,0,0,0,0,0)
plt.pie(accident, labels = rawData['위반유형'] ,autopct='%.1f%%',startangle=150, counterclock=False, wedgeprops=wedgeprops, explode=explodes)
plt.title('노인보행사고 중 가해운전자 법규위반 비율')
plt.show()

fig = plt.figure(figsize=(8,8))
fig.set_facecolor('white')
ax1 = fig.add_subplot()
# plt.ylim([0, 900])

xtick_label_position = list(range(len(a_type))) 
ax1.set_xticks(xtick_label_position) 
ax1.set_xticklabels(a_type) 
a_bar = ax1.bar(xtick_label_position, num, color='c', label = '사고발생건수')
#plt.xlabel('가해차량 법규위반 유형')
ax1.set_ylabel('노인보행자 사고발생건수')
for i in range( len(a_type)):
  plt.text( i-0.4, num[i]+20, f'{num[i]}', size = 14)
plt.legend(loc='best')


ax2 = ax1.twinx() 
d_plot = ax2.plot(xtick_label_position, death, color='r', linestyle='--', marker='o', label = '사망자 수')
ax2.tick_params(axis='y', labelcolor='r')
ax2.set_ylabel('사망자 수')
for i in range( len(a_type)):
  plt.text( i+0.1, death[i]+0.5, f'{death[i]}', size = 14, color='r')
plt.legend(loc=(0.81,0.9))

# ax3 = ax1.twinx()
# i_plot = ax3.plot(xtick_label_position, injury, color='b', linestyle='--', marker='o', label = '부상자 수')
# ax3.tick_params(axis='y', labelcolor='r')
# for i in range( len(a_type)):
#   plt.text( i-0.25, injury[i]-0.1, f'{injury[i]}', size = 14, color='b')
# plt.legend(loc=(0.81,0.9))


plt.title('가해차량 법규위반유형별 사고발생건수와 사망자')
plt.show()

- 안전운전의무 불이행으로 인한 사고는 전체 사고수 중 87.6%를 차지한다.
- 또한 그로 인해 사망한 수도 다른 사고에 비해 압도적으로 많다
- 운전자들의 안전운전의무 인식을 상기시킬 필요가 있다
- 과속의 경우 사고건수는 적은 편이지만 그에 비해 사망률은 치명적
