```python
from selenium import webdriver
driver = webdriver.Chrome('/Users/kime/Desktop/chromedriver')
driver
```




    <selenium.webdriver.chrome.webdriver.WebDriver (session="0af3e314029ec1c0ab36b5295801634b")>




```python
### url : http://ldjwj.github.io/00_SBA01_BigData/05_HTML/idx_lec_list
### 통계기본(xpath) : /html/body/div/div/div/div/div[9]/div[4]/a
### [selenium 객체].click()  :  다른페이지로 이동
```


```python
url = 'https://ldjwj.github.io/00_SBA01_BigData/05_HTML/idx_lec_list'
driver.get(url)
```


```python
sel_link1 = driver.find_element_by_xpath('/html/body/div/div/div/div/div[13]/div[4]/a')
sel_link1

```




    <selenium.webdriver.remote.webelement.WebElement (session="0af3e314029ec1c0ab36b5295801634b", element="9aa8301d-f9ac-4588-aade-8f74dac0681d")>




```python

sel_link1.text
```




    'Link'




```python
sel_link1.tag_name
```




    'a'




```python
sel_link2 = driver.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div[3]')
sel_link2
```




    <selenium.webdriver.remote.webelement.WebElement (session="0af3e314029ec1c0ab36b5295801634b", element="e597d781-32f7-416e-8252-fee940de8e54")>




```python
sel_link2.tag_name
```




    'div'




```python
url = 'https://pythonstart.github.io/web/'
driver.get(url)
```


```python
sel_id = driver.find_element_by_id("rank")
print(sel_id.text)
print(sel_id.tag_name)
```

    10. 랭킹 정보 가져오기(웹 크롤링)
    a


## 태그 이름으로 가져오기


```python
sel_a_all = driver.find_elements_by_tag_name("a")

for one in sel_a_all:
    print(one.tag_name, one.text)
```

    a 01. 제목 가져오기(title)
    a 02. 텍스트 가져오기(p)
    a 03. 링크 가져오기(a)
    a 04. 이미지 정보 가져오기(img)
    a 05. 리스트 정보 가져오기(ul,ol)
    a 06. id를 활용한 정보 획득
    a 07. class를 활용한 정보 획득
    a 08. 하나의 이미지 다운로드
    a 09. 여러개의 이미지 다운로드
    a 10. 랭킹 정보 가져오기(웹 크롤링)


## link_text로 가져오기


```python
sel_link = driver.find_element_by_link_text("01. 제목 가져오기(title)")
print(sel_link.tag_name, sel_link.text)
```

    a 01. 제목 가져오기(title)



```python
sel_link.get_attribute("href")
```




    'https://pythonstart.github.io/web/01.html'



## name 속성으로 가져오기


```python
sel_names = driver.find_elements_by_name("link_get")
sel_names
for i in sel_names:
    print(i.tag_name, i.text)
```

## selector를 이용한 접근


```python
sel_css = driver.find_elements_by_css_selector("body ul a")
for one in sel_css:
    print(one.tag_name, one.text)
```

    a 01. 제목 가져오기(title)
    a 02. 텍스트 가져오기(p)
    a 03. 링크 가져오기(a)
    a 04. 이미지 정보 가져오기(img)
    a 05. 리스트 정보 가져오기(ul,ol)
    a 06. id를 활용한 정보 획득
    a 07. class를 활용한 정보 획득
    a 08. 하나의 이미지 다운로드
    a 09. 여러개의 이미지 다운로드
    a 10. 랭킹 정보 가져오기(웹 크롤링)


## 링크의 내용 일부 내용으로 가져오기


```python
sel_p_link = driver.find_elements_by_partial_link_text("가져오기")
for one in sel_p_link:
    print(one.tag_name, one.text)
```

    a 01. 제목 가져오기(title)
    a 02. 텍스트 가져오기(p)
    a 03. 링크 가져오기(a)
    a 04. 이미지 정보 가져오기(img)
    a 05. 리스트 정보 가져오기(ul,ol)
    a 10. 랭킹 정보 가져오기(웹 크롤링)



```python
url = 'https://ldjwj.github.io/00_SBA01_BigData/05_HTML/idx_lec_list'
driver.get(url)
```


```python
content = driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div[3]')
content


```




    <selenium.webdriver.remote.webelement.WebElement (session="0af3e314029ec1c0ab36b5295801634b", element="4526735b-a750-4453-bc4b-5e9245a7ba18")>


content_all = driver.find_elements_by_class_name("cell")
for one in content_all:
    print(one.text)

