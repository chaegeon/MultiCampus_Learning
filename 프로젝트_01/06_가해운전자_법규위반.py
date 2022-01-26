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