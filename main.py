import platform
import requests
import webbrowser
from bs4 import BeautifulSoup

URL = 'https://ecampus.kangnam.ac.kr/'
LOGIN_URL = 'https://ecampus.kangnam.ac.kr/login/index.php'
LOGIN_HEADER = {
    'Referer': 'https://ecampus.kangnam.ac.kr/login.php',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/90.0.4430.85 Safari/537.36'
}
CSS_URL = 'https://ecampus.kangnam.ac.kr/theme/styles.php?theme=coursemosv2&rev=1620358043&type=all'

LOGIN_DATA = {
    'username': input("username : "),
    'password': input("password : ")
}

# #*** 테스트용 ***#
# LOGIN_DATA = {
#     'username': '201704049',
#     'password': '****'
# }

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
    # ************ 테스트 중 **********#
    f = open("test.html", "w", encoding="utf-8")
    f.write(page.text)
    f.close()
    # *******************************#

    # a태그 찾기
    courseLinkTag = soup.select('.course_label_re_03 a')
    coursePageList = list()
    attendCountList = list()

    # a태그 속 href 로 세션만들기
    for courseLink in courseLinkTag:
        print(courseLink.get('href'))
        coursePageList.append(s.get(courseLink.get('href')))

    # 교과목 페이지에서 진도 현황 가져오기
    for page in coursePageList:
        print(page.text.find('허지욱'))
        html = BeautifulSoup(page.text, 'html.parser')
        attendCountList.append(html.select('.att_count'))

    # 진도 현황 가져와졌는지 출력해보기
    for div in attendCountList:
        print(div)

    # CSS 가져와서 css.text 에 저장
    css = s.get(CSS_URL)
    f = open("css.txt", "w", encoding="utf-8")
    f.write(css.text)
    f.close()

    # attendCountList 를 attendCountList.txt 파일로 저장
    f = open("attendCountList.txt", "w", encoding="utf-8")
    f.write("")
    f = open("attendCountList.txt", "a", encoding="utf-8")
    for div in attendCountList:
        f.write(str(div))
    f.close()

    # attendCountList.txt 파일을 soup 으로 만듬
    f = open("attendCountList.txt", "r", encoding="utf-8")
    soupAttendCountList = BeautifulSoup(f.read(), 'html.parser')
    f.close()
    print(soupAttendCountList)

    # 각 강좌 버튼에 출석 횟수 붙이기
    for course in soup.select(".course_label_re_03"):
        course.append(soupAttendCountList.select(".att_count")[0])

    f = open("reformPage.html", "w", encoding="utf-8")
    f.write(str(soup))
    f.close()

    # MacOS
    chrome_path_mac = 'open -a /Applications/Google\ Chrome.app %s'
    # Windows
    chrome_path_windows = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    # Linux
    chrome_path_linux = '/usr/bin/google-chrome %s'

    # Mac : 'Darwin', Windows : 'Windows', Linux : 'Linux'
    os = platform.system()

    if os == 'Darwin':
        webbrowser.get(chrome_path_mac).open('reformPage.html')
    elif os == 'Windows':
        webbrowser.get(chrome_path_windows).open('reformPage.html')
    elif os == 'Linux':
        webbrowser.get(chrome_path_linux).open('reformPage.html')
    else:
        print("운영체제를 찾지 못했습니다.")

