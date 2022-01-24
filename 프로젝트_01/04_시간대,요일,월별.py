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

## 시간대별 시각화

plt.figure(figsize=(20,5))
n_data = len(time)
index = np.arange(len(time))
plt.bar(time, accident)
plt.show()

plt.figure(figsize=(23,5))
n_data = len(time)
index = np.arange(len(time))
plt.bar(time, accident)
plt.grid(True, alpha = 0.5, axis = 'y')

for i in range( len(time)):
  plt.text( i-0.1, accident[i]+2, f'{accident[i]}', size =15)

plt.show()

# 내림차순으로 정렬
seoul_sort = seoul.sort_values('1',ascending=False)
seoul_sort

time_s = seoul_sort['0'].values.tolist()
time_s

accident_s = seoul_sort['1'].values.tolist()
accident_s

## 결론

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

- 점심시간 전후부터 퇴근시간전까지
- 너무 당연...
- 의외로 그 다음은 오전 8시~10시
- 오후 8시~10시부터 절반수준으로 내려감 
- 어두운 시간보다는 밝은 시간에 사고가 더 많이 일어남