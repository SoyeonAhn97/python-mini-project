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
    # 로그인 시도
    login_req = s.post(LOGIN_URL, data=LOGIN_DATA, allow_redirects=False)
    # 로그인 결과 : 200이 나오면 request 날리기 성공!
    print(login_req.status_code)
    # 로그인 실패 시 : 200이 안나오면 request 날리기 실패
    if login_req.status_code != 200:
        print('request 실패')

    # cookie = login_req.headers['Set-Cookie']
    # print(cookie)

    # 페이지 html 가져오기
    url_html = s.get(URL)
    # soup 만들기
    soup = BeautifulSoup(url_html.text, 'html.parser')
    print(soup)
