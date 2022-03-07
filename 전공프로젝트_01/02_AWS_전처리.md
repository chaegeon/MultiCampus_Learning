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

%sql SELECT * FROM DB.맑음흐림20010101_20211231;

%sql cloudiness << SELECT * FROM cloudy.맑음흐림20010101_20211231;

# 변수명 : sqlData
# df이름 : cloudiness

sqlData = %sql SELECT * FROM cloudy.맑음흐림20010101_20211231;
cloudiness = sqlData.DataFrame()

cloudiness

pd.DataFrame(cloudiness).to_csv('cloudiness.csv')

%sql SELECT * FROM stock.2001_2021_주가;

%sql stock << SELECT * FROM stock.2001_2021_주가;

# 변수명 : sqlStock
#df이름 : stock

sqlStock = %sql SELECT * FROM stock.2001_2021_주가;
stock = sqlStock.DataFrame()

stock

pd.DataFrame(stock).to_csv('stock.csv')

stock.rename(columns = {"date":"Date"}, inplace=True)
stock

sns.countplot(data = cloudiness_kospi, x='Sky_condition')

# cloudiness 의 Date 컬럼의 타입을 datetime으로 변환
cloudiness['Date'] = pd.to_datetime(cloudiness['Date'])

cloudiness.dtypes

cloudiness_stock = pd.merge(cloudiness, stock, left_on = 'Date', right_on='Date', how='inner')
cloudiness_stock

# 2001년 ~ 2010년까지
CS_2010 = cloudiness_stock[cloudiness_stock['Date'].between('2001-01-01','2010-12-31')]
CS_2010

# 2011년 ~ 2021년까지
CS_2021 = cloudiness_stock[cloudiness_stock['Date'].between('2011-01-01','2021-12-31')]
CS_2021

len(cloudiness_stock)

len(CS_2010)

len(CS_2021)

2479+2702

pd.DataFrame(CS_2010).to_csv('2001~2010.csv')

pd.DataFrame(CS_2021).to_csv('2011~2021.csv')







cloudiness_stock.info()

cloudiness_stock.isna().sum(), cloudiness_stock.isnull().sum()

pd.DataFrame(cloudiness).to_csv('cloudiness_stock.csv')

cloudiness_stock['kospi'].min()

cloudiness_stock[cloudiness_stock['kospi'] == 0]

# 중간에 휴장일 날짜의 행이 포함되어 있어 삭제
cloudiness_stock = cloudiness_stock.drop([cloudiness_stock.index[2641]])
cloudiness_stock

cloudiness_stock[cloudiness_stock['kospi'] == 0]

cloudiness_stock = cloudiness_stock.reset_index()
cloudiness_stock

cloudiness_stock=cloudiness_stock.drop(['index'],axis=1)

cloudiness_stock



################################################################################################################################

# engine = create_engine("mysql+mysqldb://st02:st02@localhost:3306/cloudy?charset=utf8", encoding='utf-8')
# cloudiness_stock.to_sql(name='흐림과_주식_20010101_20211231', con=engine, index=False, if_exists='fail')

# 5181개의 행 중,
# 맑음 1696
# 구름조금 1457
# 구름많음 1350
# 흐림 678







plt.figure(figsize=(50,8))
sns.lineplot(x='Date', y='Average_total_cloudiness(1/10)', data=cloudiness_stock, color='black', alpha=0.5)


plt.figure(figsize=(50,8))
sns.lineplot(x='Date', y='Total_sunlight_time(hr)', data=cloudiness_stock, alpha=0.8)






kospi_list = cloudiness_stock['kospi'].values.tolist()
kospi_list

kospiS= pd.Series(kospi_list)
kospiS

cloudiness_stock['kospi_net_change'] = cloudiness_stock.kospi.diff()

cloudiness_stock['kospi_fluctuation'] = round((kospiS.pct_change()*100), 2)

cloudiness_stock

