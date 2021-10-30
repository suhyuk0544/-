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

#for o in range(len(i)):
                #label1 = Label(root, text=i[o], justify='right')
                #label1.pack
                #print(i[o])
#insert into stdtbl value('김범수','경남'),('성시경','서울'),('조용필','경기'),('은지원','경북'),('바비킴','서울');
#insert into clubtbl value('수영','101호'),('바둑','102호'),('축구','103호'),('봉사','104호');
#insert into stdclubtbl value(null,'김범수','바둑'),(null,'김범수','축구'),(null,'조용필','축구'),(null,'은지원','축구'),(null,'은지원','봉사'),(null,'바비킴','봉사');

