import json
from json import *
import sqlite3
import tkinter
from tkinter import *
from tkinter import messagebox

cnt=0
#####Functions
############SubmitF###############
def submit():
##########SUBMIT DONE###############
    def subdone():
        def backmenue2():
             win10.destroy()
             win3.destroy()
             win2.destroy()
             
        win10=tkinter.Toplevel(win)
        win10.geometry('450x250+430+225')
        win10.configure(bg="black",cursor='star')
        win10.resizable(False,False)
        
        sublbl11=tkinter.Label(win10,text='ACCOUNT SUBMITED SUCCESSFULLY!',font=('Times New Roman',15,'bold'),fg='pink',bg='black')
        sublbl11.place(x=45,y=50)
        
        btn12=tkinter.Button(win10,text='BACK TO MENUE',bg='pink',fg='black',font=('Times New Roman',15),height=0,width=17,activebackground='black',activeforeground='pink',command=backmenue2)
        btn12.place(x=130,y=120)
    
        win10.mainloop()
        
        
##########CREAT FILE###########
    def creat_file():
        win3=tkinter.Toplevel(win)
        win3.geometry('400x300+200+300')
        win3.configure(bg="black",cursor='star')
        win3.resizable(False,False)
        wlbl=tkinter.Label(win3,text='!FILE NOT FOUND!'+'/n'+'DO YOU WANT TO CREAT ONE?',font=('Times New Roman',30,'bold'),fg='pink',bg='black')
        sublbl.place(x=170,y=50)
        try:
            dct={'admin':'12345678'}
            with open('D:/passs.json','w') as j:
                json.dump(dct,j)
        except:
            pass
###########VALIDATION##########
    def validate():
        result=True
        username=user.get()
        password=pas.get()
        if(username=="" or password==""):
           sublbl3.configure(text="PLEASE FILL THE BLANKS",fg="red")
           result=False 
        elif(len(username)<5):
            sublbl3.configure(text="USERNAME MUST BE AT LEAST 5 CHARACTER",fg="red")
            result=False
        elif(len(password)<8):
            sublbl3.configure(text="PASSWORD MUST BE AT LEAST 8 CHARACTER",fg="red")
            result=False    
        elif(not(username.isalpha())):
            sublbl3.configure(text="INVALID CHARACTERS FOR USERNAME!",fg="red")
            result=False  
        else:
            try:
                with open('D:/passs.json') as f:
                    dct=json.load(f)
                if user in dct:
                    sublbl3.configure(text="USERNAME ALREADY EXIST",fg="red")
                    result=False
            except FileNotFoundError:
                creat_file()
        return result 
    
    
     
        win3.mainloop()
        
############ADDING TO JSON#########            
    def tojsonfiles():    
        username=user.get()
        password=pas.get()
        with open('D:/passs.json')as j:
            dct=json.load(j)
        dct[username]=password
        with open('D:/passs.json','w') as f:
            json.dump(dct,f)
        
        subdone()
          
            # r=messagebox.showinfo('submitdone','SUBMIT COMPLETED SUCCESSFULLY!',font=('Times New Roman',50,'bold'),fg='pink',bg='black')
            # if r==True:
            #     win2.destroy()
##########MAIN SUBMIT FUNCTION#########    
    def sub2():
        sublbl3.configure(text="")
        if validate():
            tojsonfiles()
