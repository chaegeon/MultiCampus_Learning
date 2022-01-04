import requests
from fake_useragent import UserAgent

agent = UserAgent()
header = {'User-Agent':agent.chrome}

url = '이미지 URL' # 저장된 사진은 지우고 깃헙

response = requests.get(url, headers=header)

with open('web/data/download4.jpg', 'wb') as file:
  file.write( response.content )