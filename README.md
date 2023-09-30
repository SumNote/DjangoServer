# OCR을 위한 DjangoServer

안드로이드로부터 사진을 전달받아 OCR 파이썬 코드를 작동시키기 위한 서버이다.

사용하기전 먼저 가상환경으로 진입해야 한다. 진입 방법은 아래와 같다.

source ./myenv/bin/activate

![1](https://github.com/y2hscmtk/Algorithm-Study/assets/109474668/cfa631a0-219a-4b0c-948d-8781b5cca87f)

가상환경을 종료하려면 deactivate명령을 입력하면 된다.

현재 상태(8월 4일)에서 OCRServer를 이용하기 위해 설치해야 하는 라이브러리는 아래와 같다.
라이브러리는 가상환경에 진입한 후 설치하는 것을 권장한다.

1. 터미널 창에서 원하는 폴더 위치에서 `git clone "복사한 링크"` 를 입력한다.

2. 다운 받은 폴더 위치로 이동한다. (최상위 폴더에 manage.py 파일이 위치하도록) ex) `cd OCRServer`
만약 현재 폴더 위치에 manage.py 파일이 있다면 이동할 필요 없다.

3. 가상환경을 만들어준다.
`python3 -m venv venv`

4. 가상환경을 실행한다.
`source venv/bin/activate`

5. pip install -r requirements.txt 를 터미널 창에서 실행한다.
<br>추가적으로 pytesserect 설치를 진행한다.
<br>brew install tesseract
<br>brew install tesseract-lang

6. manage.py 파일이 위치하도록 한 최상위 폴더에 secrets.json을 생성하고 내용은 노션을 참고하여 추가한다.
7. python3 manage.py makemigrations
8. python3 manage.py migrate
9. python3 manage.py migrate --run-syncdb

...(ocr코드 작성 이후 추가 예정)...

Django서버를 실행시키는 방법은 아래와 같다.

![2](https://github.com/y2hscmtk/Algorithm-Study/assets/109474668/236008e7-0c79-47e7-b52c-9c596f4d8d12)

python3 manage.py runserver


사용하는 API형식은 아래와 같으며 Body에 form-data로 이미지를 넣어 서버로 전송한다.

http://127.0.0.1:8000/imageToText/ 

서버에서 이미지 저장에 실패하여 OCR작업에 실패하였다면 {"text": "fail"} 형식으로 Json을 받는다.

![3](https://github.com/y2hscmtk/Algorithm-Study/assets/109474668/96d94c5c-55df-433b-a04d-dbd548ff6700)

서버에서 이미지 저장에 실패하여 OCR작업에 성공하였다면 {"text": "TextBook's Text String Data"} 형식으로 Json을 받는다.
(현재는 ocr코드가 완성되어있다고 가정하고 성공시 "TextBook's Text String Data"를 리턴하도록 하였다. 원래는 이곳에서 교과서에서 인식한 모든 글자들을 리턴받도록 한다.)

![4](https://github.com/y2hscmtk/Algorithm-Study/assets/109474668/7606baf3-e1a8-4988-8fee-ce88b9e6de7c)



