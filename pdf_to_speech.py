
from tkinter import *
from tkinter import filedialog
from gtts import *
import pyttsx3
import PyPDF2
#import os

root = Tk()
root.geometry('350x350')

# label_page = Label(root, text="Starting Page Number").pack()
# start_page_number = Entry(root)
# start_page_number.pack()

label = Label(root, text="Which book you want to read?",font="arial 14").pack()


engine=pyttsx3.init()
def fileDialog():
    path = filedialog.askopenfilename()
    book = open(path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    
    
    for num in range(0,pages):
        page = pdfReader.getPage(num)
        txt = page.extractText()
        engine.say(txt)
        engine.runAndWait()




  



    


imageicon1=PhotoImage(file="pdfimg.Png")
Button(root, text="Choose Pdf",compound=LEFT,image=imageicon1,font="arial 14",command=fileDialog).pack()

# imageicon2=PhotoImage(file="save.png")
# btn=Button(root,text="Save Audio",compound=LEFT,image=imageicon2,font="arial 14 ",bg="green",command=saveAudio)
# btn.place(x=110,y=100)

root.mainloop()