#########DESTROYING KEY#################
    def back():
        win2.destroy()
        
    win2=tkinter.Toplevel(win)
    win2.geometry('850x650+225+45')
    win2.configure(bg="black",cursor='star')
    win2.resizable(False,False)
    
    sublbl=tkinter.Label(win2,text='*SUBMIT PAGE*',font=('Times New Roman',50,'bold'),fg='pink',bg='black')
    sublbl.place(x=170,y=50)

    user=Entry(win2,width=25,font=("Times New Roman",19),bg='pink',selectbackground='black',selectforeground='pink')
    user.place(x=280,y=200)
    sublbl2=tkinter.Label(win2,text='USERNAME',font=('Times New Roman',15,'bold'),fg='pink',bg='black')
    sublbl2.place(x=370,y=170)

    pas=Entry(win2,width=25,font=("Times New Roman",19),bg='pink',selectbackground='black',selectforeground='pink',show='*')
    pas.place(x=280,y=265)
    sublbl4=tkinter.Label(win2,text='PASSWORD',font=('Times New Roman',15,'bold'),fg='pink',bg='black')
    sublbl4.place(x=370,y=235)

    btn3=tkinter.Button(win2,text='SUBMIT',bg='pink',fg='black',font=('Times New Roman',20),height=0,width=10,activebackground='black',activeforeground='pink',command=sub2)
    btn3.place(x=350,y=330)

    btn4=tkinter.Button(win2,text='BACK',bg='pink',fg='black',font=('Times New Roman',15),height=0,width=7,activebackground='black',activeforeground='pink',command=back)
    btn4.place(x=387,y=400)
    
    sublbl3=tkinter.Label(win2,text='',font=('Times New Roman',13,'bold'),fg='pink',bg='black')
    sublbl3.place(x=320,y=450)
    
    win2.mainloop()
    
############LoginF###############
#################################
    
def login():
######AFTER LOGIN##########
    def main():
        win12=tkinter.Toplevel(win)
        win12.geometry('850x650+225+45')
        win12.configure(bg="black",cursor='star')
        win12.resizable(False,False)
        
        loglb12=tkinter.Label(win12,text='*WELCOME*',font=('Times New Roman',50,'bold'),fg='pink',bg='black')
        loglb12.place(x=170,y=50)
#########DESTROY BUTTON#########        
        def goback():
            win7.destroy()
            
        win7=tkinter.Toplevel(win)
        win7.geometry('850x650+225+45')
        win7.configure(bg="black",cursor='star')
        win7.resizable(False,False)
       
        loglbl=tkinter.Label(win4,text='*LOGIN PAGE*',font=('Times New Roman',50,'bold'),fg='pink',bg='black')
        loglbl.place(x=170,y=50)
        
        btn7=tkinter.Button(win7,text='GO BACK',bg='pink',fg='black',font=('Times New Roman',20),height=0,width=10,activebackground='black',activeforeground='pink',command=goback)
        btn7.place(x=350,y=330)

##########CHECK F############        
    def validate2():
        result=True
        username=user.get()
        password=pas.get()
        if(username=="" or password==""):
           loglbl4.configure(text="PLEASE FILL THE BLANKS",fg="red")
           result=False 
        elif(len(username)<5):
            loglbl4.configure(text="USERNAME MUST BE AT LEAST 5 CHARACTER",fg="red")
            result=False
        elif(len(password)<8):
            loglbl4.configure(text="PASSWORD MUST BE AT LEAST 8 CHARACTER",fg="red")
            result=False    
        elif(not(username.isalpha())):
            loglbl4.configure(text="INVALID CHARACTERS FOR USERNAME!",fg="red")
            result=False  
        else:
            try:
                with open('D:/passs.json') as f:
                    dct=json.load(f)
                if user not in dct:
                    loglbl4.configure(text="USERNAME NOT EXIST!",fg="red")
                    result=False
            except FileNotFoundError:
                creat_file()
        return result
###########VARIFY LOGIN############
    def tojsonfile2():
        global cnt
        username=user.get()
        password=pas.get()
        with open('D:/passs.json') as f:
            dct=json.load(f)
        if username in dct:
            if dct[user]==pas:
                main()
   
        cnt+=1
        if cnt==3:
            loglbl4.configure(text="3 TIMES ERROR!",fg="red")
            win4.destroy()
###########DESTROY BUTTON##########         
    def back2():
        win4.destroy()