cloudiness_kospi = cloudiness_stock.drop(columns=['Total_sunlight_time(hr)', 'kosdaq', 'volume_kosdaq', 'amount_kosdaq'])
cloudiness_kospi

# cloudiness_kospi = cloudiness_stock.drop(columns=['Total_sunlight_time(hr)'])
# cloudiness_kospi

sunny = cloudiness_stock[cloudiness_stock['Average_total_cloudiness(1/10)'] < 3]
sunny

few = cloudiness_stock[(cloudiness_stock['Average_total_cloudiness(1/10)'] >= 3) & (cloudiness_stock['Average_total_cloudiness(1/10)'] < 6)]
few

many = cloudiness_stock[(cloudiness_stock['Average_total_cloudiness(1/10)'] >= 6) & (cloudiness_stock['Average_total_cloudiness(1/10)'] < 9)]
many

overcast = cloudiness_stock[cloudiness_stock['Average_total_cloudiness(1/10)'] >= 9]
overcast

plt.figure(figsize=(200,50))

sns.lineplot(x = sunny['Average_total_cloudiness(1/10)'], y=cloudiness_stock['kospi'], color='red')

plt.figure(figsize=(200,50))

sns.lineplot(x = few['Average_total_cloudiness(1/10)'], y = cloudiness_stock['kospi'], color='red')

plt.figure(figsize=(200,50))

sns.lineplot(x = many['Average_total_cloudiness(1/10)'], y = cloudiness_stock['kospi'], color='red')

plt.figure(figsize=(200,50))

sns.lineplot(x = overcast['Average_total_cloudiness(1/10)'], y = cloudiness_stock['kospi'], color='red')

plt.figure(figsize=(100,50))
sns.lineplot(x=cloudiness_stock['Date'], y=sunny['kospi'], color='red')
sns.lineplot(x=cloudiness_stock['Date'], y=few['kospi'], color='green')
sns.lineplot(x=cloudiness_stock['Date'], y=many['kospi'], color='blue', alpha=0.5)
sns.lineplot(x=cloudiness_stock['Date'], y=overcast['kospi'], color='black', alpha=0.8)

cloudiness_kospi.groupby(['Sky_condition'])

cloudiness_kospi.groupby(['Sky_condition'])['kospi_fluctuation'].mean()

cloudiness_kospi.groupby(['Sky_condition2'])['kospi_fluctuation'].mean()

cloudiness_kospi.isna().sum()

cloudiness_kospi

cloudiness_kospi['kospi_fluctuation'].fillna(0, inplace=True)

cloudiness_kospi['kospi_net_change'].fillna(0, inplace=True)

cloudiness_kospi

cloudiness_kospi.isna().sum()

cloudiness_kospi.info()

cloudiness_kospi.groupby(['Sky_condition'])

cloudiness_kospi.groupby(['Sky_condition'])['kospi_fluctuation'].mean()

cloudiness_kospi.groupby(['Sky_condition2'])['kospi_fluctuation'].mean()

cloudiness_kospi['kospi_fluctuation'].isna().sum()

cloudiness_kospi[cloudiness_kospi['kospi_fluctuation'].isna()]

cloudiness_kospi['kospi_fluctuation'].mean()







v_kospi_list = cloudiness_kospi['volume_kospi'].values.tolist()
v_kospi_list

vol_kospiS= pd.Series(v_kospi_list)
vol_kospiS

cloudiness_kospi['vol_net_change'] = cloudiness_kospi.volume_kospi.diff()

cloudiness_kospi['vol_fluctuation'] = round((vol_kospiS.pct_change()*100), 2)

cloudiness_kospi

amt_kospi_list = cloudiness_kospi['amount_kospi'].values.tolist()
amt_kospi_list

amt_kospiS= pd.Series(amt_kospi_list)
amt_kospiS

cloudiness_kospi['amt_net_change'] = cloudiness_kospi.amount_kospi.diff()

cloudiness_kospi['amt_fluctuation'] = amt_kospiS.pct_change()*100

cloudiness_kospi

cloudiness_kospi['vol_fluctuation'].fillna(0, inplace=True)

