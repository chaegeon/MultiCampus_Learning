import pandas as pd
import numpy as np
import pymysql

pip install xmltodict

import xmltodict
import matplotlib.pyplot as plt
import seaborn as sns

pip install ipython-sql


pip install PyMySQL

pip install mysqlclient

import pymysql
import pandas as pd
from sqlalchemy import create_engine
pymysql.install_as_MySQLdb()
import MySQLdb

%load_ext sql

%sql mysql://st02:st02@localhost:3306/DB?charset=utf8
# ?charset=utf8  => 인코딩문제로 불러오기가 안 됐었는데 이걸로 해결







rawData = pd.read_csv('../lab20/Data/2001_01_01-2010_12_31_흐림.csv',encoding='CP949')

rawData1 = pd.read_csv('../lab20/Data/2011_01_01-2020_12_31_흐림.csv',encoding='CP949')

rawData2 = pd.read_csv('../lab20/Data/2021_01_01-2021_12_31_흐림.csv',encoding='CP949')

rawData

rawData1

rawData2

rawData = pd.merge(rawData.T, rawData1.T, left_index = True, right_index=True)
rawData

rawData = pd.merge(rawData, rawData2.T, left_index = True, right_index=True)
rawData

rawData = rawData.T
rawData

rawData=pd.DataFrame(rawData)



engine = create_engine("mysql+mysqldb://st02:st02@localhost:3306/DB?charset=utf8", encoding='utf-8')

# rawData.to_sql(name='흐린날20010101_20211231', con=engine, index=False, if_exists='fail')

####################################################################################################################################

%sql SELECT * FROM DB.흐린날20010101_20211231;

%sql cloudiness << SELECT * FROM DB.흐린날20010101_20211231;

# 변수명 : sqlData
# df이름 : cloudiness

sqlData = %sql SELECT * FROM DB.흐린날20010101_20211231;
cloudiness = sqlData.DataFrame()

cloudiness

cloudiness = rawData
cloudiness

cloudiness.info()

cloudiness.dtypes

cloudiness.isna().sum()

cloudiness=cloudiness.fillna(0)
cloudiness.isna().sum()

cloudiness.columns

cloudiness.index

cloudiness

cloudiness = cloudiness.rename(columns = {'지점':'Point', '지점명':'Point_name', '일시':'Date','강수 계속시간(hr)':'Continuous_precipitation_time(hr)', '일강수량(mm)':'Daily_precipitation(mm)',
'합계 일조시간(hr)':'Total_sunlight_time(hr)', '평균 전운량(1/10)':'Average_total_cloudiness(1/10)'})
cloudiness

cloudiness = cloudiness.reset_index()
cloudiness

cloudiness = cloudiness.drop(['index', 'Point', 'Point_name'], axis=1)
cloudiness

cloudiness.isnull().sum(), cloudiness.isna().sum(), cloudiness.dtypes

cloud = cloudiness['Average_total_cloudiness(1/10)'].values.tolist()
cloud

sunlight = cloudiness['Total_sunlight_time(hr)'].values.tolist()
sunlight

fig = plt.figure(figsize=(100,20))
plt.plot(cloudiness['Date'], cloudiness['Total_sunlight_time(hr)'])

cloudiness = cloudiness.drop(['Continuous_precipitation_time(hr)', 'Daily_precipitation(mm)'], axis=1)
cloudiness

sunny = cloudiness[cloudiness['Average_total_cloudiness(1/10)'] < 3]
sunny

few = cloudiness[(cloudiness['Average_total_cloudiness(1/10)'] >= 3) & (cloudiness['Average_total_cloudiness(1/10)'] < 6)]
few

many = cloudiness[(cloudiness['Average_total_cloudiness(1/10)'] >= 6) & (cloudiness['Average_total_cloudiness(1/10)'] < 9)]
many

overcast = cloudiness[cloudiness['Average_total_cloudiness(1/10)'] >= 9]
overcast

plt.figure(figsize=(100,20))
sns.lineplot(x=sunny['Date'], y=sunny['Total_sunlight_time(hr)'], color='red', alpha=0.8)
sns.lineplot(x=sunny['Date'], y=sunny['Average_total_cloudiness(1/10)'], color='navy', alpha=0.8)

plt.figure(figsize=(100,20))
sns.lineplot(x=few['Date'], y=few['Total_sunlight_time(hr)'], color='red', alpha=0.3)
sns.lineplot(x=few['Date'], y=few['Average_total_cloudiness(1/10)'], color='navy', alpha=0.7)

plt.figure(figsize=(100,20))
sns.lineplot(x=many['Date'], y=many['Total_sunlight_time(hr)'], color='red', alpha=0.3)
sns.lineplot(x=many['Date'], y=many['Average_total_cloudiness(1/10)'], color='navy', alpha=0.7)

plt.figure(figsize=(100,20))
sns.lineplot(x=overcast['Date'], y=overcast['Total_sunlight_time(hr)'], color='red', alpha=0.5)
sns.lineplot(x=overcast['Date'], y=overcast['Average_total_cloudiness(1/10)'], color='navy', alpha=0.9)

# 일일 합계 일조시간과 일일 평균 전운량의 관계는 반비례
# 흐린 날은 일일 평균 전운량으로 판단할 수 있을 것 같다

def func(x) :
    if x >= 9 :
        return "흐림"
    elif x >= 6:
        return "구름많음"
    elif x >= 3:
        return "구름조금"
    else : return "맑음"
cloudiness["Sky_condition"] = cloudiness["Average_total_cloudiness(1/10)"].apply(lambda x : func(x))

def func(x) :
    if x >= 6 :
        return "흐림"
    else : return "맑음"
cloudiness["Sky_condition2"] = cloudiness["Average_total_cloudiness(1/10)"].apply(lambda x : func(x))

cloudiness

cloudiness.groupby(['Sky_condition'])

cloudiness.groupby(['Sky_condition']).count()

pd.DataFrame(cloudiness).to_csv('맑음흐림2001_01_01-2021_12_31.csv.csv')

cloudiness.isna().sum()



engine = create_engine("mysql+mysqldb://st02:st02@localhost:3306/cloudy?charset=utf8", encoding='utf-8')
cloudiness.to_sql(name='맑음흐림20010101_20211231', con=engine, index=False, if_exists='fail')

%sql SELECT * FROM DB.맑음흐림20010101_20211231;

%sql SELECT * FROM DB.흐린날20010101_20211231;

%sql SELECT * FROM DB.맑음흐림2001_01_01-2021_12_31;







%sql SELECT * FROM stock.2001_2021_주가;

%sql stock << SELECT * FROM stock.2001_2021_주가;

# 변수명 : sqlStock
#df이름 : stock

sqlStock = %sql SELECT * FROM stock.2001_2021_주가;
stock = sqlStock.DataFrame()

stock



stock['kospi'].min()

stock[stock['kospi'] == 0]