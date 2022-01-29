### 보행노인사고다발지점 분석
 - 65세이상 인구수는 뺐습니다! 없어도 될 것 같아요!

from matplotlib import font_manager, rcParams
!apt-get install fonts-nanum*
rcParams['font.family'] = 'NanumGothicCoding'
rcParams['axes.unicode_minus'] = False
font_manager._rebuild()

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

plt.figure(figsize=(20,15))

img1 = mpimg.imread('/content/drive/MyDrive/[D9&10] 데이터시각화 프로젝트_5조/주예린/사고발생건수 상위4곳 로드뷰/1위 동작구 상도동(성대시장 인근).png')
plt.subplot(2, 2, 1) 
plt.imshow(img1)
plt.title("성대시장 인근 (사고발생건수 1위)",fontsize=25)
plt.axis('off')

img2 = mpimg.imread('/content/drive/MyDrive/[D9&10] 데이터시각화 프로젝트_5조/주예린/사고발생건수 상위4곳 로드뷰/2위 동대문구 제기동 (청량리청과물도매시장 인근).png')
plt.subplot(2, 2, 2)  
plt.imshow(img2)
plt.title("청량리청과물도매시장 인근 (사고발생건수 2위)", fontsize=25)
plt.axis('off')

img3 = mpimg.imread('/content/drive/MyDrive/[D9&10] 데이터시각화 프로젝트_5조/주예린/사고발생건수 상위4곳 로드뷰/3위(공동) 동대문구 용두동 (경동시장 인근).png')
plt.subplot(2, 2, 3)  
plt.imshow(img3)
plt.title("경동시장 인근 (사고발생건수 공동3위)", fontsize=25)
plt.axis('off')

img4 = mpimg.imread('/content/drive/MyDrive/[D9&10] 데이터시각화 프로젝트_5조/주예린/사고발생건수 상위4곳 로드뷰/3위(공동) 종로구 숭인동 (동묘 앞).png')
plt.subplot(2, 2, 4)  
plt.imshow(img4)
plt.title("동묘앞 인근 (사고발생건수 공동3위)", fontsize=25)
plt.axis('off')

plt.tight_layout()
plt.show()

img = mpimg.imread('/content/drive/MyDrive/[D9&10] 데이터시각화 프로젝트_5조/Data/횡단쉼터.png')
plt.figure(figsize=(15,15))
plt.imshow(img)
plt.title("<횡단쉼터>",fontsize=25)
plt.axis('off')
plt.show()

from google.colab import drive
drive.mount('/content/drive')

m = folium.Map(location=[37.58, 127.0], tiles="cartodbpositron", zoom_start=11)

# 사고다발지점(빨간색 원)
for i in oldman.index :
    folium.Circle(
        location = oldman.loc[i, ['위도', '경도']],
        radius = 100,
        color = 'red'
    ).add_to(m)

m

**ppt에 스트리트뷰 사진 첨부하시고 하단의 내용 추가하시면 될 것 같습니다**

- 노인보행자 교통사고의 발생 원인을 알아보기 위해 사고다발지점을 분석하였습니다.
- 서울시 전체 사고다발지점 데이터 중, 발생건수가 4 이상인 데이터를 추출하였습니다.
- 사고다발지점의 위도,경도 데이터를 이용하여 구글 지도에서 스트리트뷰를 확인하였으며, 사고원인으로 추정되는 변수를 데이터로 만들었습니다.
- 사고다발지점에 변수가 존재하면 1, 그렇지 않으면 0으로 표기하였습니다.
 - (사고다발지점 데이터는 2020년 기준이며, 구글 스트리트뷰는 2018년에 촬영되었으므로 시차를 감안하여주시면 감사하겠습니다.)

variable = pd.read_csv('/content/drive/MyDrive/[D9&10] 데이터시각화 프로젝트_5조/Data/variable.csv')
variable

variable.describe()

variable.mean()

- 변수가 존재하면 1, 그렇지 않으면 0으로 표기했기 때문에 평균값이 높으면 사고다발지점에서 변수가 존재하는 확률이 높다고 볼 수 있습니다.
 - 즉, 평균값이 높으면 해당 변수와 보행자교통사고 발생에 상관관계가 있다고 볼 수 있습니다.

variable[variable['발생건수'] > 4.98].mean()

variable[variable['발생건수'] < 4.98].mean()

- 흥미로운 점은 '발생건수'가 평균 발생건수보다 많은 지점의 경우, 평균 발생건수가 적은 지점에 비해 상대적으로 근처에 시장이 있을 확률이 높다는 사실입니다.
 - 노인 보행자 유동인구가 많을 수록 사건발생이 잦다고 생각해볼 수 있습니다.
 - 노인 보행자 교통사고 발생을 줄이기 위해서 시장처럼 노인 보행자 유동인구가 많은 지점에 노인 보행자 보호를 위한 방안이 필요해보입니다.

- '발생건수'가 평균 발생건수보다 적은 지점의 경우, 사고다발지점에 무신호횡단로가 있을 확률이 높았습니다.
 - 나이가 듦에 따라 신체능력(보행 속도 등)이 감소하여 신호등이 없는 횡단로에서 사고가 잦은 것으로 예상됩니다.
 - 사고 다발 지점에 추가적인 신호등 설치가 되어야 할 것입니다.

m = folium.Map(location=[37.58, 127.0], tiles="cartodbpositron", zoom_start=11)

# 지도에 사고다발지점 표시(빨간색 원, 반경 200미터)
for i in oldman.index :
    folium.Circle(
        location = oldman.loc[i, ['위도', '경도']],
        radius = 200,
        color = 'red'
    ).add_to(m)

# 지도에 노인보호구역 표시(파란색 원, 반경 300미터)
for i in silverzone.index :
    folium.Circle(
        location = silverzone.loc[i, ['위도', '경도']],
        radius = 300,
        color = 'dodgerblue'
    ).add_to(m)


m

- 서울시 보행노인사고다발지점과 노인보호구역을 지도에 시각화하였습니다.

- 서울시 전체 노인보호구역 145곳 중 17곳이 사고다발지점을 포함하고 있습니다.
 - 사고다발지점은 교통량과 노인유동인구가 많은 곳, 주택가에 위치하고 있습니다.
 - 반면에 노인보호구역은 노인복지관, 요양원 위주로 지정되어 있습니다.
   - 따라서 교통량과 노인유동인구가 많은 지점에 추가로 노인보호구역을 지정해야 합니다.
 - 노인보호구역으로 지정되었음에도 불구하고 사고다발지점인 곳이 존재합니다.
   - 단순히 노인보호구역 지정에만 그칠 것이 아닌, 노인보호구역에 대한 인식 제고 및 사후관리가 필요합니다.