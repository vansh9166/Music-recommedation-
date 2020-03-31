from tkinter import *
#def click():
window=Tk()
window.title("MUSIC RECOMMENDATION SYSTEM")
window.configure(background="white")
photo1=PhotoImage(file="/home/yaman/recommender_system-master/notebooks/photo.gif")
Label(window,image=photo1,bg="white").grid(row=0,column=0,sticky=W)
Label(window,text="ENTER ARTIST NAME",bg="white",fg="black",font="none 12 bold").grid(row=1,column=0,sticky=W)
textentry=Entry(window,width=20,bg="black")
textentry.grid(row=2, column=0, sticky=W)
#Button(window,text="SUBMIT",width=6,command=click).grid(row=3,column=0,sticky=W)
