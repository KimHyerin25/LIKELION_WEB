```python
import os
```


```python
os.getcwd()
```




    '/Users/kime'




```python
from selenium import webdriver
from bs4 import BeautifulSoup
```


```python
driver = webdriver.Chrome('/Users/kime/Desktop/chromedriver')
driver
```




    <selenium.webdriver.chrome.webdriver.WebDriver (session="a7292d97c6956bbe1b5e9fe46826dc8f")>




```python
url = 'https://www.amazon.com/Apple-Watch-GPS-42mm-Silver-Aluminium/dp/B07K3HG6T9/ref=sr_1_3?dchild=1&keywords=apple%2Bwatch&qid=1624253099&sr=8-3&th=1'
driver.get(url)
```


```python
sel_rate = driver.find_element_by_xpath('//*[@id="acrCustomerReviewText"]')
sel_rate.click()
```


```python
sel_review = driver.find_element_by_xpath('//*[@id="cr-pagination-footer-0"]/a')
sel_review.click()
```


```python
page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')
soup.title
```




    <title>Amazon.com: Customer reviews: Apple Watch Series 3 (GPS, 42mm) - Silver Aluminum Case with White Sport Band</title>




```python
all_r = soup.find_all("span", class_="a-size-base review-text review-text-content")
all_review = []
for one in all_r:
    tmp = one.text
    review = tmp.strip()
    all_review.append(review)
    
print("리뷰 개수 : ", len(all_review))
print(all_review[0], all_review[-1], sep="\n")
```

    리뷰 개수 :  10
    I am a Fitbit person. But I decided to slurge a little bit...... The only think that kept me from switching was that I had to charge the watch so much more. I originally had the Fitbit charge 2...... then I purchased the series 3 (42mm) and I love this watch but it was just far too big. So I am returning the 42mm and just received the 38mm and am much happier with the size. I wanted to really share the size difference. I love this watch so far... will review in the future.
    After getting the initial Apple Watch, I am so excited for the upgrade with the Series 3. After weighing the differences between the Series 3 and Series 4, I decided that this was not only cost effective but completely comparable to the Series 4. The newest model only has marginal differences such as an ECG meter and a slightly brighter screen, but in the era of negligible upgrades there really is no reason not to consider this model over the newer ones. Unless the Series 4 drops in price or even newer, future models has features like a selfie camera, why pay the price? Great for parents and students who want the power of a new Apple Watch without the price burden. Not a lower standard!



