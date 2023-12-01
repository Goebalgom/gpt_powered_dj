# ChatGPT & 파이썬으로 AI 직원 만들기 실습

**<Do it! 챗GPT&파이썬으로 AI직원 만들기>** 책의 실습 코드를 작성한 저장소입니다.  
OpenAI API 레퍼런스 사이트를 같이 참고하여 작성하여 코드가 책과 다소 다릅니다.  

### API 키 ###
로컬에 .env 파일로 작성한 뒤 [python-dotenv 라이브러리](https://pypi.org/project/python-dotenv)를 이용하여 환경변수에 추가하고,  
os 패키지의 environ.get 함수를 이용해 불러서 사용합니다.

### OpenAI API 사용 ###
[Quickstart 가이드](https://platform.openai.com/docs/quickstart?context=python)에 따라 api key를 파라메터로 갖는 객체를 생성하여 사용합니다.  

### 사용 예 ###
```python
from os import environ
from dotenv import load_dotenv
from openai import OpenAI

...

load_dotenv()

client = OpenAI(api_key=environ.get('OPENAI_API_KEY'))
```
