# OECD 노인보행자 사망자수
- 단위( 명/10만 명) 설명 추가
- 평균값을 계산해서 설명 추가

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

# 그래프에 추가할 평균선 평균 구하기
import numpy
arr = Per
average = numpy.mean(arr)
print(average)


## 시각화 및 결론

plt.figure(figsize=(23,5))
n_data = len(Country)
index = np.arange(len(Country))
plt.bar(Country,Per)

plt.ylabel('사망자 수')
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

- 대한민국의 10만명당 노인보행 중 사망자는 평균보다 약 2.6배나 높다
- 노인보행자 보호 대책이 시급하다




# 서울시 노인 교통사고 현황

accident = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/실습/Data폴더/서울시 노인 교통사고 현황.csv')
accident
# 2020년 만 65세 이상의 노인 교통사고

# 출처: TAAS 교통사고분석시스템(http://taas.koroad.or.kr/)

accident.columns

# 컬럼명 수정
accident.columns=['Unnamed', '기간', '지역', '노인교통사고_발생건수', '노인교통사고_사망자수', '노인교통사고_부상자수', '노인운전자교통사고_발생건수', '노인운전자교통사고_사망자수', '노인운전자교통사고_부상자수', '노인보행자_사망자수', '노인보행자_부상자수']

accident.head(5)

# 불필요한 컬럼 삭제
accident = accident.drop(columns = ['Unnamed', '기간'])
accident.head(5)

# 컬럼명과 중복되는 행 삭제
accident = accident.drop(index=[0])
accident.head(5)

accident['노인교통사고_사망자수'].unique()

def func(x):
    if x == '-' :
      x = '0'

# 결측치가 문자열 '-'로 되어있다.
# 일단 결측치인 '-'값들을 같은 문자열 '0'으로 변경
accident = accident.apply(lambda x: x.replace('-','0'), axis=1)
accident

accident.dtypes

# 데이터들을 숫자타입으로 변경
# accident = accident.apply(pd.to_numeric) -> 한 번에 바꾸려 했으나 '지역' 때문에 불가능
accident = accident.astype({'노인교통사고_발생건수':int, '노인교통사고_사망자수':int, '노인교통사고_부상자수':int, '노인운전자교통사고_발생건수':int, '노인운전자교통사고_부상자수':int, '노인운전자교통사고_사망자수':int, '노인보행자_사망자수':int, '노인보행자_부상자수':int})

accident.dtypes

accident.info()

accident

rawData = accident.drop(index=[1])
rawData.head(5)

rawData['지역']

rawData.columns

# '지역' 컬럼의 값들을 리스트로 변환
region = rawData['지역'].values.tolist()
region

death = rawData['노인보행자_사망자수'].values.tolist()
death

injury = rawData['노인보행자_부상자수'].values.tolist()
injury

# 지역별 부상자
plt.figure(figsize=(20,5))
n_data = len(region)
index = np.arange(len(region))
plt.bar(region,injury)
plt.show()

# 지역별 사망자
plt.figure(figsize=(20,5))
n_data = len(region)
index = np.arange(len(region))
plt.bar(region,death, color='r')
plt.show()

## 시각화 및 결론

# "부상자, 사망자"로 값을 표시
plt.figure(figsize=(25,10))
barWidth = 0.5
plt.bar(index, injury, color='c', width = barWidth, label='부상자')
plt.bar(index, death, color='r', width = barWidth, label='사망자')
plt.grid(True, alpha = 0.5, axis = 'y')

for i in range( len(region)):
  injury_r = injury[i]
  death_r = death[i]
  # plt.text( i+0.3, death[i], injury[i], '%d %/ %d')
  # plt.text( i-1, injury[i]+2, f'{death[i]}명 사망 / {injury[i]}명 부상')
  plt.text( i-0.6, injury[i]+2, f'부상{injury[i]},사망{death[i]}')


plt.xticks( index, region )
plt.legend()
plt.xlabel('지역')
plt.ylabel('사상자수')
plt.title('노인보행사고_사상자수')
plt.show()

