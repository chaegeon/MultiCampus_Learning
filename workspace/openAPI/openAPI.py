clientID = "cDNffGVA2nC2U_fASyE7"
clientSecret = 'T00FPlJpbY'

import requests
import json

url = 'https://openapi.naver.com/v1/datalab/search'
header = {
    'X-Naver-Client-Id' : 'cDNffGVA2nC2U_fASyE7',
    "X-Naver-Client-Secret": 'T00FPlJpbY',
    'Content-type' : 'application/json'
}
data = {
    'startDate' : '2021-01-01',
    'endDate' : '2021-12-31',
    'timeUnit' : 'month',
    'keywordGroups' : [
      {
        'groupName' : '이재명',
        'keywords' : ['더불어민주당', '이재명']
      },
      {
        'groupName' : '윤석열',
        'keywords' : ['국민의힘', '윤석열']
      },
      {
        'groupName' : '허경영',
        'keywords' : ['국가혁명당', '허경영']
      },
      {
        'groupName' : '심상정',
        'keywords' : ['정의당', '심상정']
      },
      {
        'groupName' : '안철수',
        'keywords' : ['국민의당', '안철수']
      },
    ],
    'ages' : ['3', '4', '5', '6', '7', '8', '9', '10', '11']
}

jsonData = json.dumps(data)
reponse = requests.post( url, data=jsonData, headers=header)
print(reponse.status_code)

print(reponse.json())