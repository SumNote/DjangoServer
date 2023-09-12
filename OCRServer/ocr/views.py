from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from .ocr import do_ocr  # ocr.py에서 do_ocr 함수 import
from .gpt_api import gpt_sum, gpt_pro
import re

@csrf_exempt
def imageToText(request):
    # 이미지로 불러오는데 실패할 경우, fail이라는 값을 가져오게 끔 기본값을 fail로 설정
    response_data = {
            'text': "fail",
    }
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']

        try:

            # 디렉토리에 book.jpg이름으로 저장
            with open('media/book.jpg', 'wb') as f:
                for chunk in image.chunks():
                    f.write(chunk)
            print("image saved!")  # 저장 성공 로그 확인용

             # get_sum에 요약할 내용 입력
            sum_result = gpt_sum("""

            """)

            # 이미지에서 추출한 텍스트 받아오기
            result = do_ocr('media/book.jpg')

            # 분류 결과를 스마트폰으로 반환 (JSON 형태로 반환)
            response_data = {
                'text': result,
                'sum_result' : sum_result,
            }
            return JsonResponse(response_data)
        
        except Exception as e:
            print(f"Error saving image: {e}")
            JsonResponse(response_data)

    # 이미지를 저장하지 못했다면 => 앞서 저장한 fail이 Json으로 반환될 것임
    return JsonResponse(response_data)


