# KNU 이러닝캠퍼스 UI 개선하기
***
## 프로젝트 배경
>코로나로 인해 대부분의 수업을 비대면으로 진행하게 되면서 대부분의 시간을 학교가 아닌 이러닝 캠퍼스에서 보내게 되었습니다. 학생들이 이러닝 캠퍼스에서 가장 많이 이용하는 부분은 온라인 수업을 듣고 출석이 잘되었나 확인하는 부분이었는데, 기존의 이러닝 캠퍼스에서는 과목을 하나하나 들어가 확인해야만 했습니다. 그러다보니 출석을 놓치는 경우가 생기기도 했고 비효율적이라고 생각하여 진행하게 되었습니다.

## 사용 모듈
* **BeautifulSoup**
* **Webbrowser**
* **Platform**
* **requests**

## 사용 방법
**main.py를 실행**하고 콘솔창에 **학번과 비밀번호를 입력**하면 'reformPage.html' 파일이 생기고 크롬에서 열리게 됩니다.

## 결과( Before )
<img src="https://user-images.githubusercontent.com/60254939/120756059-bf6fed00-c549-11eb-9176-f233f43225f2.png"  width="80%" height="80%">

## 결과( After )
<img src="https://user-images.githubusercontent.com/60254939/120755931-918aa880-c549-11eb-865e-c31644a70c32.png"  width="80%" height="80%">

## 동작 구조
1. 이러닝 캠퍼스 로그인
2. BeautifulSoup을 이용해 페이지 html 파싱
3. href 태그를 이용해 각 과목 페이지 접근
4. 출석 현황 html 코드 파싱
5.  메인페이지 html에 삽입
6.  webbrowser 모듈을 이용해 수정된 html을 크롬으로 동작


***
