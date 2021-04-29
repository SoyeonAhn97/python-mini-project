# python-mini-project
파이썬 프로젝트

이러닝페이지 접근 -> GET방식으로 ~~login.php를 띄워줌 -> 폼 입력 후 버튼 클릭 -> index.php에 POST방식으로 request ->  서버에서 아이디를 비교 -> index.php는 303 See Other 응답 코드를 띄움 -> GET방식으로 이러닝페이지를 얻음

( status Code 303 : 요청에 대한 리소스는 다른 URI에 있기 때문에 GET 메서드를 사용해서 얻어야 한다는 것을 나타냄. 302 코드와 같지만, 303은 리디렉션 위치를 GET 메서드를 통해 얻어야 한다고 명확하게 되어 있음. 출처: https://ooz.co.kr/260 [이러쿵저러쿵] )