```python
#/html/body/div/div/div/div/div[2]/div[3]
#/html/body/div/div/div/div/div[3]/div[3]
#/html/body/div/div/div/div/div[4]/div[3]
```
sel_class = driver.find_elements_by_css_selector("div[data-title='Content']")
for one in sel_class:
    print(one.text)sel_link5 = driver.find_elements_by_xpath('/html/body/div/div/div/div/div/div[3]')
for i in sel_link5:
    print(i.text)sel_content = driver.find_elements_by_css_selector('body div div div div div div')
for one in range(6, len(sel_content), 4):
    print(sel_content[one].tag_name, sel_content[one].text)
# LINK
* /html/body/div/div/div/div/div[2]/div[4]/a
* /html/body/div/div/div/div/div[3]/div[4]/a
#내코드
sel_class_link = driver.find_elements_by_xpath('/html/body/div/div/div/div/div/div[4]/a')
for i in sel_class_link:
    print(i.text, i.get_attribute("href"))#답안코드1
sel_class = driver.find_elements_by_xpath('/html/body/div/div/div/div/div/div[3]')
sel_class_link = driver.find_elements_by_xpath('/html/body/div/div/div/div/div/div[4]/a')
for i in range(len(sel_class_link)):
    print(sel_class[i+1].text)
    print(sel_class_link[i].get_attribute("href"))# 답안코드2
def get_data_by_css(css_name):
    return driver.find_elements_by_css_selector(css_name)
contents = get_data_by_css("div[data-title='Content']")
links = get_data_by_css("div[data-title='Link'] a")
for idx in range(len(contents)):
    print(contents[idx].text)
    print(links[idx].get_attribute("href"))