- 지역별로 사상자(부상자+사망자)의 차이가 크다



# 사고발생 상황유형(보행자 행동별)

cross = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/실습/Data폴더/횡단중.csv')
cross
# 2020년 만 65세 이상의 노인 차대사람 사고 상황 유형
# 차대사람 데이터의 사상자는 보행자+차로 카운트되기 때문에
# 다른 데이터들과 비교해봤을 때 부상자가 12명이 더 많음. 차측 부상자인 듯
# 사고건수 - 사망자만 비교해봐야 할 듯

# 출처: TAAS 교통사고분석시스템(http://taas.koroad.or.kr/)

cross = cross.drop(columns=['Unnamed: 0', '2'])

cross['0'] = '횡단중_사고건수', '횡단중_사망자수', '횡단중_부상자수'
cross

road = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/실습/Data폴더/차도통행중.csv')
road

road = road.drop(columns= ['Unnamed: 0', '2'])
road

road['0'] = '차도통행중_사고건수', '차도통행중_사망자수', '차도통행중_부상자수'
road

side = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/실습/Data폴더/보도통행중.csv')
side

side = side.drop(columns= ['Unnamed: 0', '2'])
side

side['0'] = '보도통행중_사고건수', '보도통행중_사망자수', '보도통행중_부상자수'
side

edge = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/실습/Data폴더/길가장자리구역통행중.csv')
edge

edge = edge.drop(columns= ['Unnamed: 0', '2'])
edge

edge['0'] = '길가장자리통행중_사고건수', '길가장자리통행중_사망자수', '길가장자리통행중_부상자수'
edge

etc = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/실습/Data폴더/사고유형 기타.csv')
etc

etc = etc.drop(columns= ['Unnamed: 0', '2'])
etc

etc['0'] = '기타_사고건수', '기타_사망자수', '기타_부상자수'
etc

cross

road

side

edge

etc

action = pd.merge(cross, road, left_index = True, right_index=True)
action

action = pd.merge(action,side, left_index = True, right_index=True)
action

action = pd.merge(action, edge, left_index = True, right_index=True)
action

action = pd.merge(action, etc, left_index = True, right_index=True)
action

action.loc[0]

action = action.drop(columns=['0_x', '0_y', '0'])
action

action.columns = ['횡단중', '차도통행중', '보도통행중', '길가장자리통행중', '기타']

action.index = ['사고발생건수', '사망자수', '부상자수']
action

#action

action_a = action.columns

action = action.T
action

action = action.reset_index()
action

action.columns=['행동유형', '사고발생건수', '사망자수', '부상자수']
action

a_type = action['행동유형'].values.tolist()

a_type

num = action['사고발생건수'].values.tolist()
num

death = action['사망자수'].values.tolist()
death

injury = action['부상자수'].values.tolist()
injury

## 시각화 및 결론

fig = plt.figure(figsize=(8,8))
fig.set_facecolor('white')
ax1 = fig.add_subplot()
plt.ylim([0, 900])

xtick_label_position = list(range(len(a_type))) 
ax1.set_xticks(xtick_label_position) 
ax1.set_xticklabels(a_type) 
a_bar = ax1.bar(xtick_label_position, num, color='c', label = '노인보행사고 발생건수')
plt.xlabel('보행자 행동유형')
ax1.set_ylabel('노인보행자 사고발생건수')
for i in range( len(a_type)):
  plt.text( i-0.07, num[i]-20, f'{num[i]}', size = 14)
plt.legend(loc='best')


ax2 = ax1.twinx() 
d_plot = ax2.plot(xtick_label_position, death, color='r', linestyle='--', marker='o', label = '사망자 수')
ax2.tick_params(axis='y', labelcolor='r')
ax2.set_ylabel('사망자 수')
for i in range( len(a_type)):
  plt.text( i-0.25, death[i]-0.1, f'{death[i]}', size = 14, color='r')
plt.legend(loc=(0.81,0.9))

