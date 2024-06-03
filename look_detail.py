from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import cart_page


def PieChart(stray, member):
    plt.rcParams['font.family'] = "Malgun Gothic"
    plt.rcParams['axes.unicode_minus']=False  ### 원형차트 한글 인코딩
    
    # X = [member,10-member]      
    # X_ = [10, 10]
    labels=["수강꾸러미 신청인원", "수강꾸러미 남은인원"]
    explode = [0.1,0]
    colors = ["red","blue"]
    
    list_title = stray.split('/')
    #전 페이지에서 문자열 받아오기
    
    if member <= 10:    #초과 인원 발생할 수 있게 수정
        # 수강인원이 10명 이하일 경우
        X = [member, 10 - member]
    else:
        # 수강인원이 10명을 초과하는 경우
        #member = str(member)
        #lb_ = Label(cart_page.detailWindow, text=("정원이 초과되었습니다.\n현재 신청 정원: " + member))
        #lb_.pack(cart_page.detailWindow)
        colors = ["yellow", "blue"]
        X = [10, 0]  # 10명 고정, 초과 인원으로 표시
        labels = ["정원이 초과되었습니다", "-"]

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