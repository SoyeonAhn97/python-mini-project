import requests
from bs4 import BeautifulSoup

URL = 'https://ecampus.kangnam.ac.kr/'
LOGIN_URL = 'https://ecampus.kangnam.ac.kr/login.php'
LOGIN_HEADER = {
    'Referer': 'https://ecampus.kangnam.ac.kr/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.198 Whale/2.9.115.16 Safari/537.36'
}
LOGIN_DATA = {
    'input-username': '201704049',
    'input-password': '****'
}

# Session 생성, with 구문 안에서 세션 유지, with 를 벗어나면 자동으로 세션 종료
with requests.Session() as s:
    # 로그인 데이터를 서버로 전송하고 응답을 response 에 저장 한다.
    response = s.post(LOGIN_URL, headers=LOGIN_HEADER, data=LOGIN_DATA)
    
    # 200이 나오면 정상 응답
    print(response.status_code)

    # 세션에서
    page = s.get(URL)

    # soup 만들기
    soup = BeautifulSoup(page.text, 'html.parser')
    #print(soup)

    print(page.text.find('로그아웃')) #로그인이 정상적으로 되었는지 확인용도