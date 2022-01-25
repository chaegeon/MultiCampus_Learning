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