##########MAIN LOGIN F###########       
    def login2():
        loglbl4.configure(text='')
        if validate2():
            tojsonfile2()
            
        
    win4=tkinter.Toplevel(win)
    win4.geometry('850x650+225+45')
    win4.configure(bg="black",cursor='star')
    win4.resizable(False,False)
    
    loglbl=tkinter.Label(win4,text='*LOGIN PAGE*',font=('Times New Roman',50,'bold'),fg='pink',bg='black')
    loglbl.place(x=170,y=50)

    user=Entry(win4,width=25,font=("Times New Roman",19),bg='pink',selectbackground='black',selectforeground='pink')
    user.place(x=280,y=200)
    sublbl2=tkinter.Label(win4,text='USERNAME',font=('Times New Roman',15,'bold'),fg='pink',bg='black')
    sublbl2.place(x=370,y=170)

    pas=Entry(win4,width=25,font=("Times New Roman",19),bg='pink',selectbackground='black',selectforeground='pink',show='*')
    pas.place(x=280,y=265)
    loglbl3=tkinter.Label(win4,text='PASSWORD',font=('Times New Roman',15,'bold'),fg='pink',bg='black')
    loglbl3.place(x=370,y=235)

    btn5=tkinter.Button(win4,text='LOGIN',bg='pink',fg='black',font=('Times New Roman',20),height=0,width=10,activebackground='black',activeforeground='pink',command=login2)
    btn5.place(x=350,y=330)

    btn4=tkinter.Button(win4,text='BACK',bg='pink',fg='black',font=('Times New Roman',15),height=0,width=7,activebackground='black',activeforeground='pink',command=back2)
    btn4.place(x=387,y=400)
    
    loglbl4=tkinter.Label(win4,text='',font=('Times New Roman',13,'bold'),fg='pink',bg='black')
    loglbl4.place(x=320,y=450)
    
    win4.mainloop()








############DeleteF###############
def delete():
############DELETE CONFIRM##########    
    def confirmdel(): 
        def sdlt():
            def backmenue():
                win9.destroy()
                win8.destroy()
                win5.destroy()
            
            win9=tkinter.Toplevel(win)
            win9.geometry('450x250+430+225')
            win9.configure(bg="black",cursor='star')
            win9.resizable(False,False)
            
            dellbl11=tkinter.Label(win9,text='ACCOUNT DELETED SUCCESSFULLY!',font=('Times New Roman',15,'bold'),fg='pink',bg='black')
            dellbl11.place(x=55,y=50)
            
            btn11=tkinter.Button(win9,text='BACK TO MENUE',bg='pink',fg='black',font=('Times New Roman',15),height=0,width=17,activebackground='black',activeforeground='pink',command=backmenue)
            btn11.place(x=130,y=120)
        
            win9.mainloop()
        def no():
            win8.destroy()
        def yes():
            with open('D:/passs.json') as f:
                dct=json.load(f)
                dct.pop(username)
            sdlt()
                
        
            
            
            
        win8=tkinter.Toplevel(win)
        win8.geometry('850x650+225+45')
        win8.configure(bg="black",cursor='star')
        win8.resizable(False,False)
        
        dellbl8=tkinter.Label(win8,text='*WARNING*',font=('Times New Roman',50,'bold'),fg='pink',bg='black')
        dellbl8.place(x=220,y=40)
    
        dellbl9=tkinter.Label(win8,text='IF YOU CLICK ON YES BUTTON,YOUR ACCOUNT WILL BE REMOVE,',font=('Times New Roman',15,'bold'),fg='pink',bg='black')
        dellbl9.place(x=115,y=230)
    
        dellbl10=tkinter.Label(win8,text='ARE YOU SURE?',font=('Times New Roman',15,'bold'),fg='pink',bg='black')
        dellbl10.place(x=345,y=260)
        
        btn8=tkinter.Button(win8,text='YES',bg='pink',fg='black',font=('Times New Roman',17),height=0,width=10,activebackground='black',activeforeground='pink',command=yes)
        btn8.place(x=260,y=330)
        
        btn9=tkinter.Button(win8,text='NO',bg='pink',fg='black',font=('Times New Roman',17),height=0,width=10,activebackground='black',activeforeground='pink',command=no)
        btn9.place(x=450,y=330)
        
        dellbl9=tkinter.Label(win5,text='',font=('Times New Roman',13,'bold'),fg='pink',bg='black')
        dellbl9.place(x=320,y=450)
        
        win8.mainloop()
    
    
    def back3():
        win5.destroy()
