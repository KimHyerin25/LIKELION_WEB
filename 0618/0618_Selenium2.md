```python
from selenium import webdriver
import time
import lxml

url = 'https://pythonstart.github.io/web/'
start = time.time()
driver = webdriver.Chrome('/Users/kime/Desktop/chromedriver')
driver.get(url)
```
a_tag = driver.find_elements_by_css_selector("ul a")
a_tag
### BeautifulSoup
### Selenium
01 Selenium 웹 페이지를 띄우고
02 해당 웹의 HTML소스를 얻어오기


```python
from bs4 import BeautifulSoup
```


```python
page = driver.page_source
soup = BeautifulSoup(page, 'lxml')
soup.title
```




    <title>나의 웹 페이지</title>



#### 웹페이지 URL : https://pythonstart.github.io/web/
* 실습1. BeautifulSoup를 이용해서 전체 링크 내용을 가져와 보자.
* 실습2. Selenium 함수를 이용해서 (find_element/elements...) 전체 링크를 가져와보자.


```python
##실습2 - 내코드
title = driver.find_element_by_tag_name("h1")
contents = driver.find_elements_by_tag_name("a")
print("<",title.text,">")
for one in contents:
    print(one.text, one.get_attribute("href"))
```

    < my web page >
    01. 제목 가져오기(title) https://pythonstart.github.io/web/01.html
    02. 텍스트 가져오기(p) https://pythonstart.github.io/web/02.html
    03. 링크 가져오기(a) https://pythonstart.github.io/web/03.html
    04. 이미지 정보 가져오기(img) https://pythonstart.github.io/web/04.html
    05. 리스트 정보 가져오기(ul,ol) https://pythonstart.github.io/web/05.html
    06. id를 활용한 정보 획득 https://pythonstart.github.io/web/06.html
    07. class를 활용한 정보 획득 https://pythonstart.github.io/web/07.html
    08. 하나의 이미지 다운로드 https://pythonstart.github.io/web/08.html
    09. 여러개의 이미지 다운로드 https://pythonstart.github.io/web/09.html
    10. 랭킹 정보 가져오기(웹 크롤링) https://pythonstart.github.io/web/10.html



```python
##실습1 - 내코드
soup.title.text
contents = soup.find("ul").findAll("a")
for one in contents:
    print(one.text, one.get("href"))
```

     01. 제목 가져오기(title)  ./01.html
     02. 텍스트 가져오기(p)  ./02.html
     03. 링크 가져오기(a)  ./03.html
     04. 이미지 정보 가져오기(img)  https://pythonstart.github.io/web/04.html
     05. 리스트 정보 가져오기(ul,ol)  ./05.html
     06. id를 활용한 정보 획득  ./06.html
     07. class를 활용한 정보 획득  ./07.html
     08. 하나의 이미지 다운로드  ./08.html
     09. 여러개의 이미지 다운로드  https://pythonstart.github.io/web/09.html
     10. 랭킹 정보 가져오기(웹 크롤링)  ./10.html


## 추가실습 
* 02번의 텍스트 가져오기
* 03번의 링크 가져오기 페이지의 내용을 가지고 오기


```python
## 02번 텍스트 가져오기
url = 'https://pythonstart.github.io/web/02.html'
driver = webdriver.Chrome('/Users/kime/Desktop/chromedriver')
driver.get(url)

num2_text = driver.find_elements_by_tag_name("p")
for one in num2_text:
    print(one.text)
```

    여기는 두번째 단계
    01 시작이 반이다
    02 포기하지말고 화이팅!
    03 응원합니다.



```python
## 03번 링크, 페이지내용 가져오기
url = 'https://pythonstart.github.io/web/03.html'
driver = webdriver.Chrome('/Users/kime/Desktop/chromedriver')
driver.get(url)

num3_link = driver.find_elements_by_tag_name("a")
for one in num3_link:
    print(one.text, " : ",one.get_attribute("href") )
```

    네이버  :  https://www.naver.com/
    구글  :  https://www.google.co.kr/
    마이크로 소프트  :  https://www.microsoft.com/ko-kr
    카카오  :  https://www.kakaocorp.com/



```python

```