cloudiness_kospi['vol_net_change'].fillna(0, inplace=True)

cloudiness_kospi['amt_net_change'].fillna(0, inplace=True)

cloudiness_kospi['amt_fluctuation'].fillna(0, inplace=True)

cloudiness_kospi

cloudiness_kospi.groupby(['Sky_condition'])['vol_fluctuation'].mean()

cloudiness_kospi.groupby(['Sky_condition2'])['amt_fluctuation'].mean()

sky = cloudiness_kospi.groupby(['Sky_condition'], as_index=False).mean()
sky

sky_sum = cloudiness_kospi.groupby(['Sky_condition'], as_index=False).mean()
sky_sum

# 전운량 별 평균 코스피지수

plt.figure(figsize=(25,10))
sns.lineplot(x='Average_total_cloudiness(1/10)', y='kospi', data=sky)

# 전운량 별 평균 코스피지수

plt.figure(figsize=(25,10))
sns.lineplot(x='Average_total_cloudiness(1/10)', y='volume_kospi', data=sky)

# 구름이 있을 때 거래량이 활발

# 전운량 별 평균 코스피지수

plt.figure(figsize=(25,10))
sns.lineplot(x='Average_total_cloudiness(1/10)', y='amount_kospi', data=sky)

sky2 = cloudiness_kospi.groupby(['Sky_condition2'], as_index=False).mean()
sky2

# 전운량2 별 평균 코스피지수 평균

plt.figure(figsize=(25,10))
sns.lineplot(x='Average_total_cloudiness(1/10)', y='kospi', data=sky2)

# 전운량2 별 평균 코스피 거래량 평균

plt.figure(figsize=(25,10))
sns.lineplot(x='Average_total_cloudiness(1/10)', y='volume_kospi', data=sky2)

# 전운량2 별 코스디 거래대금 평균

plt.figure(figsize=(25,10))
sns.lineplot(x='Average_total_cloudiness(1/10)', y='amount_kospi', data=sky2)





cloudiness_kospi['UpDown'] = np.where(cloudiness_kospi['kospi_fluctuation']>=0, '상승', '하락')

cloudiness_kospi

cloudiness_kospi['vol_UpDown'] = np.where(cloudiness_kospi['vol_fluctuation']>0, '상승', '하락')

cloudiness_kospi['amt_UpDown'] = np.where(cloudiness_kospi['amt_fluctuation']>0, '상승', '하락')

cloudiness_kospi

cloudiness_kospi.isna().sum(), cloudiness_kospi.isnull().sum()

cloudiness_kospi.plot.bar(x='Sky_condition', y='kospi_fluctuation')

cloudiness_kospi.head(5)

sns.barplot(data = cloudiness_kospi, x='Sky_condition', y='kospi_fluctuation')

sns.countplot(data = cloudiness_kospi, x='Sky_condition')

sky_UpDown = cloudiness_kospi[['Sky_condition', 'UpDown']]
sky_UpDown 

sns.countplot(data =sky_UpDown, x='Sky_condition', hue='UpDown')

sky_UpDown2 = cloudiness_kospi[['Sky_condition2', 'UpDown']]
sky_UpDown2 

sns.countplot(data =sky_UpDown2, x='Sky_condition2', hue='UpDown')

cloudiness_kospi.plot.bar( x= 'Sky_condition',y=('kospi_fluctuation'))

plt.figure(figsize=(10,10))
plt.scatter(cloudiness_kospi['Sky_condition'], cloudiness_kospi['kospi_fluctuation'])
plt.axhline( y = 0, color='r', linewidth = 1) 

cloud = ['맑음', '구름조금', '구름많음', '흐림']

cloudiness_kospi.groupby('Sky_condition')['kospi_fluctuation'].mean().reindex(cloud)

Cloud = cloudiness_kospi.groupby('Sky_condition')['kospi_fluctuation'].mean().reindex(cloud)

Cloud

cloud2 = ['맑음', '흐림']