plt.title('보행자 행동유형별 사고발생건수와 사망자', fontsize=20)
plt.show()

- 횡단중일 때 발생한 사고건수가 2번째로 많고 사망자는 제일 많다
  - 신호등의 필요성이나 신호등 시간을 늘리거나 횡단쉼터설치 등의 대책방안을 생각해 볼 수 있음
- 차도통행이나 길가장자리 통행 사고도 많은데 이에 대한 해결방안은? 
  - 보도울타리, 중앙분리대 등

  

# 노인보행사상자 유형(사망,부상정도)


- 사상자: 사망자+부상자
- 사망: 사고 발생시로부터 30일이내에 사망한 경우
- 중상: 3주 이상의 치료를 요하는 부상
- 경상: 5일 이상 3주 미만의 치료를 요하는 부상
- 부상신고: 5일 미만의 치료를 요하는 부상

rawData = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/실습/Data폴더/연령별 보행사상자 유형.csv')
rawData

rawData = rawData.T
rawData

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

## 시각화 및 결론

plt.figure(figsize=(7,7))
wedgeprops = {'width':0.7, 'edgecolor':'w', 'linewidth':5}
plt.pie(rawData, labels = lab, autopct='%.1f%%',startangle=150, counterclock=False, wedgeprops=wedgeprops, colors = ['#1c9099','#1c9099','#a6bddb','#a6bddb'])
plt.show()

- 2020년 서울시 기준, 보행 중 교통사고를 당한 노인의 총 사상자는 1826명
- 보행 중 교통사고를 당한 노인들의 부상정도는 3주 이상의 치료를 요하는 중상이 절반 이상이다.
- 사망자수와 합하면 56%정도로 교통사고로 인한 노인 보행자의 부상정도가 심각하다고 볼 수 있다

- 문제제기 부분?


- 사상자: 사망자+부상자
- 사망: 사고 발생시로부터 30일이내에 사망한 경우
- 중상: 3주 이상의 치료를 요하는 부상
- 경상: 5일 이상 3주 미만의 치료를 요하는 부상
- 부상신고: 5일 미만의 치료를 요하는 부상



# 시간대,요일,월별 노인보행자사고 현황

# 2020년 만 65세 이상의 시간대, 요일, 월별 교통사고 - 차대사람
# 차대사람 : 사람기준이 아닌, 사고상황에 대한 용어. 사상자는 보행자+차

# 보행자 기준의 자료가 아닌, 차대사람 기준의 자료라서
# 다른 자료 대비 차쪽 부상자 12명이 추가되어 있음
# 특정 시간대/요일/월의 사상사 중 '보행자 사상자 수'만을 알 수가 없어 사상자 비교는 어려울 듯

# 출처: TAAS 교통사고분석시스템(http://taas.koroad.or.kr/)

## 시간대별

rawData = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/실습/Data폴더/time_a.csv')
rawData

# 출처: TAAS 교통사고분석시스템(http://taas.koroad.or.kr/)

rawData = rawData.T
rawData

rawData.index

rawData .columns

seoul = rawData.loc[['0', '1']]

seoul

seoul = seoul.drop(columns = [0])

seoul = seoul.drop(columns = [1])

seoul = seoul.T
seoul

seoul.index = ['0','1','2','3','4','5','6','7','8','9','10','11','12']

seoul

seoul = seoul.astype({'1':int})

seoul.info()

seoul

seoul = seoul.drop(index=['0'])

seoul

time = seoul['0'].values.tolist()
time

accident = seoul['1'].values.tolist()
accident

seoul

# 내림차순으로 정렬
seoul_sort = seoul.sort_values('1',ascending=False)
seoul_sort

time_s = seoul_sort['0'].values.tolist()
time_s

accident_s = seoul_sort['1'].values.tolist()
accident_s

### 시간대별 시각화 및 결론

