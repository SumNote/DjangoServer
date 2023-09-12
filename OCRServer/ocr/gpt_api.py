import openai
import time
import json
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured


# Load your API key from an environment variable or secret management service
BASE_DIR = Path(__file__).resolve().parent.parent
secret_file = BASE_DIR / 'secrets.json'
with open(secret_file) as file:
    secrets = json.loads(file.read())

def get_secret(setting, secrets_dict=secrets):
    try:
        return secrets_dict[setting]
    except KeyError:
        error_msg = f'Set the {setting} environment variable'
        raise ImproperlyConfigured(error_msg)
    
openai.api_key = get_secret('GPT_SECRET_KEY')


        # 엔터티 : 정보의 기본 단위, 테이블로 표현\n\n
        # 관계 : 테이블 간의 연결\n\n
        # 인덱스 : 데이터 검색 속도 향상을 위한 구조\n\n
        # 일대일, 일대다, 다대다 : 엔터티 간 관계 유형\n\n
        # 뷰 : 하나 이상의 테이블로부터 파생된 가상 테이블\n\n
        # 무결성 : 데이터의 정확성과 일관성을 유지하는 규칙

# $데이터 베이스$, 줄여서 DB 특정 다수의 이용자들에게 필요한 정보를 제공한다든지 조직 내에서 필요로 하는 정보를 체계적으로 축적하여 그 조직 내의 이용자에게 필요한 정보를 제공하는 정보 서비스 기관의 심장부에 해당된다.
#    일반적으로 응용 프로그램과는 별개의 미들웨어[1]를 통해서 관리된다. 데이터베이스 자체만으로는 거의 아무 것도 못하기 때문에 그걸 관리하는 시스템과 통합돼 제공되며 따라서 정확한 명칭은 $데이터베이스 관리 시스템$(DBMS)[2]이 된다. 데이터베이스만 제공되는 건 CSV같이 아주 단순한 데이터에 국한되는데 이걸 직접 사용하는 경우는 많지 않고 이런 데이터를 RAW데이터로 간주해 다른 DBMS시스템에 적재하고 사용하는 게 일반적이다.
def gpt_sum(data):

    messages = []

        # 역할 부여
    messages.append(
        {"role" : "system",
        "content" : """
        당신은 주어진 텍스트를 하나의 주제(제목)에 대해 <핵심 단어> : <핵심 단어에 대한 문장>와 같은 형태로 요약하여 하나의 노트를 만들어주는 역할을 합니다. 
        당신이 작성하는 하나의 노트에는 []로 감싸진 하나의 제목만이 존재합니다.
        다음과 같은 요구사항을 따라 제공하는 텍스트를 제목을 포함하여 요약한 노트를 만들어주세요. 
        1. 핵심 키워드 혹은 핵심 문장은 $사과$와 같이 $로 처음과 끝을 감싸서 주어진 텍스트에서 제공됩니다.
        2. 핵심 문장이나 단어가 주어진 텍스트에 없는 경우 자신이 생각했을 때 중요하거나 핵심이라고 생각하는 부분을 핵심 단어로 정합니다.
        3. 핵심 문장이나 단어가 여러개인 경우 각각의 의미를 포함한 하나의 제목을 선정합니다.
        4. 요약된 노트의 제목은 []로 표현해야 하고, []로 되어 있는 제목은 이 노트에서 무조건 하나만 존재해야 합니다.
        5. 제목과 마지막 문장을 제외한 각 문장의 끝은 \n\n으로 표기하여 구분합니다.
        6. 각각의 문장은 <핵심 단어> : <핵심 단어에 대한 문장>와 같이 정리하며, 핵심 단어에 대한 문장은 되도록 짧게 요약합니다.
        7. 모든 문장이 7줄 이내가 되도록 즉, 핵심 단어가 7개가 넘어가지 않도록 하고 하나만 존재하는 제목에 대하여 하나의 필기노트로 요약하여 작성하세요. 다음 형식을 사용합니다.

        [요약된 노트의 제목]
        핵심 단어 : 핵심 단어에 대한 문장\n\n
        핵심 단어 : 핵심 단어에 대한 문장\n\n
        핵심 단어 : 핵심 단어에 대한 문장\n\n
        핵심 단어 : 핵심 단어에 대한 문장\n\n
        핵심 단어 : 핵심 단어에 대한 문장\n\n
        핵심 단어 : 핵심 단어에 대한 문장\n\n
        핵심 단어 : 핵심 단어에 대한 문장\n\n

        8. 이 노트에는 []로 감싸져 있는 제목이 하나만 존재해야 합니다.
        9. 제목을 제외한 핵심 단어나 문장을 []로 감싸지 않습니다.
        10. 위의 형식을 제외한 형식은 사용하지 않습니다.
        11. 주어진 텍스트 안에 있는 기호들 중 $ 기호를 제외하고는 전부 의미가 없으니 무시하세요.
        """}
    )

    # user_content = input("user : ")
    messages.append({"role": "user", "content": f"{data}"})

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    result = completion.choices[0].message["content"].strip()

    print(f"GPT : {result}")
    return result



