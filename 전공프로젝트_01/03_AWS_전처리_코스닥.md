# 코스닥

import pandas as pd
import numpy as np
import pymysql

pip install xmltodict

import xmltodict
import matplotlib.pyplot as plt
import seaborn as sns

#한글화 설정
from matplotlib import font_manager, rcParams
!apt-get install fonts-nanum*
rcParams['font.family'] = 'NanumGothicCoding'
rcParams['axes.unicode_minus'] = False
font_manager._rebuild()

pip install ipython-sql


pip install PyMySQL

pip install mysqlclient

import pymysql
import pandas as pd
from sqlalchemy import create_engine
pymysql.install_as_MySQLdb()
import MySQLdb

%load_ext sql

%sql mysql://st02:st02@localhost:3306/cloudy?charset=utf8
# ?charset=utf8  => 인코딩문제로 불러오기가 안 됐었는데 이걸로 해결





cloudiness = pd.read_csv('cloudiness.csv')
cloudiness

stock = pd.read_csv('stock.csv')
stock

# cloudiness 의 Date 컬럼의 타입을 datetime으로 변환
cloudiness['Date'] = pd.to_datetime(cloudiness['Date'])

stock.rename(columns = {"date":"Date"}, inplace=True)
stock

# cloudiness 의 Date 컬럼의 타입을 datetime으로 변환
stock['Date'] = pd.to_datetime(stock['Date'])

cloudiness_stock = pd.merge(cloudiness, stock, left_on = 'Date', right_on='Date', how='inner')
cloudiness_stock

cloudiness_stock[cloudiness_stock['kospi'] == 0]

# 중간에 휴장일 날짜의 행이 포함되어 있어 삭제
cloudiness_stock = cloudiness_stock.drop([cloudiness_stock.index[2641]])
cloudiness_stock

cloudiness_stock = cloudiness_stock.dropna()
cloudiness_stock



cloudiness_stock = cloudiness_stock.reset_index()
cloudiness_stock

cloudiness_stock = cloudiness_stock.drop(['index', 'Unnamed: 0_x', 'Unnamed: 0_y'],axis=1)
cloudiness_stock

cloudiness_stock.isna().sum()

kosdaq_list = cloudiness_stock['kosdaq'].values.tolist()
kosdaq_list

kosdaqS= pd.Series(kosdaq_list)
kosdaqS

cloudiness_stock['kosdaq_net_change'] = cloudiness_stock.kosdaq.diff()

cloudiness_stock['kosdaq_fluctuation'] = round((kosdaqS.pct_change()*100), 2)

cloudiness_stock

kosdaq = cloudiness_stock.drop(columns=['Total_sunlight_time(hr)', 'kospi','volume_kospi', 'amount_kospi'])
kosdaq

kosdaq['kosdaq_fluctuation'].fillna(0, inplace=True)

kosdaq['kosdaq_net_change'].fillna(0, inplace=True)

kosdaq

kosdaq.isna().sum()

kosdaq.info()

kosdaq.groupby(['Sky_condition'])

kosdaq.groupby(['Sky_condition'])['kosdaq_fluctuation'].mean()

kosdaq.groupby(['Sky_condition2'])['kosdaq_fluctuation'].mean()

kosdaq['kosdaq_fluctuation'].isna().sum()

kosdaq[kosdaq['kosdaq_fluctuation'].isna()]

kosdaq['kosdaq_fluctuation'].mean()

v_kosdaq_list = kosdaq['volume_kosdaq'].values.tolist()
v_kosdaq_list

vol_kosdaqS= pd.Series(v_kosdaq_list)
vol_kosdaqS

kosdaq['vol_net_change'] = kosdaq.volume_kosdaq.diff()

kosdaq['vol_fluctuation'] = round((vol_kosdaqS.pct_change()*100), 2)

kosdaq

amt_kosdaq_list = kosdaq['amount_kosdaq'].values.tolist()
amt_kosdaq_list

amt_kosdaqS= pd.Series(amt_kosdaq_list)
amt_kosdaqS

kosdaq['amt_net_change'] = kosdaq.amount_kosdaq.diff()

kosdaq['amt_fluctuation'] = amt_kosdaqS.pct_change()*100

kosdaq

kosdaq.fillna(0, inplace = True)

kosdaq.isna().sum()

# 전체 일수 중 전운량에 따라 나눈 일수
ax = sns.countplot(data = kosdaq, x='Sky_condition')
for x in ax.patches:
  height = x.get_height()
  ax.text(x.get_x() + x.get_width()/2., height+3, height, ha='center', size=15)

plt.ylabel('일 수')

ax = plt.gca()
ax.axes.yaxis.set_ticks([])


kosdaq.groupby(['Sky_condition'])['kosdaq'].mean()

