from tkinter import *
from tkinter import messagebox
import csv
import look_detail
import final_page as final_page
import random

list_market = []    #수강 꾸러미 목록
member_final = []   #수강생 수
major = ["디지털소프트웨어공학부", "데이터사이언스전공"]    # 1전공 2전공
major_cnt = {"디지털소프트웨어공학부": 0, 
            "데이터사이언스전공": 0}   # 장바구니에 담긴 전공별 과목 개수

def open_cart_page():
    window2 = Tk() 
    window2.title("장바구니")
    window2.geometry('500x600+10+10')
    lb2 = Listbox(window2, width=60)        #lb2 : 장바구니 목록 출력

    courseFile = open("courseList.csv", encoding="UTF-8")
    courseData = csv.reader(courseFile) # 전공 / 과목명 / 과목코드 / 교수 / 분반
    courses = list(courseData)
    courseFile.close()

    member = [random.randint(1,20) for _ in range(len(courses))]  # 각 과목별 수강생 수(랜덤)

    def lookup(list):     #리스트 확인
        for course in list:
            lb2.insert(END, course)

    def btnpress():     # 입력창의 내용을 리스트 박스 마지막에 추가
        num = lb2.curselection() 
        num = int(num[0])
        selected_major = courses[num][0]
        if selected_major in major:
            if len(list_market) < 4:
                if major_cnt[selected_major] < 2:
                    lb.insert(END, courses[num]) 
                    list_market.append(courses[num])
                    member_final.append(member[num])
                    major_cnt[selected_major] += 1
                    lb2.delete(num)
                    del courses[num]
                    del member[num]
                else:
                    messagebox.showerror("개수 초과", "전공별 최대 과목 수인 2개를 초과했습니다.")
            else:
                messagebox.showerror("개수 초과", "장바구니 최대 과목 수인 4개를 초과했습니다.")
        else:
            messagebox.showerror("전공 불일치", "전공이 아닙니다.")
        
    def btnpress1():              # 리스트 박스 중 선택된 값 삭제  
        num = lb.curselection() 
        num = int(num[0])
        selected_major = list_market[num][0]
        major_cnt[selected_major] -= 1
        lb2.insert(END,list_market[num])
        courses.append(list_market[num])
        member.append(member_final[num])
        list_market.remove(list_market[num])
        member_final.remove(member_final[num])
        lb.delete(lb.curselection())  # 리스트 박스 중 선택된 값 삭제

    def complete():     
        global newWindow, new_lbox , finish_label     # 새 창 띄우기, 최종 과목명 출력 리스트박스
        newWindow = Toplevel()
        newWindow.title("(최종) 수강 꾸러미 목록")
        newWindow.geometry("500x600+10+10")
        final_page.real_final(newWindow, member_final, list_market)

        newWindow.mainloop()

    def detail(event):
        num = lb.curselection()
        if num:
            num=int(num[0])
            global detailWindow #, finish_lbox       # 새 창 띄우기, 최종 과목명 출력 리스트박스(이거 고치면 됨-임시)
            detailWindow = Toplevel()
            
            detailWindow.geometry("700x600+10+10")
            look_detail.PieChart(list_market[num], member_final[num])
            detailWindow.title('수강내역 상세보기')
        
    def realCheck():        # 확정을 물어보는 메세지박스
        str = messagebox.askyesno('확인', "확정 지으시겠습니까?")
        if str == True:
            complete()      # 새 창을 띄우는 함수로 넘어감

    lb1 = Label(window2, text="장바구니", command=lookup(courses))     #lb1 : 장바구니
    lb1.pack(side=TOP, padx=10, pady=10)

    lb2.config(selectmode="single")         #lb2 : 장바구니 목록 출력
    lb2.config(height=10)
    lb2.pack(padx=10)

    btn = Button(window2)                
    btn.config(text= "수강 꾸러미에 추가")          # 버튼 내용 
    btn.config(width=15)              # 버튼 크기
    btn.config(command=btnpress)      # 버튼 기능 (btnpree() 함수 호출)
    btn.pack(pady=5)                        # 버튼 배치

    lb3 = Label(window2, text="수강 꾸러미")
    lb3.pack(padx=10, pady=5)

    lb = Listbox(window2, width=60)             # 수강꾸러미 리스트 생성        #lb: 수강꾸러미 리스트
    lb.config(selectmode="single")    # 리스트 박스 selectmode 설정
    lb.config(height = 6)             # 리스트 박스 높이 설정
    lb.pack(padx=10, pady=5)                         # 리스트 박스 배치
        
    lb.bind('<Double-Button-1>', detail)            # 리스트 박스 데이터시각화  ####해당 값 더블클릭 시 데이터 시각화 페이지로 이동

    btn1 = Button(window2)                
    btn1.config(text= "삭제")          # 삭제 버튼
    btn1.config(width=10)              # 버튼 크기
    btn1.config(command=btnpress1)     # 버튼 기능 (btnpree1() 함수 호출)
    btn1.pack(pady=5)                        # 버튼 배치

    btn2 = Button(window2)      # 완료 버튼
    btn2.config(text="완료")
    btn2.config(width=10)
    btn2.config(command=realCheck)        #버튼 기능 (completet() 함수 호출)
    btn2.pack(pady=10)

    window2.mainloop()