```python
import os
import pandas as pd

url = 'https://ldjwj.github.io/00_SBA01_BigData/05_HTML/idx_lec_list'
driver.get(url)
sel_link1 = driver.find_elements_by_xpath('/html/body/div/div/div/div/div/div[3]')
sel_link2 = driver.find_elements_by_xpath('/html/body/div/div/div/div/div/div[3]')
sel_link3 = driver.find_elements_by_xpath('/html/body/div/div/div/div/div/div[3]')
sel_link4 = driver.find_elements_by_xpath('/html/body/div/div/div/div/div/div[4]/a')

Cat=[]
Lcode=[]
Cont=[]
Link=[]

for i in range(len(sel_link4)):
    print("Category: "+sel_link1[i+1].text+" LeacturCode: "+sel_link2[i+1].text+" Contents: "+sel_link3[i+1].text+" Link: "+ sel_link4[i].get_attribute("href"))
    Cat.append(sel_link1[i+1].text)
    Lcode.append(sel_link2[i+1].text)
    Cont.append(sel_link3[i+1].text)
    Link.append(sel_link4[i].get_attribute("href"))
dat = { 'Category':Cat,'LeacturCode':Lcode ,'Contents':Cont, 'Link':Link }
dat = pd.DataFrame(dat)

dat.to_excel("selegram.xlsx", index=False)
dat
```

    Category: R 기본 전체(전 수업 링크) LeacturCode: R 기본 전체(전 수업 링크) Contents: R 기본 전체(전 수업 링크) Link: https://github.com/LDJWJ/RBasic/tree/master/01_RClass
    Category: 통계기본이해하기(1) LeacturCode: 통계기본이해하기(1) Contents: 통계기본이해하기(1) Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/Stat01_01_Basic_Summary_v12.pdf
    Category: 가설검정이해(1) LeacturCode: 가설검정이해(1) Contents: 가설검정이해(1) Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/Stat01_02_Hypo_v10.pdf
    Category: 통계기본이해_실습(1)-통계가설검정 LeacturCode: 통계기본이해_실습(1)-통계가설검정 Contents: 통계기본이해_실습(1)-통계가설검정 Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/stat01_Lab02_ttest_v11.html
    Category: 통계기본이해_실습(1)-통계가설검정 LeacturCode: 통계기본이해_실습(1)-통계가설검정 Contents: 통계기본이해_실습(1)-통계가설검정 Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/stat01_Lab02_v10.html
    Category: 회귀분석이해(1) LeacturCode: 회귀분석이해(1) Contents: 회귀분석이해(1) Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/Stat02_Regression_v10.pdf
    Category: 첫번째 모델 만들기 LeacturCode: 첫번째 모델 만들기 Contents: 첫번째 모델 만들기 Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/stat02_Lab01_lm_firstmodel.html
    Category: 회귀 모델 실습(1)-mtcars LeacturCode: 회귀 모델 실습(1)-mtcars Contents: 회귀 모델 실습(1)-mtcars Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/stat02_Lab02_lm_mtcars.html
    Category: 회귀 모델 실습(2)-Boston 집값 예측 LeacturCode: 회귀 모델 실습(2)-Boston 집값 예측 Contents: 회귀 모델 실습(2)-Boston 집값 예측 Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/stat02_Lab03_lm_housing.html
    Category: 회귀 모델 실습(3) - 캐글 데이터-집값 예측 LeacturCode: 회귀 모델 실습(3) - 캐글 데이터-집값 예측 Contents: 회귀 모델 실습(3) - 캐글 데이터-집값 예측 Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/stat02_Lab04_lm_house_adv.html
    Category: 로지스틱 회귀 모델 실습(1) - 인디언 암 예측 LeacturCode: 로지스틱 회귀 모델 실습(1) - 인디언 암 예측 Contents: 로지스틱 회귀 모델 실습(1) - 인디언 암 예측 Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/stat03_Lab05_logit_indian.html
    Category: 의사결정트리 기본 이해(1) LeacturCode: 의사결정트리 기본 이해(1) Contents: 의사결정트리 기본 이해(1) Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/stat04_decisiontree_v11.pdf
    Category: 의사결정트리 실습(1) LeacturCode: 의사결정트리 실습(1) Contents: 의사결정트리 실습(1) Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/stat04_Lab01_tree_titanic.html
    Category: 의사결정트리 실습(2) LeacturCode: 의사결정트리 실습(2) Contents: 의사결정트리 실습(2) Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/stat04_Lab02_tree_titanic.html
    Category: 데이터 탐색 - Boston 집값 LeacturCode: 데이터 탐색 - Boston 집값 Contents: 데이터 탐색 - Boston 집값 Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/stat02_Lab03_eda_housing.html
    Category: 텍스트 마이닝 시작하기 LeacturCode: 텍스트 마이닝 시작하기 Contents: 텍스트 마이닝 시작하기 Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/R_LV_Up08_TextMining.html
    Category: KoNLP를 패키지를 활용한 텍스트 분석(1) LeacturCode: KoNLP를 패키지를 활용한 텍스트 분석(1) Contents: KoNLP를 패키지를 활용한 텍스트 분석(1) Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/TM_Lab01_KoNLP.html
    Category: 텍스트 감정 분석(1) LeacturCode: 텍스트 감정 분석(1) Contents: 텍스트 감정 분석(1) Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/TM_LAB06_sentiment.html
    Category: TFIDF 이해하기(1) LeacturCode: TFIDF 이해하기(1) Contents: TFIDF 이해하기(1) Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/TM_Lab02_tfidf01.html
    Category: R과 MySQL 연동 환경 만들기 LeacturCode: R과 MySQL 연동 환경 만들기 Contents: R과 MySQL 연동 환경 만들기 Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/R_MYSQL_01_1909.pdf
    Category: R과 MySQL 연동 실습하기 LeacturCode: R과 MySQL 연동 실습하기 Contents: R과 MySQL 연동 실습하기 Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/R_LV_Up_MySQL01.html
    Category: 데이터 시각화 기본(1) LeacturCode: 데이터 시각화 기본(1) Contents: 데이터 시각화 기본(1) Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/B01_dataVis0418.pdf
    Category: 데이터 시각화 기본(2) LeacturCode: 데이터 시각화 기본(2) Contents: 데이터 시각화 기본(2) Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/B01_plot_basic.pdf
    Category: 데이터 시각화 기본(3) LeacturCode: 데이터 시각화 기본(3) Contents: 데이터 시각화 기본(3) Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/B02_ggplot2_jitter.pdf
    Category: 데이터 시각화 기본(4) LeacturCode: 데이터 시각화 기본(4) Contents: 데이터 시각화 기본(4) Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/B03_ggplot2_custom.pdf
    Category: 데이터 시각화 활용(5) LeacturCode: 데이터 시각화 활용(5) Contents: 데이터 시각화 활용(5) Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/DataVis_R_Lab07_networkAna01.r
    Category: 데이터 시각화 참고자료(1) LeacturCode: 데이터 시각화 참고자료(1) Contents: 데이터 시각화 참고자료(1) Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/G01_Graph_0601.r
    Category: 데이터 시각화 참고자료(2) LeacturCode: 데이터 시각화 참고자료(2) Contents: 데이터 시각화 참고자료(2) Link: https://ldjwj.github.io/00_SBA01_BigData/05_HTML/01_RClass/G02_Graph_0601.r





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Category</th>
      <th>LeacturCode</th>
      <th>Contents</th>
      <th>Link</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>R 기본 전체(전 수업 링크)</td>
      <td>R 기본 전체(전 수업 링크)</td>
      <td>R 기본 전체(전 수업 링크)</td>
      <td>https://github.com/LDJWJ/RBasic/tree/master/01...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>통계기본이해하기(1)</td>
      <td>통계기본이해하기(1)</td>
      <td>통계기본이해하기(1)</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>가설검정이해(1)</td>
      <td>가설검정이해(1)</td>
      <td>가설검정이해(1)</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>통계기본이해_실습(1)-통계가설검정</td>
      <td>통계기본이해_실습(1)-통계가설검정</td>
      <td>통계기본이해_실습(1)-통계가설검정</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>통계기본이해_실습(1)-통계가설검정</td>
      <td>통계기본이해_실습(1)-통계가설검정</td>
      <td>통계기본이해_실습(1)-통계가설검정</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>회귀분석이해(1)</td>
      <td>회귀분석이해(1)</td>
      <td>회귀분석이해(1)</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>첫번째 모델 만들기</td>
      <td>첫번째 모델 만들기</td>
      <td>첫번째 모델 만들기</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>회귀 모델 실습(1)-mtcars</td>
      <td>회귀 모델 실습(1)-mtcars</td>
      <td>회귀 모델 실습(1)-mtcars</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>회귀 모델 실습(2)-Boston 집값 예측</td>
      <td>회귀 모델 실습(2)-Boston 집값 예측</td>
      <td>회귀 모델 실습(2)-Boston 집값 예측</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>회귀 모델 실습(3) - 캐글 데이터-집값 예측</td>
      <td>회귀 모델 실습(3) - 캐글 데이터-집값 예측</td>
      <td>회귀 모델 실습(3) - 캐글 데이터-집값 예측</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>로지스틱 회귀 모델 실습(1) - 인디언 암 예측</td>
      <td>로지스틱 회귀 모델 실습(1) - 인디언 암 예측</td>
      <td>로지스틱 회귀 모델 실습(1) - 인디언 암 예측</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>의사결정트리 기본 이해(1)</td>
      <td>의사결정트리 기본 이해(1)</td>
      <td>의사결정트리 기본 이해(1)</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>의사결정트리 실습(1)</td>
      <td>의사결정트리 실습(1)</td>
      <td>의사결정트리 실습(1)</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>의사결정트리 실습(2)</td>
      <td>의사결정트리 실습(2)</td>
      <td>의사결정트리 실습(2)</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>데이터 탐색 - Boston 집값</td>
      <td>데이터 탐색 - Boston 집값</td>
      <td>데이터 탐색 - Boston 집값</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
    <tr>
      <th>15</th>
      <td>텍스트 마이닝 시작하기</td>
      <td>텍스트 마이닝 시작하기</td>
      <td>텍스트 마이닝 시작하기</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>KoNLP를 패키지를 활용한 텍스트 분석(1)</td>
      <td>KoNLP를 패키지를 활용한 텍스트 분석(1)</td>
      <td>KoNLP를 패키지를 활용한 텍스트 분석(1)</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
    <tr>
      <th>17</th>
      <td>텍스트 감정 분석(1)</td>
      <td>텍스트 감정 분석(1)</td>
      <td>텍스트 감정 분석(1)</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>TFIDF 이해하기(1)</td>
      <td>TFIDF 이해하기(1)</td>
      <td>TFIDF 이해하기(1)</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
    <tr>
      <th>19</th>
      <td>R과 MySQL 연동 환경 만들기</td>
      <td>R과 MySQL 연동 환경 만들기</td>
      <td>R과 MySQL 연동 환경 만들기</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>R과 MySQL 연동 실습하기</td>
      <td>R과 MySQL 연동 실습하기</td>
      <td>R과 MySQL 연동 실습하기</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
    <tr>
      <th>21</th>
      <td>데이터 시각화 기본(1)</td>
      <td>데이터 시각화 기본(1)</td>
      <td>데이터 시각화 기본(1)</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
    <tr>
      <th>22</th>
      <td>데이터 시각화 기본(2)</td>
      <td>데이터 시각화 기본(2)</td>
      <td>데이터 시각화 기본(2)</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>데이터 시각화 기본(3)</td>
      <td>데이터 시각화 기본(3)</td>
      <td>데이터 시각화 기본(3)</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
    <tr>
      <th>24</th>
      <td>데이터 시각화 기본(4)</td>
      <td>데이터 시각화 기본(4)</td>
      <td>데이터 시각화 기본(4)</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
    <tr>
      <th>25</th>
      <td>데이터 시각화 활용(5)</td>
      <td>데이터 시각화 활용(5)</td>
      <td>데이터 시각화 활용(5)</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
    <tr>
      <th>26</th>
      <td>데이터 시각화 참고자료(1)</td>
      <td>데이터 시각화 참고자료(1)</td>
      <td>데이터 시각화 참고자료(1)</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
    <tr>
      <th>27</th>
      <td>데이터 시각화 참고자료(2)</td>
      <td>데이터 시각화 참고자료(2)</td>
      <td>데이터 시각화 참고자료(2)</td>
      <td>https://ldjwj.github.io/00_SBA01_BigData/05_HT...</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
