# 막대 + 꺾은 선 그래프
fig = plt.figure(figsize=(8,8)) ## Figure 생성 
fig.set_facecolor('white') ## Figure 배경색 지정
 
colors = sns.color_palette('summer', len(day)) ## 바 차트 색상
 
xtick_label_position = list(range(len(day))) ## x축 눈금 라벨이 표시될 x좌표
plt.xticks(xtick_label_position, day) ## x축 눈금 라벨 출력
 
plt.bar(xtick_label_position, num_icecream, color=colors) ## 바차트 출력
plt.plot(xtick_label_position, num_icecream, color='b',
         linestyle='--', marker='o') ## 선 그래프 출력
plt.title('Sales Icecream for Days', fontsize=20)
plt.show()
