from tkinter import Tk, Label, Entry, Button, messagebox
import cart_page as cart_page

def login():
    user_id = input_id.get()
    user_pw = input_pw.get()

    if user_id == '20001234' and user_pw == '1234':
        cart_page.open_cart_page(window)
    else:
        messagebox.showerror("로그인 오류", "아이디 또는 비밀번호를 다시 확인해주세요.")

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