cloudiness_kospi.groupby('Sky_condition2')['kospi_fluctuation'].mean().reindex(cloud2)

Cloud2 = cloudiness_kospi.groupby('Sky_condition2')['kospi_fluctuation'].mean().reindex(cloud2)

# 전운량별 평균 등락률 - 맑음, 구름조금, 구름많음, 흐림
plt.bar(Cloud.index, Cloud)

# 전운량별 평균 등락률 - 맑음, 흐림
plt.bar(Cloud2.index, Cloud2)

###################################################################################################################################
# 맑음과 흐림만 빼봄
sunny_overcast = cloudiness_kospi[(cloudiness_kospi['Sky_condition']=='맑음') | (cloudiness_kospi['Sky_condition']=='흐림')]
sunny_overcast

# engine = create_engine("mysql+mysqldb://st02:st02@localhost:3306/cloudy?charset=utf8", encoding='utf-8')
# cloudiness_kospi.to_sql(name='kospi_이것저것_다', con=engine, index=False, if_exists='fail')

# pd.DataFrame(cloudiness_kospi).to_csv('kospi_이것저것_다')

# engine = create_engine("mysql+mysqldb://st02:st02@localhost:3306/cloudy?charset=utf8", encoding='utf-8')
# sunny_overcast.to_sql(name='맑은날_흐린날만', con=engine, index=False, if_exists='fail')

# pd.DataFrame(sunny_overcast).to_csv('맑은날_흐린날만')























SO = sunny_overcast.groupby(['Sky_condition'], as_index=False).mean()
SO

# 전운량 별 평균 코스피지수

plt.figure(figsize=(25,10))
sns.lineplot(x='Average_total_cloudiness(1/10)', y='kospi', data=SO)

# 전운량 별 평균 코스피지수

plt.figure(figsize=(25,10))
sns.lineplot(x='Sky_condition', y='kospi', data=SO)

# 전운량 별 평균 코스피지수

plt.figure(figsize=(25,10))
sns.lineplot(x='Sky_condition', y='Average_total_cloudiness(1/10)', data=SO)







# 흐림, 맑음 별 평균 등락률?
sns.set_palette("Greys", 2)
ax = sns.barplot(x='Sky_condition', y='kospi_fluctuation', data=SO)
for x in ax.patches:
  height = x.get_height()
  ax.text(x.get_x() + x.get_width()/2., height+0.0001, height, ha='center', size=15)

plt.ylabel('일 수')
ax = plt.gca()
ax.axes.yaxis.set_ticks([])

SO.plot.bar(x='Sky_condition', y='vol_fluctuation')

SO.plot.bar(x='Sky_condition', y='amt_fluctuation')

# 맑음, 흐림 별 코스피 상승하락 카운트
sns.set_palette("Blues", 2)
ax = sns.countplot(data=sunny_overcast, x='Sky_condition', hue = 'UpDown')
for x in ax.patches:
  height = x.get_height()
  ax.text(x.get_x() + x.get_width()/2., height+3, height, ha='center', size=15)

plt.ylabel('일 수')

# 맑음, 흐림 별 코스피 거래량 상승하락 카운트

ax = sns.countplot(data=sunny_overcast, x='Sky_condition', hue = 'vol_UpDown')
for x in ax.patches:
  height = x.get_height()
  ax.text(x.get_x() + x.get_width()/2., height+3, height, ha='center', size=15)

plt.ylabel('일 수')

# 맑음, 흐림 별 코스피 거래대금 상승하락 카운드
sns.countplot(data=sunny_overcast, x='Sky_condition', hue = 'amt_UpDown')

# 날짜에 따른 맑음, 흐림 별 코스피 그래프

plt.figure(figsize=(25,10))
sns.lineplot(x='Date', y='kospi', hue='Sky_condition', data=sunny_overcast)

cloudiness.median


# 날짜에 따른 맑음, 흐림 별 거래대금 변화

