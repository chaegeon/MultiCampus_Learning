# 두번째 실습은 쇼핑몰 후기 가져오기
# import requests
# import bs4

# url = 'http://itempage3.auction.co.kr/DetailView.aspx?itemno=C319609831'
# response = requests.get(url)
# html = bs4.BeautifulSoup( response.text, 'html.parser')

# elements = html.select_one('div#divVipReview')
# print(elements)

# 터미널에 <div id="divVipReview"></div> 라고는 뜨는데
# 근데 하나도 안 나와
# -> 자바스크립트가 실행이 된 이후에야 화면에 표현이 되는거라 ( <script> 이 부분 )
# 그럼 자바스크립트를 먼저 실행한 후에 크롤링을 해야 됨
# -> 파이썬을 통해 브라우저를 직접 제어할 것?
# 브라우저를 통해서 요청을 하면, 웹서버에서는 자바스크립트가 섞인 응답을 할텐데
# 브라우저가 자바스크립트를 실행을 함. 그 이후에 페이지를 가져오면 됨
# 파이썬 - 웹브라우저 - 웹서버