plt.figure(figsize=(23,5))
n_data = len(time_s)
index = np.arange(len(time_s))
plt.bar(time_s, accident_s)
plt.grid(True, alpha = 0.5, axis = 'y')
plt.ylim([0, 300])
plt.legend()
plt.title('시간대별 사고발생건수')

for i in range( len(time_s)):
  plt.text( i-0.1, accident_s[i]+5, f'{accident_s[i]}', size =14)


plt.rc('xtick', labelsize=15)   
plt.rc('ytick', labelsize=20)  


plt.show()

- 점심시간 전후부터 퇴근시간전까지의 시간대에 사고가 가장 많이 발생
- 의외로 그 다음은 저녁시간대 보다 오전 8시~10시
- 오후 8시~10시부터 절반수준으로 내려감 
- 어두운 시간보다는 밝은 시간에 사고가 더 많이 일어남



## 요일별

rawData = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/실습/Data폴더/day_a.csv')
rawData

# 출처: TAAS 교통사고분석시스템(http://taas.koroad.or.kr/)

rawData = rawData.T
rawData

rawData.index

rawData .columns

seoul = rawData.loc[['0', '1']]
seoul

seoul = seoul.drop(columns = [0, 1])

seoul = seoul.T
seoul

seoul.index = ['0','1','2','3','4','5','6']
seoul

seoul = seoul.astype({'1':int})

seoul.info()

day = seoul['0'].values.tolist()
day

accident = seoul['1'].values.tolist()
accident

seoul

# 내림차순으로 정렬
seoul_sort = seoul.sort_values('1',ascending=False)
seoul_sort

day_s = seoul_sort['0'].values.tolist()
day_s

accident_s = seoul_sort['1'].values.tolist()
accident_s

### 요일별 시각화 및 결론

plt.figure(figsize=(15,5))
n_data = len(day_s)
index = np.arange(len(day_s))
plt.bar(day_s, accident_s)
plt.grid(True, alpha = 0.5, axis = 'y')
plt.ylim([0, 375])
plt.legend()
plt.title('요일별 사고발생건수')

for i in range( len(day_s)):
  plt.text( i-0.1, accident_s[i]+3, f'{accident_s[i]}', size =14)


plt.show()

- 별 상관 없는 것 같다.. 



## 월별

- 겨울에는 노인들의 몸이 굳어 사고가 더 많이 발생하지 않을까? 하는 가설에서 진행해보았다

rawData = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/실습/Data폴더/month_a.csv')
rawData

# 출처: TAAS 교통사고분석시스템(http://taas.koroad.or.kr/)

rawData = rawData.T
rawData

rawData.index

rawData .columns

seoul = rawData.loc[['0', '1']]
seoul

seoul = seoul.drop(columns = [0, 1])

seoul = seoul.T
seoul

seoul.index = ['0','1','2','3','4','5','6','7','8','9','10','11','12']
seoul

seoul = seoul.astype({'1':int})

seoul.info()

seoul = seoul.drop(index=['0'])
seoul

month = seoul['0'].values.tolist()
month

accident = seoul['1'].values.tolist()
accident

seoul

# 내림차순으로 정렬
seoul_sort = seoul.sort_values('1',ascending=False)
seoul_sort

month_s = seoul_sort['0'].values.tolist()
month_s

accident_s = seoul_sort['1'].values.tolist()
accident_s

### 월별 시각화 및 결론

plt.figure(figsize=(23,5))
n_data = len(month_s)
index = np.arange(len(month_s))
plt.bar(month_s, accident_s)
plt.grid(True, alpha = 0.5, axis = 'y')
plt.ylim([0, 225])
plt.legend()
plt.title('월별 사고발생건수')

for i in range( len(month_s)):
  plt.text( i-0.1, accident_s[i]+2.3, f'{accident_s[i]}', size =14)


plt.rc('xtick', labelsize=20)   
plt.rc('ytick', labelsize=20)  


plt.show() 

- 1, 10, 11월은 가장 많이 사고가 일어나지만 12월은 적다
- 다른 월과의 차이도 크지 않은 걸 보면 계절과는 상관없는 듯 하다