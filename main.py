import requests
from bs4 import BeautifulSoup

LOGIN_URL = 'https://ecampus.kangnam.ac.kr/login.php'
# LOGIN_DATA = {
#     'id': 'input-username',
#     'pwd': 'input-password'
# }
LOGIN_HEADER = {
    'Referer': 'https://ecampus.kangnam.ac.kr/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.198 Whale/2.9.115.16 Safari/537.36'
}

##예시
LOGIN_DATA = {
    'i6Ba4SXL8CY3xDMc':'Blablabla',
    'password':'Your Password',
    'user_id':'Your Id',
    's_url':'//www.dcinside.com/',
    'ssl':'Y'
}


# with requests.session() as s:
#     res = s.post(LOGIN_URL, data=LOGIN_DATA, verify=False)


URL = 'https://ecampus.kangnam.ac.kr'

response = requests.get(URL)
if response: #response null check
    print("response status code : ", response.status_code)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
else:
    print("response is null")
