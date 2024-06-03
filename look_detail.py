from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import cart_page


def PieChart(str, member):
    plt.rcParams['font.family'] = "Malgun Gothic"
    plt.rcParams['axes.unicode_minus']=False  ### 원형차트 한글 인코딩
    
    X = [member,10-member]
    labels=["수강꾸러미 신청인원", "수강꾸러미 남은인원"]
    explode = [0,0.1]
    colors = ["r","b"]
    
    list_title = str.split('/')
    #전 페이지에서 문자열 받아오기
    

    # 파이차트 그리기
    fig, ax = plt.subplots()
    ax.pie(X, labels=labels, explode=explode, colors=colors, autopct='%1.1d명', startangle=140)
    ax.axis('equal')  # 원형을 유지
    ax.set_title(list_title[0])  # 제목 설정
    
    # Matplotlib 그림을 Tkinter 창에 삽입
    canvas = FigureCanvasTkAgg(fig, master=cart_page.detailWindow)
    canvas.draw()
    canvas.get_tk_widget().pack()

    plt.plot(label="수강꾸러미 신청인원")
    plt.plot(label="수강꾸러미 남은인원")
    plt.legend()
    plt.title(list_title[0])


    
# graph = Tk()
# graph.geometry('500x600+10+10')
# graph.title("파이차트 예제")

# 파이차트 그리기
# PieChart()

# graph.mainloop()