plt.figure(figsize=(10,10))
sns.lineplot(x='Date', y='amount_kospi', hue='Sky_condition', data=sunny_overcast)

# 날짜에 따른 맑음, 흐림 별 거래량 변화

plt.figure(figsize=(10,10))
sns.lineplot(x='Date', y='volume_kospi', hue='Sky_condition', data=sunny_overcast)

# 날짜에 따른 맑음, 흐림 별 코스피등락률 그래프

plt.figure(figsize=(10,10))
sns.lineplot(x='Date', y='kospi_fluctuation', hue='Sky_condition', data=sunny_overcast, color=('#FAB258', '#4E6DDE'))
plt.axhline( y = 0, color='black', linewidth = 2) 

# 날짜에 따른 맑음, 흐림 별 거래량대금 등락률 그래프

plt.figure(figsize=(10,10))
sns.lineplot(x='Date', y='amt_fluctuation', hue='Sky_condition', data=sunny_overcast)
plt.axhline( y = 0, color='black', linewidth = 2) 

# 날짜에 따른 맑음, 흐림 별 거래량 등락률 그래프

plt.figure(figsize=(10,10))
sns.lineplot(x='Date', y='vol_fluctuation', hue='Sky_condition', data=sunny_overcast)

##########################################################################################
#아웃라이어 제거

sunny_overcast['vol_fluctuation'].max()

sunny_overcast['vol_fluctuation'].describe()

q1=sunny_overcast['vol_fluctuation'].quantile(0.25)


q2=sunny_overcast['vol_fluctuation'].quantile(0.5)


q3=sunny_overcast['vol_fluctuation'].quantile(0.75)

iqr=200          # iqr = q3-q1
iqr

A=sunny_overcast['vol_fluctuation']>q3+1.5*iqr

sunny_overcast[A]

a=sunny_overcast[A].index
AA = sunny_overcast.drop(a)

AA['vol_fluctuation'].max()

# 날짜에 따른 맑음, 흐림 별 거래량 등락률 그래프

plt.figure(figsize=(10,10))
sns.lineplot(x='Date', y='vol_fluctuation', hue='Sky_condition', data=AA)
plt.axhline( y = 0, color='black', linewidth = 2) 



sns.boxplot(x = sunny_overcast['kospi_fluctuation'])

sns.boxplot(x = sunny_overcast['amt_fluctuation'])

sns.boxplot(x = sunny_overcast['vol_fluctuation'])

sunny_overcast['vol_fluctuation'].max()

sunny_overcast['vol_fluctuation'].describe()

q1=sunny_overcast['vol_fluctuation'].quantile(0.25)


q2=sunny_overcast['vol_fluctuation'].quantile(0.5)


q3=sunny_overcast['vol_fluctuation'].quantile(0.75)

iqr=200          # iqr = q3-q1
iqr

A=sunny_overcast['vol_fluctuation']>q3+1.5*iqr

sunny_overcast[A]

a=sunny_overcast[A].index
AA = sunny_overcast.drop(a)

AA['vol_fluctuation'].max()

sns.boxplot(x = AA['vol_fluctuation'] )













# 맑음, 흐림 별 코스피 등락률

sns.barplot(x = sunny_overcast['Sky_condition'], y = sunny_overcast['kospi_fluctuation'])

sns.barplot(x = sunny_overcast['Sky_condition'], y = sunny_overcast['vol_fluctuation'])

sns.barplot(x = sunny_overcast['Sky_condition'], y = sunny_overcast['amt_fluctuation'])

plt.figure(figsize=(10,10))
sns.violinplot(y = sunny_overcast['kospi_fluctuation'], x = sunny_overcast['Sky_condition'])

sns.stripplot(y = sunny_overcast['kospi_fluctuation'], x = sunny_overcast['Sky_condition'])

plt.figure(figsize=(20,10))
sns.swarmplot(y = sunny_overcast['kospi_fluctuation'], x = sunny_overcast['Sky_condition'])





cloudiness_kospi

cloudiness_kospi.isna().sum(),cloudiness_kospi.isnull().sum()

