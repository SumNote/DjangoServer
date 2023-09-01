from django.shortcuts import render
from .gpt_api import gpt_sum
from django.http import JsonResponse

# Create your views here.

def summary(request):
    # gpt_sum에 요약할 텍스트 삽입
    result = gpt_sum("""
        3 .알고리즘 설계와 구현
        알고리즘 설계
        ［그림 1-3 에서 본 바와 같이 컴퓨터 비전을 응용할 수 있는 분야는 무척 다양하며, 시스템이 동
        작하는 환경과 제약 조건에 따라 변화의 폭도 크다. 주어진 문제를 정확히 이해한 후 그 문제에 적
        합한 알고리즘을 새로 개발하거나 기존 알고리즘 중에서 그 문제에 가장 우수한 성능을 보이는 것
        을 선택하는 일은 아주 중요하다.
        컴퓨터 비전의 처리 절차는 ［그림 1-6 에서 본 바와 같이 여러 단계를 거친다. 각각의 단계는 여
        러 세부 문제로 구성되며, 이들 문제를 푸는 많은 종류의 알고리즘이 개발되어 있다. 사람의 손동
        작을 인식하는 문제를 생각해 보자. 손을 찾아내는 단계에서는 손 모델을 이용하여 매칭 연산을 한
        다. 에지나 영역을 사용해 연산하거나 SIFT와 같은 지역 특징을 사용할 수도 있다. 영역을 사용하
        기로 결정했다면, 여러 영역 분할 알고리즘 중에 어떤 것을 사용할지 결정해야 한다. 이러한 방법
        론적 다양성은 무엇을 뜻할까? 바로, 자신의 문제에 가장 적합한 알고리즘을 선별하는 작업이 어
        려울 뿐 아니라 아주 중요하다는 점이다.
        좋은 알고리즘을 찾기 위한 가장 확실하고 널리 사용하는 방법은 데이터베이스를 이용하여 실제
        성능 실험을 수행하고, 그 결과에 따라 알고리즘을 선택하는 것이다. 보통 적절한 알고리즘을 찾
        을 때까지 다양한 알고리즘을 적용해 보는 휴리스틱heuristic한 방식을 사용한다. 이때 주어진 문제
        에 대한 통찰력과 공학적인 경험을 갖추고 있다면 시행착오를 줄일 수 있다. 이 책은 이러한 능력
        을 갖추는 데 좋은 길잡이 노릇을 해 줄 것이다. 이 책은 주제별로 대표적인 알고리즘을 제시하는
        데, 그것들의 기본 원리를 대비시켜 좀더 깊이 이해할 수 있도록 도울 것이며 실제 응용과 관련 지
        어 장단점을 비교해 실용 시스템을 구축하는 데 필요한 통찰력을 길러줄 것이다.
        좋은 알고리즘을 선별하는 데 크게 도움이 되는 길잡이가 또 있다. 요즘 두드러진 연구 방향 중
        하나로, 표준 데이터베이스와 표준 성능 지표를 이용하여 여러 알고리즘의 성능을 객관적으로 비
        교 분석하는 일이다. 컴퓨터 비전에 관련된 학술대회나 학술지에는 이러한 연구 결과를 담은 논문
        이 많다. 알고리즘을 선별할 때 이들이 제시한 성능 비교 결과를 참조하는 것은 매우 현명한 자세
        이다. 예를 들어, 지역 특징을 비교한 Schmid2000, Mikolajczyk2005a, Mikolajczyk2005bL
        영 역 분할 알고리즘을 비교한 Estrada200이 등이 있다.

    """)

    response_data = {
        'summary': result,
    }

    return JsonResponse(response_data)
    