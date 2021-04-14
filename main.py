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
    'input-password': '*a34013401'
}

# Session 생성, with 구문 안에서 세션 유지, with 를 벗어나면 자동으로 세션 종료
with requests.Session() as s:
    # 로그인 데이터를 서버로 전송하고 응답을 response 에 저장 한다.
    response = s.post(LOGIN_URL, data=LOGIN_DATA)
    # 로그인 결과 : 200이 나오면 정상 응답
    print(response.status_code)
    # 로그인 실패 시 : 200이 안나오면 오류
    if response.status_code != 200:
        print('request 실패')

    # 'Set-Cookie'로 MoodleSession 이라는 세션 ID 값이 넘어옴을 알 수 있다.
    print("********response.headers*******")
    print(response.headers)
    # cookie로 세션을 로그인 상태를 관리하는 상태를 확인해보기 위한 코드입니다.
    print("******s.cookies.get.dict()*******")
    print(s.cookies.get_dict())


    cookie = response.headers['Set-Cookie']
    print("********cookie********")
    print(cookie)
    # session의 header 안에 MoodleSession 쿠키를 추가합니다.
    #response.add_header('Cookie', cookie)

    # 여기서부턴 로그인이 된 세션이 유지됩니다. session 의 header 에는 Cookie 의 MoodleSession ID가 들어갑니다.
    response = s.get(URL)

    print("********response.headers*******")
    print(response.headers)
    # soup 만들기
    soup = BeautifulSoup(response.text, 'html.parser')
    ##print(soup)
