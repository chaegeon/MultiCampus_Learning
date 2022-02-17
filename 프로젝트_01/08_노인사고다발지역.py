# (예린님 자료)

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd

oldman = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/실습/01_프로젝트/20_oldman.csv')

oldman

oldman.columns

# 불필요한 컬럼 제거
oldman.drop(['사고다발지FID', '사고다발지ID', '법정동코드', '지점코드', '부상신고자수', '다발지역폴리곤'], axis=1, inplace=True)

oldman.head()

# 시도시군구명에서 서울특별시 삭제
oldman['시도시군구명'] = oldman['시도시군구명'].str.replace('서울특별시', '')
oldman.head()

# 문자열 데이터를 숫자로 변환

oldman['발생건수'] = pd.to_numeric(oldman['발생건수'])
oldman['사상자수'] = pd.to_numeric(oldman['사상자수'])
oldman['사망자수'] = pd.to_numeric(oldman['사망자수'])
oldman['중상자수'] = pd.to_numeric(oldman['중상자수'])
oldman['경도'] = pd.to_numeric(oldman['경도'])
oldman['위도'] = pd.to_numeric(oldman['위도'])

## 지역별 사고다발 지점, 발생건수, 사상자수, 사망자수

oldman

# 전체 데이터의 평균, 표준편차, 사분위수, 최소값, 최대값 확인
oldman.describe()

oldman_set = oldman.set_index(['시도시군구명', '지점명'])
oldman_set

# 각 지역별 사고다발지점에서의 사고 발생건수 및 사상자수의 합
oldman_sum = oldman.groupby('시도시군구명').sum()
oldman_sum = oldman_sum.reset_index()
oldman_sum

### 서울시 전체 데이터와 비교

accident = pd.read_csv('/content/drive/MyDrive/[D9&10] 데이터시각화 프로젝트_5조/Data/2020_노인교통사고현황.csv')
accident.head()

# 사망자수와 부상자수를 합하여 사상자수 컬럼 생성
accident['사상자수'] = accident['사망자수']+accident['부상자수']
accident.head()

# 연산을 위해 '지역'컬럼을 오름차순 정렬 후 reset_index 후 'index' 컬럼 제거
accident = accident.sort_values('지역').reset_index().drop('index', axis=1)
accident.head()

# (사고다발지역 사상자수)/(전체 사상자수) -> 사고다발지역의 사상자수가 전체 사상자수에서 차지하는 비율
oldman_sum['사고다발지역 사상자수 비율'] = round(oldman_sum['사상자수'] / accident['사상자수'] * 100, 2)
oldman_sum