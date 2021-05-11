import requests
from bs4 import BeautifulSoup

URL = 'https://ecampus.kangnam.ac.kr/'
LOGIN_URL = 'https://ecampus.kangnam.ac.kr/login/index.php'
LOGIN_HEADER = {
    'Referer': 'https://ecampus.kangnam.ac.kr/login.php',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/90.0.4430.85 Safari/537.36'
}
LOGIN_DATA = {
    'username': input("username : "),
    'password': input("password : ")
}

# Session 생성, with 구문 안에서 세션 유지, with 를 벗어나면 자동으로 세션 종료
with requests.Session() as s:
    # index.php에 로그인 요청 
    response = s.post(LOGIN_URL, headers=LOGIN_HEADER, data=LOGIN_DATA)

    # 200이 나오면 정상 응답
    print(response.status_code)

    # 이러닝홈페이지를 GET방식으로 가져옵니다.
    page = s.get(URL)

    # 로그인이 정상적으로 되었는지 확인용도
    # print(page.text)
    print(page.text.find('로그아웃'))

    # soup 만들기
    soup = BeautifulSoup(page.text, 'html.parser')
    # print(soup)

    # a태그 찾기
    courseLinkTag = soup.select('.course_label_re_03 a')
    coursePage = list()
    attendBox = list()

    # a태그 속 href 로 세션만들기
    for courseLink in courseLinkTag:
        print(courseLink.get('href'))
        coursePage.append(s.get(courseLink.get('href')))

    # 교과목 페이지에서 진도 현황 가져오기
    for page in coursePage:
        print(page.text.find('허지욱'))
        html = BeautifulSoup(page.text, 'html.parser')
        attendBox.append(html.select('.user_attendance_table'))

    # 진도 현황 가져와졌는지 출력해보기
    for div in attendBox:
        print(div)
