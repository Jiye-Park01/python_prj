from tkinter import *
from tkinter import messagebox

window2 = Tk()
window2.title("장바구니")
window2.geometry('400x600+10+10')

lb2 = Listbox(window2, width=60)        #lb2 : 장바구니 목록 출력

list1 = ["과목1", "과목2", "과목3", "과목4", "과목5", "과목6"]
list2 = ["0012", "0023", "0034", "0045", "0056", "0067"]
list3 = ["배주화", "이찬수", "유제혁", "이경미", "유견아", "유제혁"]
list4 = ["01", "02", "01", "03", "02", "01"]
list_final = [1,2,3,4,5,6]
for i in range(len(list1)):
    list_final[i] = list1[i] + " // 과목코드: " + list2[i] + " // 교수명: " + list3[i] + " [" + list4[i] + "]"


def lookup(list1):      #리스트 확인
    for i in range (len(list1)):
        lb2.insert(END, list_final[i])

# frame = Frame(window2)
# frame.pack(side=TOP)
lb1 = Label(window2, text="장바구니", command=lookup(list_final))     #lb1 : 장바구니

lb1.pack(side=TOP, padx=10, pady=10)


lb2.config(selectmode="single")         #lb2 : 장바구니 목록 출력
lb2.config(height=10)
lb2.pack(padx=10)

list_market = []            #수강 꾸러미 목록

def btnpress():     # 입력창의 내용을 리스트 박스 마지막에 추가
    num = lb2.curselection()   
    num = int(num[0])
    #print(lb2.curselection())          
    lb.insert(END, list_final[num]) 
    list_market.append(list_final[num])
    print(list_market)
    lb2.delete(lb2.curselection())
    list_final.remove(list_final[num])
    
def btnpress1():              # 리스트 박스 중 선택된 값 삭제  
    #lb.delete(lb.curselection())  
    #lb2.insert(END, list_market[int(lb.curselection()[0])])
    #print(lb.curselection())

    #print(lb.curselection())
    # lb2.insert(END, list_market[int(lb.curselection()[0])])
    # list_market.remove(list_market[int(lb.curselection()[0])])
    # lb.delete(lb.curselection())  # 리스트 박스 중 선택된 값 삭제
    # print(list_market)

    print(lb.curselection())
    lb2.insert(END, list_market[int(lb.curselection()[0])])
    list_final.append(list_market[int(lb.curselection()[0])])
    list_market.remove(list_market[int(lb.curselection()[0])])
    lb.delete(lb.curselection())  # 리스트 박스 중 선택된 값 삭제
    print(list_final)

def complete():     
    global newWindow, new_lbox       # 새 창 띄우기, 임시 리스트박스(이거 고치면 됨)
    newWindow = Toplevel()
    newWindow.title("수꾸 데이터 시각화")
    newWindow.geometry("500x600+10+10")
    ######################################### 다음 창에서는 여기부터
    new_lbox = Listbox(newWindow, width=50)
    new_lbox.config(selectmode="single")
    new_lbox.config(height=6)
    new_lbox.pack(padx=10, pady=5)
    for i in range (len(list_market)):      # for 문으로 수꾸 리스트 출력(임시)
        print(list_market[i])
        new_lbox.insert(END, list_market[i])
    #################################################여기까지 삭제하고 시작(list 형태로 넘겨줘야되는거: list_market)

    newWindow.mainloop()
    
def realCheck():        # 확정을 물어보는 메세지박스
    messagebox.askyesno('확인', "진짜 완료 됨??")
    complete()          # 새 창을 띄우는 함수로 넘어감

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
    
# ent = Entry(window2)                 # 입력창 생성
# ent.pack()                        # 입력창 배치


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