def gpt_pro(data):

    # 역할 부여
    messages = [
        {"role" : "system",
        "content" : """
            당신의 역할은 4지선다 객관식 문제를 4문제 만드는 것입니다.
            아래 규칙을 따라 문제를 만들어주세요.
            1. 입력으로 문자열이 주어집니다. 이 문자열을 대상으로 문제를 만들면 됩니다.
            2. 문제의 시작과 끝은 &로 감쌉니다. 예를 들어 &다음중 사과의 색이 아닌것을 고르시오& 와 같습니다.
            3. 객관식은 #으로 시작하여 #으로 끝납니다. 예를 들어 
            #빨간색# 
            #노란색# 
            #초록색# 
            #보라색#
            와 같습니다.
            4. 문제에 대한 정답을 제공해야합니다. 예를들어 위 문제의 경우 정답은 보라색이므로 정답번호인 4를 리턴합니다.
            정답은 *로 감싸서 제공합니다. *4*
            5. 문제에 대한 해설을 제공해야합니다. 해설은 1줄에서 2줄 사이로 제공합니다. 해설은 @로 감싸서 제공합니다.
            @사과는 빨간색,노란색,초록색 등의 색상을 갖는데 보락색은 존재하지 않으므로 정답은 4번입니다.@

            최종 예시를 제공합니다.
            입력 : 
            [사과]
            과일의 하나이다. 과육은 기본적으로 노란색에서 연두색[2]이며, 맛은 품종마다 다르다. 아래 사과 품종 문단을 참고하자.

            일반적으로 한국에서 말하는 사과 맛은 달콤새콤 + 아삭아삭하게 씹히는 탄력이 있고 단단한 과육의 식감을 말한다. 종마다 다르지만 잘 익은 사과는 껍질이 벗겨지지 않은 상태에서도 청량감이 있는 좋은 냄새가 아주좋게 난다.

            너무 오래 두면 수분과 펙틱화합물(pectic compounds)이 감소하면서 과실의 경도가 낮아져 모래처럼 푸석푸석 해지는데, '사과(沙果, 모래열매)'라는 이름은 여기에서 유래한다.

            나이드신 기성세대 일부는 간혹 사과를 두고 능금이라 부르기도 한다. 능금은 Malus asiatica를 말하기 때문에 사과의 근연종일 뿐 서로 다른 종이라 구별해야 한다. 그러나, 능금 농사 풍년을 기원드린다고 쓰는 어른들이 간간히 있다.
            사과는 빨간색,노란색,초록색 등의 색상을 갖는다.

            출력:
            &다음중 사과의 색이 아닌것을 고르시오&
            #빨간색# 
            #노란색# 
            #초록색# 
            #보라색#
            *4*
            @사과는 빨간색,노란색,초록색 등의 색상을 갖는데 보락색은 존재하지 않으므로 정답은 4번입니다.@

        """},
    ]

    # user_content = input("user : ")
    messages.append({"role": "user", "content": f"{data}"})

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)


    result = completion.choices[0].message["content"].strip()

    print(f"GPT : {result}")
    return result