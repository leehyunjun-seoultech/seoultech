# README.md
별도의 언급없는 환경은 window 10, 파이썬 3.x 64bit가 default 입니다.


# AutoStockTrade

CREON Plus API를 사용하여 주식 자동매매를 실행하고 그 결과를 slacker 라이브러리를 사용, slack bot을 통해 매매 알림을 받을 수 있습니다.

"파이썬 증권 데이터 분석" 책 및 github을 참고하였습니다.
https://github.com/INVESTAR/StockAnalysisInPython

### 환경
Python version == 3.x 32bit 및 IDE가 관리자 권한으로 설정

대신증권 CREON Plus에 로그인

os == window10 // win32com 및 pywinauto 모듈의 제약

아래의 CREON Plus API 홈페이지에 있는 코드들을 통해서 원하는 작업을 할 수도 있습니다.
https://money2.creontrade.com/e5/mboard/ptype_basic/plusPDS/DW_Basic_List.aspx?boardseq=299&m=9505&p=8833&v=8639

### 사전 금융 지식

변동성 돌파 전략 : 지난날의 고가와 저가의 차이를 계산해서 k 만큼 곱한 값을 오늘 시가에서 변동 폭 만큼 올랐으면 매수하는 전략

1. 최유리 : 당장 가장 유리하게 매매할 수 있는 가격

2. 최우선 : 우선 대기하는 가격

3. IOC : 체결 후 남은 수량 취소

4. FOK : 전량 체결되지 않으면 주문 자체를 취소

### AutoTrade.py

win32com는 윈도우 상에서 Python을 이용하여 ActiveX 함수를 호출할 수 있도록 하는 라이브러리

자동매매 알고리즘은 변동성 돌파전략을 사용했으며 수수료를 고려하여 주식보다는 ETF 상품에 초점이 맞춰져 있습니다. 

변동성 돌파전략이 단타전략이기 떄문에 수수료를 고려해야 합니다. (ETF 상품이 수수료가 주식보다 저렴)

시간은 LP(유동성 공급자) 활동 시간(09:05 ~ 15:20)에 맞춰져 있으며 주문 호가는 최유리 FOK 방식을 사용했습니다.

활동 시간안에 매매를 하며 15:15에는 보유한 품을 모두 매도를 합니다.

### 주요code

8 code 자신의 slack의 oauth

134 code 변동성 돌파전략의 변동폭 비율, 현재는 0.5

246 code 매수하고자 하는 종목코드 리스트 // ex) https://finance.daum.net/quotes/A360140#home 마지막 "A360140" 가 종목코드

263 ~ code 매매 시간설정


### AutoConnect.py

pywinauto는 윈도우 O/S용 프로그램의 다이얼로그나 컨트롤에, 마우스 클릭이나 키보드 입력 등을, 사람이 직접 하지 않고 프로그램이 대신할 수 있도록 해주는 python 라이브러리

이 라이브러리를 사용하여 매번 로그인을 하지않도록 자동으로 로그인이 되게 만들었으며 15번쨰 줄에 id, pw, 공인인증서 pw를 입력하면 됩니다.

윈도우의 경우, 윈도우 키 -> 작업 스케줄러 앱을 통해서 위의 과정 모두 자동화가 가능합니다.

코드의 C:\CREON\STARTER\coStarter.exe 크레온이 깔려있는 경로입니다.

# Homomorphic Encryption(pi-HEaaN)
pi-HEaaN version 0.2.0에 대한 튜토리얼을 따로 정리한 코드입니다.

# Sentiment analysis

댓글을 수집 한 후 싫어요 대비 좋아요가 더 많은 기준으로 100개의 각 언론사별 댓글로 전처리 및 학습 후 감성 분석을 통해서 보수 진보를 구별 한 후 각 언론사 별 구독자 성향을 조사할 수 있습니다.

수집한 댓글은 형태소 분석기 Okt(KoNLPy 0.5.2) 사용 및 NLTK(3.6.2)로 자연어 처리, keras의 Sequential 모델을 사용하여 1 = 보수, 0 = 진보로 분류, 각 언론사 댓글을 통해 어느쪽 정치 성향이 많이 보는지를 파악 할 수 있습니다.

N2H4는 네이버 포털, DNH4는 다음 포털에서 각각 사용

### DNH4 라이브러리 사용예시

install.packages("DNH4") 설치, library(DNH4)불러옴 (N2H4도 똑같이 적용)

getContent() == 기사 url을 입력으로 받아 관련 내용을 크롤링

getMainCategory() == 기사의 대분류 항목을 가져옴

getSubCategory() == 기사의 소분류 항목을 가져옴

getUrlListByCategory() == 뉴스 리스트 페이지에서 기사의 제목과 링크를 가져옴

getMaxPageNum() == 뉴스 리스트 페이지의 마지막 페이지 번호 가져옴

getComment() == 기사 url을 입력으로 받아 그 기사의 댓글 정보를 가져옴 

comments<-as.data.frame(comments)로 데이터프레임으로 만들고 원하는 열을 가져올 수 있다.

1. 각 포털별 뉴스 크롤링.R을 통해서 댓글을 수집한 후 

2. 기사 전처리.py를 통해서 싫어요 대비 좋아요가 많은 상위 100개를 병합

3. 전처리한 csv파일을 가지고 포털사이트 뉴스 댓글 분석.py에 입력

# Transformer

논문 제목 : "Attention Is All You Need" 
링크 : https://arxiv.org/pdf/1706.03762.pdf%EF%BC%89%E6%8F%8F%E8%BF%B0%E4%BA%86%E8%BF%99%E6%A0%B7%E5%81%9A%E7%9A%84%E5%8E%9F%E5%9B%A0%E3%80%82

트랜스포머(Transformer)는 "Attention is all you need"에서 나온 모델로 기존의 seq2seq의 구조인 인코더-디코더를 따르면서 어텐션(Attention)만으로 구현한 모델입니다. 
이 모델은 RNN을 사용하지 않고, 인코더-디코더 구조를 설계하였음에도 성능도 RNN보다 우수하다는 특징을 갖고 있습니다.

pytorch를 사용해서 Transformer 모델을 구현하였습니다.
사용한 데이터는 WMT14 데이터이고 GPU환경 문제로 인해서 코랩에서 작업하였습니다.

spacy(2.2.4)를 사용해서 자연어 처리, 2개의 Field로 구성, BucketIterator로 모든 텍스트 작업을 일괄로 처리하고 단어를 인덱스 숫자로 변환 후에 트랜스포머 모델 입력값으로 입력한다.

입력값을 받고 embedding layer과 position encoding layer를 거친다.

트랜스포머를 각 단위별로 클래스를 만들고 인스턴스를 만든 후에 모델을 학습시킨다.

모델 평가는 torchtext.data.metrics에 있는 bleu_score로 계산한다. (추후 추가)

### Colab 환경

torch 1.8.1+cu101            
torchtext 0.6.0         
torchvision 0.9.1+cu101

# selenium
"관심있는 이미지"에 대한 검색을 하고 검색한 이미지를 수집하는 코드입니다. 
