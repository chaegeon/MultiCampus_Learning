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

action.columns

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