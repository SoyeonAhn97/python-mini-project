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
    print("response.status_code :", response.status_code)

    # 이러닝홈페이지를 GET방식으로 가져옵니다.
    print("*** 이러닝홈페이지를 GET방식으로 가져옵니다. ***")
    page = s.get(URL)

    # 로그인이 정상적으로 되었는지 확인용도
    print("*** 로그인 성공 여부(-1은 실패) ***")
    print(page.text.find('로그아웃'))

    # 기존 메인 페이지 soup 만들기
    print("*** 기존 메인 페이지 soup 만들기 ***")
    soup = BeautifulSoup(page.text, 'html.parser')

    # f = open("originPage.html", "w", encoding="utf-8")
    # f.write(page.text)
    # f.close()

    # a태그 찾기
    print("*** a태그 찾기 ***")
    courseLinkTag = soup.select('.course_label_re_03 a')
    coursePageList = list()
    #attendCountList = list()
    attendTableList = list()
    # a태그 속 href 로 세션만들기
    print("*** a태그 속 href 로 세션만들기 ***")
    for courseLink in courseLinkTag:
        print(courseLink.get('href'))
        coursePageList.append(s.get(courseLink.get('href')))

    # 교과목 페이지에서 진도 현황 가져오기
    print("*** 교과목 페이지에서 진도 현황 가져오기 ***")
    for page in coursePageList:
        print(page.text.find('허지욱'))
        html = BeautifulSoup(page.text, 'html.parser')
        #attendCountList.append(html.select('.att_count'))
        attendTableList.append(html.select('.user_attendance_table'))
    # 진도 현황 가져와졌는지 출력해보기
    print("*** 진도 현황 가져와졌는지 출력해보기 ***")
    for div in attendTableList:
        print(div)

    # CSS 가져와서 css.text 에 저장
    # print("*** CSS 가져와서 css.text 에 저장 ***")
    # css = s.get(CSS_URL)
    # f = open("css.txt", "w", encoding="utf-8")
    # f.write(css.text)
    # f.close()

    # attendCountList 를 attendCountList.txt 파일로 저장
    # print("*** attendCountList 를 attendCountList.txt 파일로 저장 ***")
    # f = open("attendCountList.txt", "w", encoding="utf-8")
    # f.write("")
    # f = open("attendCountList.txt", "a", encoding="utf-8")
    # for div in attendCountList:
    #     f.write(str(div))
    # f.close()

    # attendTableList 를 attendTableList.txt 파일로 저장
    print("*** attendTableList 를 attendTableList.txt 파일로 저장 ***")
    f = open("attendTableList.txt", "w", encoding="utf-8")
    f.write("")
    f = open("attendTableList.txt", "a", encoding="utf-8")
    for div in attendTableList:
        f.write(str(div))
    f.close()

    # attendCountList.txt 파일을 soup 으로 만듬
    # print("*** attendCountList.txt 파일을 soup 으로 만듬 ***")
    # f = open("attendCountList.txt", "r", encoding="utf-8")
    # soupAttendCountList = BeautifulSoup(f.read(), 'html.parser')
    # f.close()

    # attendTableList.txt 파일을 soup 으로 만듬
    print("*** attendTableList.txt 파일을 soup 으로 만듬 ***")
    f = open("attendTableList.txt", "r", encoding="utf-8")
    soupAttendTableList = BeautifulSoup(f.read(), 'html.parser')
    f.close()

    # css 적용하기
    div_css = "box-sizing : border-box; color : rgb(51, 51, 51); " \
              "font-family : NanumGothic; font-size : 14px; " \
              "line-height : 20px; text-size-adjust : 100%; width : 100%;"

    ul_css = "border-top-color : rgb(235, 235, 235); " \
             "border-top-style : solid; border-top-width : 1px; " \
             "border-bottom-color : rgb(235, 235, 235); " \
             "border-bottom-style : solid; border-bottom-width : 1px; " \
             "box-sizing : border-box; color : rgb(51, 51, 51); " \
             "line-height : 20px; list-style-image : none; " \
             "list-style-position : outside; list-style-type : none;"

    li_active_css = "background-color : rgb(255, 255, 255); " \
                    "border-right-color : rgb(235, 235, 235); " \
                    "border-right-style : solid; border-right-width : 1px; " \
                    "box-sizing : border-box; color : rgb(42, 123, 205); " \
                    "display : list-item; float : left; font-weight : 600; " \
                    "height : 80px;"

    li_inactive_css = "box-sizing : border-box; display : list-item; " \
                      "float : left; height : 80px; width : 38.75px; " \
                      "font-size : 12px; font-weight : 600; line-height : 17.1429.px; " \
                      "text-align : center; text-size-adjust : 100%; " \
                      "color : rgb(153, 153, 153); background-color : rgb(245, 245, 246); " \
                      "border-right-color : rgb(235, 235, 235); border-right-style : solid; " \
                      "border-right-width : 1px; list-style-image : none; list-style-position : outside;"

    p_active_css = ""

    p_inactive_css = ""

    # att_count 하위 css 필요
    # ...


    print("*** css 적용하기 ***")
    for i in range(0, len(attendTableList)):
        soupAttendTableList.select(".user_attendance_table")[i]['style'] = div_css
    for i in range(0, len(attendTableList)):
        soupAttendTableList.select(".attendance")[i]['style'] = ul_css
    for i in range(0, len(attendTableList) * 16):
        # if li .class가 active 일 때
        # p_active_css 적용
        # else (inactive) 일 때
        # p_inactive_css 적용

    # 각 강좌 버튼에 진도 현황 붙이기
    print("*** 각 강좌 버튼에 진도 현황 붙이기 ***")
    for course in soup.select(".course_label_re_03"):
        print(soupAttendTableList.select(".user_attendance_table")[0])
        course.append(soupAttendTableList.select(".user_attendance_table")[0])

    # reformPage.html로 저장
    print("*** reformPage.html로 저장 ***")
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
    print("os :", os)

    print("*** 창 열림 ***")
    if os == 'Darwin':
        webbrowser.get(chrome_path_mac).open('reformPage.html')
    elif os == 'Windows':
        webbrowser.get(chrome_path_windows).open('reformPage.html')
    elif os == 'Linux':
        webbrowser.get(chrome_path_linux).open('reformPage.html')
    else:
        print("운영체제를 찾지 못했습니다.")
