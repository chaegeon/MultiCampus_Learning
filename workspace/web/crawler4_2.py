# 두번째 실습은 쇼핑몰 후기 가져오기
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # 대소문자 주의
from selenium.webdriver.chrome.service import Service
# selenium은 bs4 없어도 파싱 가능

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# sebdriver
# 크롬을 기준으로 현재 사용하고 있는 버전에 맞춰서 다운로드 해줘야 함
# 크롬 실행 - 설정 - 도움말 - 크롬정보
# 나는  96.0.4664.110
# 구글에 chrome webdriver 검색하면 다운로드 뜸
# 버전 맞는 거( 96 까지만 맞으면 되는 듯?) 클릭한 뒤 윈도우버전으로 다운로드
# 압축해제 후 .exe 파일을 작업폴더로 이동
service = Service( executable_path='C:/Users/chgeo/TIL/workspace/chromedriver.exe')
browser = webdriver.Chrome(service=service, options=options)
# 이렇게 뜬 브라우저 객체로 제어
url = 'https://www.naver.com'
browser.get( url )
# element는 find나 select_one, elements는 find_all이나 select_all
# element = browser.find_element(By.CSS_SELECTOR, 'input#query') # id가 '쿼리'인 Input요소를 찾음 (지금은 네이버 검색창 찾고 있음)
# 없는 요소를 찾으려고 하면 터미널에 NoSuchElementException 가 뜸
# 객체가 반환되었다는 건, 해당 요소를 찾았다는 뜻

# print( element)
# 터미널의
# <selenium.webdriver.remote.webelement.WebElement (session="fa1b239682c480cc5f3c276174b62ee1", element="cda04d68-2694-4562-9266-f9aa72b125a4")>
# 이게 네이버 검색창의 요소를 찾은 거

# element.send_keys('검색어') # 뜨는 브라우저 검색창에 '검색어'가 써있음
# element.send_keys('\n') # 검색어 입력하고 엔터까지 쳐지도록
# element.send_keys

# 위에는 검색어 입력 후 엔터였다면,
# 검색어 입력 후 마우스 클릭하려면?
# 클릭 가능한 요소라면 클릭이 가능
input = browser.find_element(By.CSS_SELECTOR, 'input#query') # 입력할 요소 찾고
button = browser.find_element(By.CSS_SELECTOR, 'button#search_btn') # 버튼 요소 찾고
input.send_keys('검색어')
button.click()

# 연속으로 검색하려면, 검색한 창에서 또 다시 검색창 위치를 찾아서
# 기존 검색어를 지워주고 다시 입력 후 검색
input2 = browser.find_element(By.CSS_SELECTOR, 'input#nx_query')
input2.clear() # 기존의 검색어를 지워줌
input2.send_keys('두번째 검색어')
