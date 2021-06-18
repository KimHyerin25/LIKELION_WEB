```python
from bs4 import BeautifulSoup
from urllib.request import urlopen
```


```python
url = "http://movie.naver.com/movie/running/current.nhn"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')
```


```python
soup_ul_li = soup.find("ul", class_="lst_detail_t1").find_all("li")
len(soup_ul_li)
```




    130




```python
#영화제목
soup_ul_li[129].find("dt",class_="tit").a.text
```




    '오버드라이브'




```python
#평점
soup_ul_li[129].find("span", class_="num").text
```




    '5.35'




```python
#예매율
soup_ul_li[0].find("dl", class_="info_exp").span.text
```




    '19.64'




```python
#참여인원
soup_ul_li[0].find("em").text
```




    '4,634'




```python
#감독
soup_ul_li[0].find("dl", class_="info_txt1").findAll("dd")[1].text.strip()
```




    '크레이그 질레스피'




```python
soup_ul_li = soup.find('ul', class_='lst_detail_t1').find_all('li')


all_title = []
all_score = []
all_people = []
all_rate = []
all_director = []

for one in soup_ul_li:
    one_title = one.find('dt',class_='tit').a.text             # 제목
    one_score = one.find('span', class_='num').text    # 평점
    one_people = one.find('em').text                         # 참여인원
    one_director = one.find("dl", class_="info_txt1").findAll("dd")[1].text
    one_director = one_director.translate(  {ord('\n'):"", ord('\r'):"", ord('\t'):""} )
    
    tmp_rate = one.find("dl", class_="info_exp")
    if tmp_rate is not None:
        one_rate = one.find("dl", class_="info_exp").span.text
    else:
        one_rate = '0'
    
    
    all_title.append(one_title)
    all_score.append(one_score)
    all_people.append(one_people)
    all_rate.append(one_rate)
    all_director.append(one_director)
    
print(len(all_title), len(all_score), len(all_people), len(all_rate), all(all_director))
print(all_title)
print(all_score)
print(all_people)
print(all_rate)
print(all_director)
```

    130 130 130 130 True
    ['크루엘라', '콰이어트 플레이스 2', '루카', '컨저링 3: 악마가 시켰다', '극장판 귀멸의 칼날: 무한열차편', '여고괴담 여섯번째 이야기 : 모교', '캐시트럭', '분노의 질주: 더 얼티메이트', '뱅드림! 로젤리아 에피소드Ⅰ: 약속', '파이프라인', '아야와 마녀', '클라이밍', '그레타 툰베리', '그 여름, 가장 차가웠던', '노매드랜드', '야구소녀', '프로페서 앤 매드맨', '혼자 사는 사람들', '굴뚝마을의 푸펠', '애플', '500일의 썸머', '낫아웃', '썰', '인트로덕션', '레이니 데이 인 뉴욕', '까치발', '더 파더', '#위왓치유', '청춘 선거', '중경삼림', '극장판 콩순이: 장난감나라 대모험', '너의 이름은.', '포겟 미 낫-엄마에게 쓰는 편지', '사랑하고 사랑받고 차고 차이고', '크루즈 패밀리: 뉴 에이지', '학교 가는 길', '라이더스 오브 저스티스', '미나리', '화양연화', '명탐정 코난: 비색의 탄환', '강변호텔', '화이트 온 화이트', '도라에몽: 스탠바이미 2', '폭력의 그림자', '쿠사마 야요이: 무한의 세계', '날씨의 아이', '토토리! 우리 둘만의 여름', '언어의 정원', '어른들은 몰라요', '내겐 너무 소중한 너', '강호아녀', '마세티 킬즈', '빅 피쉬', '플래시백', '분노의 질주', '미스피츠', '스쿨 오브 락(樂)', '부활: 그 증거', '분노', '비커밍 아스트리드', '쿠오바디스, 아이다', '흐린 하늘에 웃다', '그을린 사랑', '노 게임 노 라이프 -제로-', '봉쇄수도원 카르투시오', '블루 재스민', '서칭 포 슈가맨', '아들의 이름으로', '억남', '가을 햇살', '간츠: 오', '구름의 저편, 약속의 장소', '그 여름 가장 조용한 바다', '그리고 삶은 계속된다', '꽁치의 맛', '나츠메 우인장: 세상과 연을 맺다', '날으는 해병대', '내 친구의 집은 어디인가', '내언니전지현과 나', '네가 내가 되었으면 좋겠다', '덕구', '도망친 여자', '동경의 황혼', '라스트 씬', '러브 라이브! 선샤인!! 더 스쿨 아이돌 무비 오버 더 레인보우', '러브 액츄얼리', '마스터', '무순, 세상을 가로질러', '문라이즈 킹덤', '미스터 노바디', '바람이 우리를 데려다 주리라', '버티고', '벙어리 삼룡', '별을 쫓는 아이', '소공녀', '소리에 놀라지 않는 사자처럼', '슈퍼노바', '실크 로드', '엔딩 노트', '여름날', '여호', '원더풀 라이프', '유스', '유전', '은혼', '은혼2: 규칙은 깨라고 있는 것', '이별의 아침에 약속의 꽃을 장식하자', '인디언 전사', '전야', '전주에서 길을 묻다', '좋은 빛, 좋은 공기', '찬실이는 복도 많지', '창문넘어 도망친 100세 노인', '천당의 밤과 안개', '체리 향기', '초여름', '타오르는 여인의 초상', '파도를 걷는 소년', '패터슨', '페이트 스테이 나이트 헤븐즈필 제1장 프레시지 플라워', '플로리다 프로젝트', '해피 투게더', '혼자', '화녀', '로슈포르의 숙녀들', '미스 사이공: 25주년 특별 공연', '바그다드 카페 : 디렉터스컷', '쉘부르의 우산', '신 테니스의 왕자 효테이 vs 릿카이 : 게임 오브 퓨처 후편', '오버드라이브']
    ['9.33', '8.56', '9.17', '6.69', '9.29', '4.98', '8.21', '7.64', '8.55', '7.06', '7.39', '7.06', '4.00', '8.50', '8.48', '8.13', '8.99', '8.77', '9.05', '7.85', '8.43', '8.75', '6.91', '8.00', '5.63', '8.86', '8.91', '9.05', '9.60', '8.93', '8.94', '8.79', '9.25', '8.56', '9.03', '9.59', '7.64', '7.67', '8.77', '8.93', '5.98', '7.54', '9.01', '0.00', '9.24', '7.95', '8.37', '8.17', '5.03', '9.04', '6.11', '6.80', '9.02', '6.00', '8.27', '3.58', '8.36', '9.30', '8.57', '7.60', '8.74', '1.00', '8.68', '7.26', '9.34', '8.51', '9.04', '6.48', '7.25', '7.61', '8.19', '6.93', '8.76', '8.39', '8.71', '9.27', '0.00', '9.12', '9.15', '7.76', '9.43', '6.79', '8.29', '7.11', '8.35', '8.93', '7.95', '8.40', '8.13', '8.25', '8.12', '6.27', '6.40', '7.92', '8.79', '9.17', '7.79', '8.06', '8.93', '8.89', '7.00', '8.01', '8.34', '7.23', '7.19', '8.35', '8.88', '5.00', '7.78', '8.00', '7.35', '8.76', '7.84', '8.08', '8.75', '7.88', '9.05', '6.97', '8.30', '7.11', '8.65', '9.20', '5.01', '8.25', '8.53', '9.21', '9.06', '8.78', '7.00', '5.35']
    ['4,634', '412', '88', '1,780', '12,386', '150', '553', '5,414', '47', '1,340', '135', '17', '10', '8', '567', '906', '87', '156', '113', '47', '4,502', '132', '55', '63', '696', '7', '331', '20', '5', '2,556', '159', '32,699', '8', '34', '426', '133', '108', '5,077', '1,874', '841', '406', '13', '234', '0', '17', '5,956', '19', '2,469', '890', '163', '19', '245', '3,134', '26', '566', '24', '11', '418', '1,295', '15', '23', '1', '984', '3,170', '74', '933', '801', '322', '4', '23', '472', '107', '248', '33', '86', '229', '0', '153', '179', '21', '2,638', '290', '17', '9', '344', '5,786', '669', '10', '657', '819', '24', '349', '5', '1,407', '2,824', '6', '48', '17', '177', '19', '1', '352', '1,006', '3,303', '486', '197', '1,387', '1', '87', '9', '48', '1,003', '1,832', '12', '142', '17', '1,787', '37', '1,208', '829', '1,805', '1,161', '99', '56', '19', '277', '929', '257', '2', '71']
    ['19.64', '16.63', '16.15', '7.27', '6.8', '6.4', '5.52', '3.38', '1.74', '1.55', '1.28', '1.26', '0.95', '0.76', '0.44', '0.42', '0.4', '0.36', '0.25', '0.23', '0.21', '0.21', '0.21', '0.19', '0.17', '0.15', '0.15', '0.13', '0.13', '0.11', '0.11', '0.11', '0.1', '0.1', '0.08', '0.08', '0.08', '0.06', '0.06', '0.06', '0.04', '0.04', '0.04', '0.04', '0.04', '0.04', '0.04', '0.02', '0.02', '0.02', '0.02', '0.02', '0.02', '0.02', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0.01', '0', '0', '0', '0', '0', '0']
    ['크레이그 질레스피', '존 크래신스키', '엔리코 카사로사', '마이클 차베즈', '소토자키 하루오', '이미영', '가이 리치', '저스틴 린', '코다이 카키모토', '유하', '미야자키 고로', '김혜미', '나탄 그로스만', '주순', '클로이 자오', '최윤태', 'P.B. 셰므란', '홍성은', '히로타 유스케', '크리스토스 니코우', '마크 웹', '이정곤', '황승재', '홍상수', '우디 앨런', '권우정', '플로리안 젤러', '바르보라 차르포바, 비트 클루삭', '민환기', '왕가위', '이선명', '신카이 마코토', '선희 엥겔스토프', '미키 타카히로', '조엘 크로포드', '김정인', '앤더스 토마스 옌센', '정이삭', '왕가위', '나가오카 치카', '홍상수', '테오 코트', '야기 류이치, 야마자키 다카시', '닉 로우랜드', '헤더 렌즈', '신카이 마코토', '아릴드 오스틴 아문센, 실리에 살로몬센', '신카이 마코토', '이환', '이창원, 권성모', '지아장커', '로버트 로드리게즈', '팀 버튼', '크리스토퍼 맥브라이드', '롭 코헨', '레니 할린', '강호준', '김상철', '이상일', '페르닐레 피셔 크리스텐센', '야스밀라 즈바니치', '모토히로 카츠유키', '드니 빌뇌브', '이시즈카 아츠코', '김동일', '우디 앨런', '말릭 벤젤룰', '이정국', '오오토모 케이시', '오즈 야스지로', '사이토 케이이치, 야스시  가와무라', '신카이 마코토', '기타노 다케시', '압바스 키아로스타미', '오즈 야스지로', '오오모리 타카히로, 이토 히데키', '니콜라스 레이', '압바스 키아로스타미', '박윤진', '김충길', '방수인', '홍상수', '오즈 야스지로', '박배일', '사카이 카즈오', '리차드 커티스', '폴 토마스 앤더슨', '남승석', '웨스 앤더슨', '자코 반 도마엘', '압바스 키아로스타미', '전계수', '나운규', '신카이 마코토', '전고운', '윤성준', '해리 맥퀸', '틸러 러셀', '마미 스나다', '오정석', '마이클 포웰, 에머릭 프레스버거', '고레에다 히로카즈', '파올로 소렌티노', '아리 에스터', '후쿠다 유이치', '후쿠다 유이치', '오카다 마리', '안드레 드 토스', '김상민', '진승현', '임흥순', '김초희', '플렉스 할그렌', '정성일', '압바스 키아로스타미', '오즈 야스지로', '셀린 시아마', '최창환', '짐 자무쉬', '스도 토모노리', '션 베이커', '왕가위', '박홍민', '김기영', '자크 데미', '브렛 설리반', '퍼시 애들론', '자크 데미', '카와구치 케이이치로', '안토니오 니그렛']


# 실습

* 개봉 예정영화 단락 하나 가져오기 (제목, 평점, 참여인원, 감독)
* 파일 만들고 github commit하기


```python
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://movie.naver.com/movie/running/premovie.nhn"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')

pre_soup = soup.find_all("ul",class_="lst_detail_t1")[2]
pre_title = pre_soup.find("img").get("alt")
print(len(pre_title))
```

    5



```python
all_title = []
pre_soup = soup.find_all("ul",class_="lst_detail_t1")
for a in pre_soup :
    all_title.append(a.find("img").get("alt"))

print(all_title)
```

    ['2046', '킬러의 보디가드 2', '흩어진 밤', '아사다 가족', '미드나이트', '기적', '매직아치', '블랙 위도우', '미션 임파서블: 루벤', '꽃다발 같은 사랑을 했다', '와인 패밀리', '극장판 짱구는 못말려: 격돌! 낙서왕국과 얼추 네 명의 용사들', '베놈 2: 렛 데어 비 카니지', '007 노 타임 투 다이', '웨스트 사이드 스토리', '모비우스', '쥬라기 월드: 도미니언', '미니언즈2']



```python

```


```python

```