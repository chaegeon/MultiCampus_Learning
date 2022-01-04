# MLP 피드 가져오기
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # 대소문자 주의
from selenium.webdriver.chrome.service import Service
import time
service = Service( executable_path='C:/Users/chgeo/TIL/workspace/chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(service=service, options=options)
#일단 로그인 먼저
url = 'https://lc.multicampus.com/k-digital/#/login'
browser.get( url )
time.sleep(2) # 페이지가 로딩되기 전에 요소를 찾으면 결과가 안 나올 수도 있음
# 페이지가 완전히 로딩될 때 까지 기다렸다가 찾아주도록 하는 time을 import
# sleep(2) => 억지로 2초동안 대기 후 요소를 찾도록 설정한 거

# 속성에 공백이 들어간 경우 => 속성이 2개인 것. 하나의 속성만 검색해도 됨
inputs = browser.find_elements(By.CSS_SELECTOR, 'div.input-row-line input')
loginButton = browser.find_element(By.CSS_SELECTOR, 'div.btn-row button.login-btn')

inputs[0].send_keys('ID') # 아이디
inputs[1].send_keys('PW') # 패스워드
loginButton.click()

# 스크롤을 다 내려야 다음 피드가 생기는 경우
# 관리자 페이지에서 보면 스크롤을 다 내리면 <span>이 새로 생기는 걸 볼 수 있음
# 무한 스크롤(작정하고모든 내용을 전부 스크래핑)
last_height = browser.execute_script('return document.body.scrollHeight')# 도큐먼트의 스크롤 높이
while True:
    # 스크롤을 아래로 내리고
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    
    time.sleep(2) # 다음 스크롤이 생길 때까지 잠시 대기
    
    # 새로 높이를 재고
    new_height = browser.execute_script('return document.body.scrollHeight')
    
    # 높이가 이전과 같을 경우 더 이상 내려갈 스크롤이 없으므로 중지
    if new_height == last_height : break
    
    # 기존의 높이를 새로운 높이로 변경하고 다음 회차로 반복
    last_height = new_height

# 로드 된 내용을 수집
# 스크롤을 내리면서 피드를 가져올 수는 없음. 스크롤을 다 내리고 한 번에 가져와야 함
articles = browser.find_elements(By.CSS_SELECTOR, 'div.feedlist span article') # 피드리스트 스팬의 글들
for article in articles:
    for content in article.find_elements(By.CSS_SELECTOR, 'span.feedContentBlk span'): # 얘도 리스트라..
        print( content.text) # 콘텐트만 뽑아옴