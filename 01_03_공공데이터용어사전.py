
#08_tk_dict01A.py에서 파일 읽어와서 단어의 뜻을 확인하기
#Graphic User Interface -- GUI : 우리가 만들고 있는 것

# <<grid Parameter>>
# row, column : 해당 구역으로 위젯을 이동시킵니다.
# rowspan, columnspan : 현재 배치된 구역에서 위치를 조정합니다.
# sticky : 현재 배치된 구역 안에서 특정 위치로 이동시킵니다.
# sticky : 할당된 공간 내에서의 위치 조정	-	n, e, s, w, nw, ne, sw, se

# tkinter 모듈 설명 깃허브 : https://076923.github.io/posts/#Python-Tkinter

from tkinter import * #tkinter 의 전체 모듈을 불러온다. #plot라고 써도 됨
#import tkinter #tkinter.plot 이라고 써야 함

import pandas as pd
import os
global dat

print(os.getcwd())
# 폴더를 만들고, 삭제... 현재 폴더 위치
# 폴더와 디렉토리의 차이?
# 같은 의미임 리녹스 또는 맥에서만 폴더를 디렉토리라고 하고, 윈도우에서는 폴더라고 한다. 디렉토리 = 폴더
#global dat
dat = pd.read_excel("./공공데이터용어사전.xlsx")
print(dat.columns)

def click():
    print("버튼이 클릭되었습니다.")
    word = entry.get()
    output1.delete(0.0, END)
    output2.delete(0.0, END)
    try :
        def_word1 = dat.loc[dat['용어'] ==word, '용어설명'].values[0]
        def_word2 = dat.loc[dat['순번'] ==word, '용어'].values[0]
    except:
        def_word1 = "단어 뜻을 찾을 수 없습니다."
        def_word2 = "단어 뜻을 찾을 수 없습니다."
        # dat = window_add(dat)
    output1.insert(END, def_word1)
    output2.insert(END, def_word2)
print(os.getcwd()) # get current working directory -- 이 프로그램이 작업하고 있는 위치 확인

# 기능 추가
# 제출 버튼을 클릭했을 때, 동작 기능

window = Tk()
window.title("공공데이터 용어사전 검색창")

# 01 입력 상자 설명 레이블
label = Label(window, text="원하는 단어 입력 후, 엔터 키 누르기")
label.grid(row=0, column=0, sticky=W)

# 02 텍스트 입력이 가능한 상자(Entry)
entry = Entry(window, width=15, bg="light blue")
entry.grid(row=1, column=0, sticky=W)

# 03 제출 버튼 추가
btn = Button(window, text="제출", width=5, command=click)
btn.grid(row=2, column=0, sticky=W) #sticky가 위치

# 04 설명 레이블 - 의미 : 제출 버튼을 누르고 어떤 큰 상자가 나와서 의미 라는게 들어갈 거임
label2 = Label(window, text="\n결과 : ")
label2.grid(row=3, column=0, sticky=W)

# 05 텍스트 박스 입력 상자
# WORD ? https://www.geeksforgeeks.org/how-to-wrap-text-within-tkinter-text-box/
# columnspan=2 는 (4,0)~(4,1) 위치까지 분포
output1 = Text(window, width=50, height=6, wrap=WORD, background="light blue")
output1.grid(row=4, column=0, columnspan=2, sticky=W)
output2 = Text(window, width=50, height=6, wrap=WORD, background="light blue")
output2.grid(row=4, column=0, columnspan=2, sticky=W)
#메인 반복문 실행
window.mainloop()