############VALIDATION##########        
    def validate3():
        result=True
        dellbl4.configure(text="")
        username=user.get()
        password=pas.get()
        if(username=="" or password==""):
           dellbl4.configure(text="PLEASE FILL THE BLANKS",fg="red")
           result=False
        elif(len(username)<5):
            dellbl4.configure(text="USERNAME MUST BE AT LEAST 5 CHARACTER",fg="red")
            result=False
        elif(len(password)<8):
            dellbl4.configure(text="PASSWORD MUST BE AT LEAST 8 CHARACTER",fg="red")
            result=False    
        elif(not(username.isalpha())):
            dellbl4.configure(text="INVALID CHARACTERS FOR USERNAME!",fg="red")
            result=False 
        else:    
            try:
                with open('D:/passs.json') as f:
                    dct=json.load(f)
                if user not in dct:
                    dellbl4.configure(text="USERNAME IS INCORRECT!",fg="red")
                    result=False
            except:
                dellbl4.configure(text="SOMETHING WENT WRONG!",fg="red")

############DELETING FROM JSON######
    def tojasonfile3():
         username=user.get()
         password=pas.get()
         with open('passs.json') as f:
             dct=json.load(f)
         if username in dct:
             if dct[user]==pas:
                 confirmdel()


##########MAIN DELETE F###########
    def dlt():
        dellbl4.configure(text='')
        if validate3():
            tojsonfile3()
            
            
    win5=tkinter.Toplevel(win)
    win5.geometry('850x650+225+45')
    win5.configure(bg="black",cursor='star')
    win5.resizable(False,False)
    
    dellbl=tkinter.Label(win5,text='*DELETE PAGE*',font=('Times New Roman',50,'bold'),fg='pink',bg='black')
    dellbl.place(x=170,y=50)

    user=Entry(win5,width=25,font=("Times New Roman",19),bg='pink',selectbackground='black',selectforeground='pink')
    user.place(x=280,y=200)
    dellbl2=tkinter.Label(win5,text='USERNAME',font=('Times New Roman',15,'bold'),fg='pink',bg='black')
    dellbl2.place(x=370,y=170)

    pas=Entry(win5,width=25,font=("Times New Roman",19),bg='pink',selectbackground='black',selectforeground='pink',show='*')
    pas.place(x=280,y=265)
    dellbl3=tkinter.Label(win5,text='PASSWORD',font=('Times New Roman',15,'bold'),fg='pink',bg='black')
    dellbl3.place(x=370,y=235)

    btn6=tkinter.Button(win5,text='DELETE',bg='pink',fg='black',font=('Times New Roman',20),height=0,width=10,activebackground='black',activeforeground='pink',command=confirmdel)
    btn6.place(x=350,y=330)

    btn7=tkinter.Button(win5,text='BACK',bg='pink',fg='black',font=('Times New Roman',15),height=0,width=7,activebackground='black',activeforeground='pink',command=back3)
    btn7.place(x=387,y=400)
    
    dellbl4=tkinter.Label(win5,text='',font=('Times New Roman',13,'bold'),fg='pink',bg='black')
    dellbl4.place(x=320,y=450)
    
    win5.mainloop()
############ExitF###############    
def exitt():
    win.destroy()



#####main tkinter##############
win=tkinter.Tk()
win.title('MENUE')
win.geometry('850x650+225+45')
win.configure(bg="black",cursor='star')
win.resizable(False,False)
win.iconbitmap('star.ico')


lbl=tkinter.Label(win,text='*MAIN APP*',font=('Times New Roman',70,'bold'),fg='pink',bg='black')
lbl.place(x=160,y=50)


btn=tkinter.Button(win,text='SUBMIT',bg='pink',fg='black',font=('Times New Roman',30),height=1,width=10,activebackground='black',activeforeground='pink',command=submit)
btn.place(x=310,y=200)



btn2=tkinter.Button(win,text='LOGIN',bg='pink',fg='black',font=('Times New Roman',30),height=1,width=10,activebackground='black',activeforeground='pink',command=login)
btn2.place(x=310,y=300)

btn3=tkinter.Button(win,text='DELETE',bg='pink',fg='black',font=('Times New Roman',30),height=1,width=10,activebackground='black',activeforeground='pink',command=delete)
btn3.place(x=310,y=400)

btn4=tkinter.Button(win,text='EXIT',bg='pink',fg='black',font=('Times New Roman',30),height=1,width=10,activebackground='black',activeforeground='pink',command=exitt)
btn4.place(x=310,y=500)


win.mainloop()