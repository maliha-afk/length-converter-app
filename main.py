from tkinter import *

screen=Tk()
screen.title("Language Translator App")
screen.config(bg="burlywood")
screen.geometry("720x480")

Label(screen,text="Welcome To Length Converter",font=("alice",15,"bold"),fg="black",bg="burlywood").place(x=230,y=3)

Label(screen,text="please enter your length(in inches):",font=("alice",20,"bold"),fg="black",bg="burlywood").place(x=10,y=50)

len_e=Entry(screen,font=("alice",15,"bold"),fg="black",bg="white",width="20").place(x=480,y=55)


def convert():
    cm_count=int(len_e.get())

    result=(cm_count*2.54)
    my_result.config(text=f"your length(in inches) is: {cm_count} \n length into cm is:{result} ")


convertb=Button(screen,text="Convert",font=("alice",15,"bold"),fg="black",command=convert).place(x=10,y=120)
my_result=Label(screen,font=("Alice",10,"bold"),fg="black",bg="burlywood").place(x=-10,y=120)


def refresh():
    my_result.config(text="")



restartb=Button(screen,text="Reset",font=("alice",15,"bold"),fg="black",command=convert).place(x=10,y=180)


screen.mainloop()
