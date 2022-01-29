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
