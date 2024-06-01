from tkinter import *
import tkinter.messagebox as msg

def login():
    user_id = input_id.get()
    user_pw = input_pw.get()

    if user_id == '20001234' and user_pw == '1234':
        open_cart_page()
    else:
        msg.showerror("로그인 오류", "아이디 또는 비밀번호를 다시 확인해주세요.")

def open_cart_page():
    window2 = Tk()
    window2.title("로그인 완료")
    window2.geometry("300x400")
    label = Label(window2, text="다음 페이지로 연결 or 새 창(아직 구현 X)")
    label.pack()

window = Tk()
window.title("로그인")
window.geometry("300x400")

label_id = Label(window, text="ID")
label_id.pack(pady=5)

input_id = Entry(window)
input_id.pack(pady=5)

label_pw = Label(window, text="Password")
label_pw.pack(pady=5)

input_pw = Entry(window, show="*")
input_pw.pack(pady=5)

login_button = Button(window, text="Login", command=login)
login_button.pack(pady=10)

window.mainloop()