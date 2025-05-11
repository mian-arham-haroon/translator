from tkinter import *
from tkinter import messagebox, ttk
import googletrans
from googletrans import Translator
import textblob

root = Tk()
root.title("Google Translator")
root.geometry("1080x400")
root.config(bg="white")

def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)

def translate_now():
    # global language
    # try:
    # if translate_now:

    text_ = text1.get(1.0, END)
    t1=Translator()  
    tran_text=t1.translate (text_,src=combo1.get(),dest=combo2.get())
    tran_text=tran_text.text

    text2.delete(1.0,END)
    text2.insert(END,tran_text)
    # else:
            # messagebox.showerror("Error", "Target language not found.")

        # c2 = combo1.get()
        # c3 = combo2.get()
        # if text_:
        #     # words = Translator(textblob.TextBlob(text_))
        #     lan = words.detect_language()
        #     lan_ = None
        #     for i, j in language.items():
        #         if j == c3:
        #             lan_ = i
        #     if lan_:
        #         words = words.translate(from_lang=lan, to=str(lan_))
        #         text2.delete(1.0, END)
        #         text2.insert(END, words)
                    
    # except Exception as e:
    #     messagebox.showerror("Translation Error", "Please try again")

# Icon (ensure correct file path)
try:
    image_icon = PhotoImage(file="google_Icon.png")
    root.iconphoto(False, image_icon)
except Exception as e:
    print(f"Icon image load error: {e}")

# Languages
language = googletrans.LANGUAGES
languageV = list(language.values())

combo1 = ttk.Combobox(root, values=languageV, font="Robota 14", state="r")
combo1.place(x=110, y=20)
combo1.set("ENGLISH")

label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

f = Frame(root, bg="Black", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

combo2 = ttk.Combobox(root, values=languageV, font="Robota 14", state="r")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")

label2 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

f1 = Frame(root, bg="Black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Translate button
translate = Button(root, text="Translate", font="Roboto 15 bold italic",
                   activebackground="purple", cursor="hand2", bd=5, bg='red', fg="white", command=translate_now)
translate.place(x=480, y=250)

label_change()
root.mainloop()
