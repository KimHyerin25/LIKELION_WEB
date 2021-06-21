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
data.to_excel("Amazon_applewatch.xlsx", index=False)
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
all_user = []
all_ratings=[]
all_dates=[]
all_help=[]
all_reviews=[]

for page in range(2,7,1):
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

    Username:  D.R. / rating :  4 / helpful : 0
    Review :  I didn’t buy this watch for the fitness features, I bought it for the convenience of not having to take my phone out of my pocket quite so often.  And because I have very small wrists for a grown woman, I got the 38mm GPS aluminum case version at the sub-$200 sale price.  Terrific bargain for that amount of money, especially knowing a new, feature-rich OS update is on the way!Among the things I love most about it is being able to make, take or reject a call quickly, the ability to talk to Siri just by raising the watch close to my mouth and I can scroll quickly between the watch faces I have created.  Also, I very much like the fact my Amazon music player shows up on the watch as soon as I open it on my phone.  I can pause and skip tracks quicker than I can with my headphones or earbuds.  And the knob raises or lowers the volume!  Nice!The big drawback: the face/font size.  Without my reading glasses, and even with the fonts as large and bold as they can go, I can’t see much.  To compensate, the faces I’ve created are very simple with one complication on each, such as temperature, step count, battery level, calculator, voice recorder, etc.  In other words, the ones I use most.  So instead of searching for these apps on the dock or in the layout, I can just swipe over to them as needed.  However, I look forward to being able to further customize faces (hopefully with bigger time/dates in the center instead of the corner) with the next OS coming out.To make my watch is battle-ready, I added a Zagg Invisible Shield Glass Curve Elite* and a snap-on Fintie bumper which fits well, even with the Zagg screen.  I tried the IQ Shield Screen Protector but I just couldn’t get the corners to stay down, even after two attempts.  Good thing the IQs are cheap!All in all, a worthwhile purchase for me.*Like many others, I had a problem with not being able to get rid of one or two bubbles under the Zagg screen protector.  I followed their application directions to a T, but still, the bubbles!  GRRRRR.  And each time I lifted up the edge to reset the protector, dust and debris would find its way in.  Finally, I removed the protector and put it under the tap.  While the water was running, I *gently* ran my finger around the inside to clear away the dust.  Then I held it by the edges and shook away most of the excess water.  While it was still a little damp, I reapplied it to the watch.  After a little bit of fiddling, it finally settled—and NO BUBBLES!  I left the watch sit overnight and in the morning, still NO BUBBLES!  Is this the solution everyone is looking for?  Only time will tell, so I will update accordingly.
    
    
    Username:  James Sachsel  / rating :  4 / helpful : One person found this helpful
    Review :  I have had my Apple Watch 3 since it was first released. So I liked it well enough to purchase as a gift. The downsides that I have ran into and the reason I have taken a star.1. I can’t seem to figure out how to pick what music is on my watch. This stems from iTunes somewhat also. I have purchased albums and I cannot download the entire album. Or specific singles that I have purchased. This seams to be an Apple ecosystem flaw that unfortunately reflects poorly on all of the devices I purchase from Apple.2. Fragile! Just buy extra protection.3. If you travel overseas, keep in mind the watch is Country specific. You cannot get the cellular plan outside the US if you buy the US spec watch.Outside the above mentioned, I feel Apple does a good job highlighting the features. And like I said they are good enough for me to have gotten another as a gift and still wear mine.
    
    
    Username:  Fabio Martínez / rating :  5 / helpful : 8 people found this helpful
    Review :  Fue en regalo de cumpleaños de mi novia y le encanto, tuve varios problemas con este articulo y mi banco pero ya esas son cosas que se salen de las manos del vendedor.
    
    
    Username:  Matthew / rating :  4 / helpful : 0
    Review :  I deliberated on getting an Apple Watch for a long time. I found it unnecessary and I typically hate wearing watches. However, I am working on bettering many aspect is my physical health and decided to get one.I will start by saying that I love this thing. I opted for a series 3 because the price is significantly lower than more recent models. From what I can tell, battery life and screen size are the chief improvements in the new models.The good:The watch is super convenient for accessing the most used features of my phone, without the need to use my phone. I often don’t have pockets and keep my phone in a bag, so the ability to check messages and answer calls from the watch is great.I love that I can “ping” my phone. I misplace it at the house frequently. I only wish that, like the Find My IPhone app, the ping would sound until the phone is unlocked.The watch integrates with my health related apps perfectly. Anything I need to access quickly can be done; whether it be my activity and sleep trackers or my heart rate tracker. It seems to accurately track my steps, as my phone (in pocket) and watch are generally consistent within 100 steps for every thousand.The screen is easy to see. I don’t have great vision, but have no trouble reading anything.The not as good:The watch has a poor speaker output, when talking on the phone. I Understand that the intent is to use the airpod with this and I usually do, but there are times that I don’t wish to and I would like to be able to hear clearly.Photos require an entire album to be synced. I would love to simply be able to store photos of my choosing. This becomes a bit annoying, since the aspect ratio of the Apple Watch screen is 5:4, versus most photos being 2:3 or 3:4. In order to ensure they view properly, you must crop them in the phone. As a professional photographer, this is annoying to me.The battery life isn’t quite as good as I hoped. I presumed that I would get close to two full days from each charge. I get a little bit more than one day. I am not a heavy user, as much of what I do requires my phone. I get even less when using the AirPods.The music app should be able to play from the watch speakers. AirPods obviously will sound better, but sometimes, I just want to hear my music quietly while working and don’t care so much for quality. I don’t want to have to have my phone following me or put pods in every time.Lastly, the location sharing app, which shares the same icon as Find My IPhone is not super useful. There is no way that I can see that I can use this to find other devices of mine (MBP, my other iPhone, my iPad). From my phone, I can ping all of these devices. It should be easy to equip the Watch with the same capability to do so.In short, I still love this. The issues are minor and nowhere near enough to deter me, but these are things that should be addressed in updated models or the OS, if they have not been addressed already.
    
    
    Username:  Boddiegirl / rating :  5 / helpful : One person found this helpful
    Review :  Nice fitness tracker. Easy to accessorize. Good value.Not sure if it’s me and I just haven’t figured it out but, with my Fitbit I can track everything in the app without downloading additional apps. For example if I want to track my water intake I have to download an app, onto my Apple Watch.There are some nice features like texting and answering the phone. But I think those are available on Fitbit.Last I noticed my pace on the Apple is different from Fitbit. There’s about a 3 minute pace difference. That’s very significant 😩 Apple Watch has the slower pace.
    
    



```python

```
