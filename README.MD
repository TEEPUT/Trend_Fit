<h1>Stack</h1><br>
<div align=center> 
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 
  <img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white"> 
  <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
  <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white">
  <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
  <img src="https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white"><br>
  <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
  <img src="https://img.shields.io/badge/jquery-0769AD?style=for-the-badge&logo=jquery&logoColor=white">
  <img src="https://img.shields.io/badge/pythonanywhere-1D9FD7?style=for-the-badge&logo=pythonanywhere&logoColor=white">

</div>


<h1>Intro</h1><br>

jquery와 bootstrap을 주로 프론트와 SQLite로 로그인만 설계한 토이 프로젝트입니다<br><br>

백엔드는 SQLite 를 사용해서 회원가입과 로그인 기능만 구현했습니다<br><br>


<h1>Implementation</h1><br>
<h2>Frontend</h2>
<div align="center">

**메인화면**

</div>

메인화면은 사용자에게 사이트를 탐색하는 데 도움을 주는 직관적이고 효과적인 방법을 제공합니다 <br><br>

네비게이션 상단의 위치 안내: 네비게이션 바에서 현재 위치를 확인할 수 있어 사용자가 어디에 있는지 쉽게 파악할 수 있습니다<br><br>

광고 슬라이더: 사이트에 처음 접속하면 사용자의 시선을 사로잡기 위해 큰 슬라이더에 광고를 표시합니다. 이를 통해 사용자에게 핵심 메시지를 전달하고 관심을 끌어냅니다<br><br>

베스트 상품 랭킹: 사이트 내에서 가장 인기 있는 상품을 보여주는 베스트 상품 랭킹을 제공합니다. 드래그로 아래로 내리면 카테고리별로 정렬된 베스트 상품을 볼 수 있어 사용자의 취향에 맞는 상품을 빠르게 찾을 수 있습니다<br><br>

전체 카테고리 정렬: 더 많은 상품을 탐색하고자 하는 사용자를 위해 전체 카테고리 정렬을 제공합니다. 이를 통해 다양한 상품을 한눈에 확인할 수 있습니다<br><br>

브랜드 연결: 각 브랜드별로 연결되는 링크를 제공하여 사용자가 자주 이용하는 브랜드의 제품을 쉽게 찾을 수 있습니다<br><br>

관련 네트워크 및 푸터: 하단으로 스크롤하면 사이트와 관련된 추가 정보와 푸터가 표시됩니다. 이를 통해 사용자가 사이트의 더 많은 기능 및 정보를 액세스할 수 있습니다<br><br>

<div align="center">

**회원가입**

</div>

아이디와 이메일 비밀번호를 입력하고 비밀번호를 잘못 입력했을 경우를 대비해서 비밀번호 확인까지 구현했습니다<br><br>

비밀번호는 해시형태로 저장됩니다 <br><br>


<div align="center">

**로그인**

</div>

한눈에 보기 쉽게 사각형 박스 안에 아이디와 비밀번호를 입력하게 했습니다 <br><br>

<h2>Backend</h2>
<div align="center">

**App.py**

</div>
Flask 메인 창이며 라우터 정의와 데이터 방식을 주고 받은 Controller 역할을 합니다<br><br>

<div align="center">

**Form.py**

</div>
회원가입 시 비밀번호 확인 창이 있는데 이게 정상적으로 입력이 됐는지 확인하는 역할입니다 <br><br>

<div align="center">

**Forms.py**

</div>
로그인 시 정상적으로 입력 됐는지 확인하는 역할입니다 <br><br>
<div align="center">

**Models.py**

</div>
데이터베이스를 만들는 역할과 입력하는 역할이며 이곳에서 비밀번호를 해시화 해서 데이터베이스에 저장가능하도록 합니다

<br><br>
<h1> Last </h1><br>

[https://teeput.pythonanywhere.com/Login.html](https://teeput.pythonanywhere.com/Main.html)https://teeput.pythonanywhere.com/Main.html

Flask로 백엔드를 구축하고 배포는 pythonanywhere로 했습니다

