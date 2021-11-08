from tkinter import *
from tkinter import messagebox
from random import *
from warnings import *
import itertools
root = Tk()
root.title('뽑기')
root.geometry('720x360')

def getTextInput():
    while True:
        try:
            result=textExample.get(1.0, END+"-1c") 
            result = int(result)
            result += 1
            i = range(1, result)
            i = list(i)
            shuffle(i)
            m= list(itertools.product(i,repeat=2))
            print(list(m))
            
           
            #결과 값
            
            window = Tk() 
            window.title('결과')
            window.geometry('720x360')
            
            row = 0
            column = 0
            
            for o in range(len(i)):
                column += 6
                if column == 0:
                    row +=  5
                label1 = Label(window, text=m[o])

                label1.grid(row=row,column=column)
            
            if column == result:
                break
        
        except: #에러 메세지
            messagebox.showerror("Error", "수를 다시 입력해 주십시오")
            break
        else:  
            break

textExample=Text(root, height=5) 
textExample.pack()
btnRead=Button(root, height=1, width=4, text="확인", command=getTextInput)

btnRead.pack()


def btncmd2():
    
    MsgBox = messagebox.askquestion ('종료','정말로 종료하시겠습니까?',icon = 'error')
    
    if MsgBox == 'yes':
       root.destroy()
    else:
        messagebox.showinfo('안녕', '')
        
btn2 = Button (root, text='종료',command=btncmd2)
btn2.pack()


root.mainloop()
