# (사망, 부상정도)
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

from google.colab import drive
drive.mount('/content/drive')

rawData = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/실습/Data폴더/연령별 보행사상자 유형.csv')


rawData

rawData = rawData.T
rawData

rawData.info()

rawData = rawData.loc[['0', "1", '2']]
rawData

rawData = rawData[[40, 41, 42, 43, 44, 45, 46, 47, 48, 49,]]
rawData

rawData.columns = [ '65~70세_사망자수', '65~70세_부상자수','65~70세_중상자수', '65~70세_경상자수','65~70세_부상신고자수', '71세이상_사망자수', '71세이상_부상자수','71세이상_중상자수', '71세이상_경상자수','71세이상_부상신고자수' ]
rawData

rawData = rawData.loc[['2']]
rawData

rawData = rawData.apply(pd.to_numeric)

rawData.info()

rawData['총사망자수'] = rawData['65~70세_사망자수'] + rawData['71세이상_사망자수']
rawData

rawData['총중상자수'] = rawData['65~70세_중상자수'] + rawData['71세이상_중상자수']
rawData

rawData['총경상자수'] = rawData['65~70세_경상자수'] + rawData['71세이상_경상자수']
rawData

rawData['총부상신고자수'] = rawData['65~70세_부상신고자수'] + rawData['71세이상_부상신고자수']
rawData

rawData = rawData[['총사망자수', '총중상자수', '총경상자수', '총부상신고자수']]
rawData

lab = rawData.columns
lab

# 결론
plt.figure(figsize=(7,7))
wedgeprops = {'width':0.7, 'edgecolor':'w', 'linewidth':5}
plt.pie(rawData, labels = lab, autopct='%.1f%%',startangle=150, counterclock=False, wedgeprops=wedgeprops, colors = ['#02818a','#3690c0','#a6bddb','#d0d1e6'])
plt.show()

- 2020년 서울시 기준, 보행 중 교통사고를 당한 노인의 총 사상자는 1826명
- 보행 중 교통사고를 당한 노인들의 부상정도는 3주 이상의 치료를 요하는 중상이 절반 이상이다.
- 사망자수와 합하면 56%정도로 교통사고로 인한 노인 보행자의 부상정도가 심각하다고 볼 수 있다

- 문제제기 부분에 추가?


- 사상자: 사망자+부상자
- 사망: 사고 발생시로부터 30일이내에 사망한 경우
- 중상: 3주 이상의 치료를 요하는 부상
- 경상: 5일 이상 3주 미만의 치료를 요하는 부상
- 부상신고: 5일 미만의 치료를 요하는 부상