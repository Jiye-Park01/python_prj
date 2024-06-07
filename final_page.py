from tkinter import *
import cart_page

def real_final(window, member_final, list_market, full_number=10):     
        #global new_lbox , finish_label, fail_label
        #full_number=50     # 새 창 띄우기, 최종 과목명 출력 리스트박스

        finish_label = Label(window, text='수강 꾸러미 확정 과목') #수꾸 확정 과목 리스트 라벨
        finish_label.pack(side=TOP, pady=10)
        new_lbox = Listbox(window, width=50) #수꾸 확정 과목 리스트
        new_lbox.config(selectmode="none")
        new_lbox.config(height=6)
        new_lbox.pack(padx=10, pady=5)

        fail_label=Label(window, text="초과 과목") #초과 과목 리스트 라벨
        fail_lbox = Listbox(window, width=50) #수꾸 확정 과목 리스트

        for i in range(len(member_final)):
            print(cart_page.member_final[i])
            if cart_page.member_final[i] <= full_number: 
                new_lbox.insert(END, list_market[i])
            else:
                fail_lbox.insert(END, list_market[i])

        fail_label.pack()
        
        fail_lbox.config(selectmode="none")
        fail_lbox.config(height=6)
        fail_lbox.pack(padx=10, pady=5)