cloudiness_kospi.fillna(0)

plt.figure(figsize=(50,50))
sns.lmplot(x='Date', y='kospi',col='Sky_condition', hue = 'Sky_condition', data=cloudiness_kospi)

sns.heatmap(df.corr(), annot = True, cmap = 'viridis')

plt.figure(figsize=(25,10))
sns.lineplot(x='Average_total_cloudiness(1/10)', y='kospi', data=cloudiness_kospi)

plt.figure(figsize=(25,10))
sns.scatterplot(x='Average_total_cloudiness(1/10)', y='kospi', data=cloudiness_kospi)

plt.figure(figsize=(25,10))
sns.scatterplot(x='Average_total_cloudiness(1/10)', y='kospi', hue = 'Sky_condition', data=cloudiness_kospi)

plt.figure(figsize=(25,10))
sns.lmplot(x='Average_total_cloudiness(1/10)', y='kospi', col='Sky_condition', hue='Sky_condition', data=cloudiness_stock)

sns.set_palette("RdGy", 4)
plt.figure(figsize=(20,10))
sns.scatterplot(x='kospi', y='Average_total_cloudiness(1/10)',  hue = 'Sky_condition', data=cloudiness_kospi)

sns.set_palette("RdGy", 4)
plt.figure(figsize=(50,30))
sns.lmplot(x='kospi', y='Average_total_cloudiness(1/10)', col='Sky_condition', hue = 'Sky_condition', data=cloudiness_kospi)

cdiffcorr = cloudiness_stock[['Average_total_cloudiness(1/10)','kospi','kospi_net_change','kospi_fluctuation']]


cdiffcorr.corr()

plt.figure(figsize = (10,10))
sns.heatmap(data=cloudiness_stock[['Average_total_cloudiness(1/10)','kospi','kospi_net_change','kospi_fluctuation']].corr(), annot=True, fmt='.3f', linewidths=.5, cmap = 'viridis')

plt.figure(figsize=(10,10))
ax = sns.regplot(x = "Average_total_cloudiness(1/10)", y = "kospi", data = cloudiness_kospi)

cloudiness_kospi.corr()

plt.figure(figsize=(20,10))
sns.plot(cloudiness_stock['Sky_condition'],color='blue')
plt.ylabel('Kospi_diff')

ax = plt.gca()
ax2 = ax.twinx()
ax2.plot(cloudiness_stock['Sky_condition'],color='red', alpha=0.5)
ax2.set_ylabel('hightest temp')



asd = cloudiness_kospi.groupby(['Sky_condition'], as_index=False).mean()
asd

asd.corr()

# 전운량 별 /  하루 합계 일조시간과 코스피 지수의 경향성 예측
plt.figure(figsize=(50,50))
sns.lmplot(x='Average_total_cloudiness(1/10)', y='kospi',hue = 'Sky_condition', data=cloudiness_kospi)

plt.figure(figsize=(25,10))
sns.lineplot(x='Date', y='kospi', hue='Sky_condition', data=cloudiness_stock)

cloudiness_stock

# 2001년 ~ 2010년까지
CS_2010 = cloudiness_stock[cloudiness_stock['Date'].between('2001-01-01','2010-12-31')]
CS_2010

# 2011년 ~ 2021년까지
CS_2021 = cloudiness_stock[cloudiness_stock['Date'].between('2011-01-01','2021-12-31')]
CS_2021

len(cloudiness_stock)

len(CS_2010)

len(CS_2021)

2479+2702

pd.DataFrame(cloudiness_kospi).to_csv('kospi.csv')



plt.figure(figsize=(50,10))
plt.plot(stock['kospi'],color='red', alpha = 0.8)
plt.ylabel('Kospi')

ax = plt.gca()
ax2 = ax.twinx()
ax2.plot(stock['kosdaq'],color='blue', alpha=0.8)
ax2.set_ylabel('Kosdaq')

plt.legend

sns.countplot(data = kospi_s, x='Sky_condition')