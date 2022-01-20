# 막대 + 꺾은 선 그래프 예시
day = ['Mon', 'Tue','Wed', 'Thu','Fri','Sat','Sun']
temp = [33, 29, 26, 36, 37, 32, 25]
num_icecream = [1000, 2000, 1100, 900, 1500, 1550, 2200]

fig = plt.figure(figsize=(8,8)) ## Figure 생성 
fig.set_facecolor('white') ## Figure 배경색 지정
ax1 = fig.add_subplot() ## axes 생성
 
colors = sns.color_palette('summer', len(day)) ## 바 차트 색상
 
xtick_label_position = list(range(len(day))) ## x축 눈금 라벨이 표시될 x좌표
ax1.set_xticks(xtick_label_position) ## x축 눈금 
ax1.set_xticklabels(day) ## x축 눈금 라벨
ax1.bar(xtick_label_position, num_icecream, color=colors) ## 바차트 출력
 
color = 'blue'
ax2 = ax1.twinx() ## 새로운 axis 생성
ax2.plot(xtick_label_position, temp, color=color, linestyle='--', marker='o') ## 선 그래프 
ax2.tick_params(axis='y', labelcolor=color) ## 눈금 라벨 색상 지정
 
plt.title('Sales Icecream and Temperature for Days', fontsize=20)
plt.show()