```python
import os, warnings
import re
warnings.filterwarnings(action='ignore')
import pandas as pd

all_r = soup.find_all("div", class_="a-section celwidget")

all_user = []
all_ratings=[]
all_dates=[]
all_help=[]
all_reviews=[]

for one in all_r:
    # 사용자
    user_one = one.find("span", class_="a-profile-name").text
    all_user.append(user_one)
    
    #평점
    rating_one = one.find("span", class_="a-icon-alt").text
    nums = re.findall("\d+", rating_one)[0]
    all_ratings.append(nums)
    
    #날짜
    date_one=one.find("span", class_="a-size-base a-color-secondary review-date")
    texts = date_one.text.split("on")
    data = texts[1].strip()
    all_dates.append(data)
    
    #몇 명에게 도움
    try : 
        help_one=one.find('span',class_='a-size-base a-color-tertiary cr-vote-text').text
    except :
        help_one='0'
    all_help.append(help_one)
    
        # 리뷰 추가
    review_one = one.find("span", class_="a-size-base review-text review-text-content")
    tmp = review_one.text
    review = tmp.strip()
    all_reviews.append(review)


# print(all_user)
# print(all_ratings)
# print(all_dates)
# print(all_help)
# print(all_reviews)

data = {"Username ": all_user, "Reviews":all_reviews, "Ratings": all_ratings, "Date":all_dates, "Helpful":all_help}
data = pd.DataFrame(data)
data.to_csv("Amazon_applewatch.csv", index=False)
data

```




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
      <th>Username</th>
      <th>Reviews</th>
      <th>Ratings</th>
      <th>Date</th>
      <th>Helpful</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Nick M</td>
      <td>Volume on watch was to low to use on phone. Ta...</td>
      <td>2</td>
      <td>September 25, 2019</td>
      <td>One person found this helpful</td>
    </tr>
    <tr>
      <th>1</th>
      <td>George Pytlik</td>
      <td>Replaced my wife’s old version 1 Apple Watch w...</td>
      <td>4</td>
      <td>December 21, 2020</td>
      <td>2 people found this helpful</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Jenni</td>
      <td>I decided to go with Series 3 because I had ne...</td>
      <td>4</td>
      <td>May 22, 2020</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>AirbusMark</td>
      <td>I bought this watch primarily to monitor my he...</td>
      <td>2</td>
      <td>November 17, 2020</td>
      <td>One person found this helpful</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Emily</td>
      <td>This is my fault. I thought it would be compat...</td>
      <td>5</td>
      <td>May 25, 2021</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>CraigV</td>
      <td>We have become an Apple product house (2 iPhon...</td>
      <td>5</td>
      <td>May 22, 2019</td>
      <td>3 people found this helpful</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Amazon Customer</td>
      <td>So I just got this today, came wrapped in new ...</td>
      <td>5</td>
      <td>January 4, 2021</td>
      <td>One person found this helpful</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Nikki</td>
      <td>Interesting watch. Not as much detail as the f...</td>
      <td>4</td>
      <td>January 18, 2019</td>
      <td>5 people found this helpful</td>
    </tr>
    <tr>
      <th>8</th>
      <td>misfitsailor</td>
      <td>Works reliably to make and answer calls.  No n...</td>
      <td>5</td>
      <td>April 5, 2021</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Boddiegirl</td>
      <td>Nice fitness tracker. Easy to accessorize. Goo...</td>
      <td>5</td>
      <td>October 4, 2020</td>
      <td>One person found this helpful</td>
    </tr>
  </tbody>
</table>
</div>




```python
import time

all_user = []
all_ratings=[]
all_dates=[]
all_help=[]
all_reviews=[]

for page in range(2,10,1):
    time.sleep(3)
    
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    all_r = soup.find_all("div", class_="a-section celwidget")
    
    for one in all_r:
        # 사용자
        user_one = one.find("span", class_="a-profile-name").text
        all_user.append(user_one)

        #평점
        rating_one = one.find("span", class_="a-icon-alt").text
        nums = re.findall("\d+", rating_one)[0]
        all_ratings.append(nums)

        #날짜
        date_one=one.find("span", class_="a-size-base a-color-secondary review-date")
        texts = date_one.text.split("on")
        data = texts[1].strip()
        all_dates.append(data)

        #몇 명에게 도움
        try : 
            help_one=one.find('span',class_='a-size-base a-color-tertiary cr-vote-text').text
        except :
            help_one='0'
        all_help.append(help_one)

            # 리뷰 추가
        review_one = one.find("span", class_="a-size-base review-text review-text-content")
        tmp = review_one.text
        review = tmp.strip()
        all_reviews.append(review)
        
    #확인
    print("Username: ", all_user[-1], "/", "rating : ", all_ratings[-1],"/", "helpful :", all_help[-1])
    print("Review : ", all_reviews[-1], end="\n\n\n")
    
    #다음 페이지 클릭
    sel_next = driver.find_element_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a')
    sel_next.click()
```

    Username:  WINC818 / rating :  1 / helpful : One person found this helpful
    Review :  I LOVE an Apple Watch, so much so that after 3 years mine died and I am buying a second.  For whatever reason I got a dud. They will not allow me to return it despite on the site it saying I can. I have been through 4 customer care reps and spent too much time "trouble shooting" this product as they will not allow you to return it without going through their reset process. I have been through 4 reps as it must be their break time but they just leave and assign you someone else and you have to START ALL OVER every time. I will buy from Apple, Costco, Target, you name it but NOT FROM AMAZON. I love Amazon, but this is not the product to buy from them. On the Apple Watch, you won't regret it. So convenient. So convenient that I found it hard to go the 2 days without one once mine died!!!  DOn't start with it if you don't want to be addicted and fall in love with it :)
    
    
    Username:  virgie / rating :  2 / helpful : 0
    Review :  I was told by someone on amazon that this watch would pair with my iPhone so I went ahead and bought it. Had to wait a week to receive it even though I paid for next day delivery. Then I tried pairing it with my phone and it wouldn’t work kept saying my iPhone needed to update so I tried to update my iPhone it said it was updated so I called Apple and they said No this watch wouldn’t pair up unless I brought it to a Apple store and let them down grade the watch ???????I have no Apple store local it’s a 2hr drive to the closes store.So now I have to snail mail my watch to Apple to get it to work with my iPhone.So BUYERS BEWARE don’t make the same mistake I made.
    
    
    Username:  Teresa Larson / rating :  5 / helpful : 3 people found this helpful
    Review :  Well after an hour of trying to get it to connect to my phone and failed time after time I called apple support and 3 hours later I find out the watch won’t update due to the watch having such an old version on software.Update they have pushed a software patch though love the product I just wish it would have worked right away when I took it out of the box
    
    
    Username:  Brandon / rating :  5 / helpful : 4 people found this helpful
    Review :  We bought this for my dad for Father’s Day, 3 days later the watch notified him that his resting heart rate was high (140 bpm).  He went to the emergency room and was eventually diagnosed with AFib and will have to control it with meds.  The watch may have prevented a stroke or saved his life.
    
    
    Username:  My 2 Cents / rating :  5 / helpful : 0
    Review :  I'm not a fan of Apple products. I only have an iPhone because my company mandates it. In general, I complain a lot about using it having had other devices (not just Android!) in the past. I must say though, the Apple watch really brings the overall experience up to above average. It is incredibly well integrated. All of the things you never thought you would need on your wrist and were fine on your phone are now things you can't believe you ever went without. If you're considering a $200-300 fitness / connected watch and you have an iPhone, consider the Apple Watch. It tracks fitness very well. The only thing it doesn't do well is sleep tracking. Alone, the watch and iPhone will only estimate when you went to bed and if it thinks you were asleep or not. It does not do quality of sleep. However, there are free apps for download that will do such analysis from the data that the watch can already collect.
    
    
    Username:  Mandy C / rating :  5 / helpful : One person found this helpful
    Review :  There is absolutely nothing negative about this watch. I used to collect watches and was drawn to those with altimeters, pedometers, tide charts, weather, etc. This does all that and more. You can text on the fly while your phone is nearby. You can answer and make calls. The activity app is amazing and works well when I bike, run or go for a fitness walk. It is also accurate on the treadmill. Battery life can go for 24 hours before recharging. This is Incredible technology and beautiful jewelry all in one. This is the ultimate watch. It is everything I dreamed of as a little girl. I now have about a dozen watches to sell on Ebay....
    
    
    Username:  Elizabeth Casanova / rating :  5 / helpful : 0
    Review :  I am a bit frugal when it comes to buying items like this. I have been wanting an apple watch for a while but put it off because I felt like it was an overindulgent expense. But I'm starting to walk every day and do more exercise. My steps are not correctly monitored on my phone so I began researching pedometers and workout watches. I saw that this apple 3 watch was significantly reduced. It seemed like a great price. So I took the plunge (also my phone and computer are apple and prefer this product). I'm so glad I got this watch. It monitors all activity including walking, standing and heart. I can connect to other people and it is a motivator to stay active. I also love that I can take calls and send texts on the watch, instead of having my phone out at work. It's also really nice looking. I love the way it looks. There are too many apps and functions to mention here. But I'm glad I got this watch.
    
    
    Username:  Michelle Miller / rating :  5 / helpful : 0
    Review :  Your browser does not support HTML5 video.
    
    
       Overall I’m happy with the watch. I’m still learning all the features. I haven’t figured out sleep tracking which if the watch does in fact have I would love to open up. I upgraded from a Fitbit to this and am missing the sleep tracking that my Fitbit gave me. Probably something I need to open or download so I will keep exploring for that.The battery life is pretty much for the day. I can get through about a day and a half.I just learned that I need to clear/clean the speakers after swimming which is an easy fix on the watch.Overall, I’m happy with it
    
    



```python

```