@csrf_exempt
def imageToTextTest(request):
    # 이미지로 불러오는데 실패할 경우, fail이라는 값을 가져오게 끔 기본값을 fail로 설정
    response_data = {
            'text': "fail",
        }
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        # 디렉토리에 book.jpg이름으로 저장
        with open('media/book.jpg', 'wb') as f:
            for chunk in image.chunks():
                f.write(chunk)
        print("image saved!(test)")  # 저장 성공 로그 확인용

        # get_sum에 요약할 내용 입력
        sum_result = gpt_sum("""
본래 $원동기$의 동력을 이용하는 탈것은 사전적인 의미의 자동차에 속한다. 대한민국 법령에서는 원동기장치자전거[2], 전기자전거나 전동휠체어 등은 제외한 자동차관리법 제3조와 대통령령으로 규정하는 탈것을 자동차라고 한다. 군용차의 경우 기술적 제원으로는 군용무기로 간주해 자동차관리법의 적용대상은 아니지만, 공도상에서는 장갑차, 표준차량, 민수차량 모두 도로교통법상의 자동차로 인정한다는 대법원 판례(94도1519)가 있다.
도로교통법상 자동차는 자동차관리법 제3조에서 규정하는 $승용, 승합, 화물, 특수, 이륜$ 긴급자동차와 건설기계관리법 제26조 제1항에서 규정하는 건설기계[3]를 뜻한다. 다만, 법적으로 차와 자동차는 그 범주가 달라서, 굴착기 같은 건 차이지만 자동차는 아니다. 피자를 채소류로 정했다 해서 진짜로 피자가 채소가 되는 건 아닌 것처럼, 법이란 본래 기술적인 측면도 있어서, 같은 이륜자동차라 하더라도 배기량이 125 cc 이상이면 자동차이고, 그 이하이면 자동차가 아니라 원동기장치자전거가 된다. 경운기는 농기계의 일종일뿐 자동차에 해당하지는 않는다는 것이 판례이다.[4]

그러나 자동차가 아니라고 해도 사람 또는 가축의 힘이나 그밖의 동력에 의해 도로에서 운전되는 것에 해당하면 차마에는 해당한다고 볼 수 있다. 쉽게 생각해서 바퀴가 달린 탈것, 끌것은 대부분 '차마'인 것이다. 대표적으로 자전거가 있는데, 제반 교통규칙을 준수할 의무가 있는 점은 마찬가지이며 사고가 나면 교통사고처리특례법에 의해 처벌받는다. 노면전차의 경우 차마에 속하지 않지만 법적으로는 차마와 유사한 취급을 받는다.
""")

        # 정규 표현식을 사용하여 제목과 요약 추출
        title_match = re.search(r'\[(.*?)\]', sum_result)
        

        # title과 summary 추출
        title = title_match.group(1) if title_match else ""
        
        # 제목을 제외한 나머지 줄을 summary에 저장
        lines = sum_result.split('\n')
        summary = '\n'.join(lines[1:]) if len(lines) > 1 else ""

        # 결과 출력
        print("Title:", title)
        print("Summary:", summary)

        # 분류 결과를 스마트폰으로 반환 (JSON 형태로 반환)
        response_data = {
            'text': "08008는 동시에 사용할 수 있는 사용자의 수에 따라 단일사용자 08545와 다중사용\n자 28045로 나눌 수 있다. 실제 <ㅠㄴ는 하나이지만 여러 사용자가 동시에 사용할 수 있\n: 는것은 다중 프로그래밍의 개념을 이용하기 때문이다. 예를 들어 은행 업무 시스템이\n. 항공기 예약 시스템 등은 여러 명의 사용자가 동시에 이용하게 되므로 다중사용자\n_ 08)45에 속하게 된다.\n\n： 로잔의 간섭으로 인해 일관성이 파괴될 수 있다. 이와 같이 상황이 발생되지 않도록\n: 드란잭션의 실행 순서를 제어할 필요가 있는데 이러한 기법을 통시성 제어(000010500/\n000008라고 한다. 동시성 제어는 다중사용자 08148에서는 매우 중요한 문제이다.\n\n. 2-1 트랜잭션에서의 연산\n\n동시성 제어를 위한 방법을 설명하기 위해서 우선 트랜잭션에서의 연산들을 정의한다.\n용자 관점에서 데이터베이스에 대한 연산은 대부분 901문을 사용하는데 50[을 실행\n하기 위해서는 내부적으로 데이터베이스에 대한 읽기와 쓰기 연산이 요구된다. 예를 들\n이 90Ｌ의 5860문은 읽기 연산을 필요로 하고 40000문은 읽기와 쓰기 연산을 필요로\n다. 이처럼 데이터베이스에서 실행되는 연산들은 다음과 같이 읽기 연산과 쓰기 연산\n으로 단순화하여 표현할 수 있다.\n\n。 ,=4460:이름이 ×인 데이터베이스 항목을 트랜잭션의 지역변수 <로 읽어 들인다.\n\n。 ㅠ00660:지역변수 ×에 저장된 값을 데이터베이스 항목 *에 저장한다.\n\n여기서 ×는 테이블, 레코드, 필드 등 데이터베이스를 구성하는 임의의 구성 요소가 될\n수 있다. 이때 뚜의했야 할 점은 01000 연산을 수행했을 때 그 결과가 디스크에 즉시\n저장될 수도 있고 그렇지 않을 수도 있는 점이다. 대부분의 21805에서는 주기억상치에\n버퍼0>4007)를 두고 디스크에 저장해야 할 데이터들을 일시적으로 보관하였나가 나중\n\n에 블록(11000) 단위로 기록한다.  ：\n\n196 15900( 4    녕 605 00 (\n「   \"   0 +\n\n^ 시 210  '거  !   라  여류\n생 ! 12  9 0후그라 |\n\n371\n",
            'title' : title,
            'summary' : summary,
            'sum_result' : sum_result
        }
        return JsonResponse(response_data)
    # 이미지를 저장하지 못했다면 => 앞서 저장한 fail이 Json으로 반환될 것임
    return JsonResponse(response_data)


@csrf_exempt
def generateProblem(request):
    # 이미지로 불러오는데 실패할 경우, fail이라는 값을 가져오게 끔 기본값을 fail로 설정
    quiz = {
            'text': "fail",
    }

    if request.method == 'POST':
        

        # get_pro 에 해당 요약된 노트 내용 전달
        problem_result = gpt_pro("""

        """)

        # 정규 표현식을 사용하여 문자열을 파싱
        query_match = re.search(r'&(.+)&', problem_result)
        answer_list_matches = re.findall(r'#(.+?)#', problem_result)
        answer_num_match = re.search(r'(\d+)', problem_result)

        # query, answerList, answerNum 추출
        query = query_match.group(1) if query_match else ""
        answer_list = answer_list_matches if answer_list_matches else []
        answer_num = int(answer_num_match.group(1)) if answer_num_match else 0

        # 분류 결과를 스마트폰으로 반환 (JSON 형태로 반환)
        # Quiz 객체 생성
        quiz = {
            "query": query,
            "answerList": answer_list,
            "answerNum": answer_num
        }

        # Quiz 객체를 출력
        print(quiz)



        
        
        return JsonResponse(quiz)
    # 이미지를 저장하지 못했다면 => 앞서 저장한 fail이 Json으로 반환될 것임
    return JsonResponse(quiz)