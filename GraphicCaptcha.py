# CHECKBOX: multiple choices
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import tkinter.simpledialog
import tkinter.colorchooser
from tkinter import messagebox



class checkbox:
        def __init__(self,root):
            self.f=Frame(root,height=700,width=650,bg="white")
            self.f.propagate(0)
            self.f.pack()   
            # 4 variables for 4 checkboxes
            self.var1=IntVar()
            self.var2=IntVar()
            self.var3=IntVar()
            self.var4=IntVar()
            self.var5=IntVar()
            self.var6=IntVar()
            self.var7=IntVar()
            self.var8=IntVar()
            self.var9=IntVar()
            
            self.l0=Label(self.f,text="Select all the images which show Buses",font=("Arial",20))
            self.l0.place(x=70,y=0) 
            messagebox.showinfo("Test","Prove that you are not Robot !") 
            
            # Create a photoimage object of the image1 in the path
        #Image1
            image1 = Image.open("C:/Users/hp/buss.jpg")
            test = ImageTk.PhotoImage(image1)
            #label1
            self.label1 = tkinter.Label(self.f,image=test)
            self.label1.image = test
            self.label1.place(x=10,y=50)
            #checkbox1
            self.c1=Checkbutton(self.f,variable=self.var1,text="")
            self.c1.place(x=50,y=180)
         
        
        #image2
            image2 = Image.open("C:/Users/hp/nbuss.jpg")
            test2 = ImageTk.PhotoImage(image2)
            #label2
            self.label2 = tkinter.Label(self.f,image=test2)
            self.label2.image = test2
            self.label2.place(x=220,y=50)
            #checkbox2
            self.c2=Checkbutton(self.f,variable=self.var2,text="")
            self.c2.place(x=250,y=180)
        #image3
            image3 = Image.open("C:/Users/hp/buss1.jpg")
            test3 = ImageTk.PhotoImage(image3)
            #label3
            self.label3 = tkinter.Label(self.f,image=test3)
            self.label3.image = test3
            self.label3.place(x=450,y=50)
            #checkbox3
            self.c3=Checkbutton(self.f,variable=self.var3,text="")
            self.c3.place(x=490,y=180)
            
        #image4
            image4 = Image.open("C:/Users/hp/nbuss1.jpg")
            test4 = ImageTk.PhotoImage(image4)
            #label3
            self.label4 = tkinter.Label(self.f,image=test4)
            self.label4.image = test4
            self.label4.place(x=10,y=200)
            #checkbox3
            self.c4=Checkbutton(self.f,variable=self.var4,text="")
            self.c4.place(x=50,y=330)
        #image5
            image5 = Image.open("C:/Users/hp/nbuss2.jpg")
            test5 = ImageTk.PhotoImage(image5)
            #label3
            self.label5 = tkinter.Label(self.f,image=test5)
            self.label5.image = test5
            self.label5.place(x=200,y=200)
            #checkbox3
            self.c5=Checkbutton(self.f,variable=self.var5,text="")
            self.c5.place(x=240,y=330)
        #image6
            image6 = Image.open("C:/Users/hp/nn.jpg")
            test6 = ImageTk.PhotoImage(image6)
            #label3
            self.label6 = tkinter.Label(self.f,image=test6)
            self.label6.image = test6
            self.label6.place(x=440,y=200)
            #checkbox3
            self.c6=Checkbutton(self.f,variable=self.var6,text="")
            self.c6.place(x=490,y=330)
        #image7
            image7 = Image.open("C:/Users/hp/buss2.jpg")
            test7 = ImageTk.PhotoImage(image7)
            #label3
            self.label7 = tkinter.Label(self.f,image=test7)
            self.label7.image = test7
            self.label7.place(x=10,y=350)
            #checkbox3
            self.c7=Checkbutton(self.f,variable=self.var7,text="")
            self.c7.place(x=50,y=485)
        #image8
            image8 = Image.open("C:/Users/hp/nbuss3.jpg")
            test8 = ImageTk.PhotoImage(image8)
            #label3
            self.label8 = tkinter.Label(self.f,image=test8)
            self.label8.image = test8
            self.label8.place(x=210,y=350)
            #checkbox3
            self.c8=Checkbutton(self.f,variable=self.var8,text="")
            self.c8.place(x=250,y=485)
        #image9
            image9 = Image.open("C:/Users/hp/buss3.jpg")
            test9 = ImageTk.PhotoImage(image9)
            #label3
            self.label9 = tkinter.Label(self.f,image=test9)
            self.label9.image = test9
            self.label9.place(x=440,y=350)
            #checkbox3
            self.c9=Checkbutton(self.f,variable=self.var9,text="")
            self.c9.place(x=490,y=485)
    
  

            self.b1=Button(self.f,text="Verify",font=("Arial",16),command=self.displayCount)
            self.b1.place(x=260,y=520)
        

          
        def display(self):

            s1=self.var1.get()
            s2=self.var2.get()
            s3=self.var3.get()
            s4=self.var4.get()
            s5=self.var5.get()
            s6=self.var6.get()
            s7=self.var7.get()
            s8=self.var8.get()
            s9=self.var9.get()
            
            count=0
            if s1==1:
                count+=1
            if s2==1:
                count-=1
            if s3==1:
                count+=1
            if s4==1:
                count-=1
            if s5==1:
                count-=1
            if s6==1:
                count-=1
            if s7==1:
                count+=1
            if s8==1:
                count-=1
            if s9==1:
                count+=1 
        def clear(self):
            self.var1.set(0)
            self.var2.set(0)
            self.var3.set(0)
            self.var4.set(0)
            self.var5.set(0)
            self.var6.set(0)
            self.var7.set(0)
            self.var8.set(0)
            self.var9.set(0)
            
            

        def displayCount(self):
            s1=self.var1.get()
            s2=self.var2.get()
            s3=self.var3.get()
            s4=self.var4.get()
            s5=self.var5.get()
            s6=self.var6.get()
            s7=self.var7.get()
            s8=self.var8.get()
            s9=self.var9.get()
            count=0
            lim=0
            if s1==1:
                count+=1
                lim+=1
                
            if s2==1:
                count-=1
                lim+=1
            if s3==1:
                count+=1
                lim+=1
            if s4==1:
                count-=1
                lim+=1
            if s5==1:
                count-=1
                lim+=1
            if s6==1:
                count-=1
                lim+=1
            if s7==1:
                count+=1
                lim+=1
            if s8==1:
                count-=1
                lim+=1
            if s9==1:
                count+=1 
                lim+=1
                
            if ( lim==4):
                if(count==4):
                    #L=Label(text=count)
                    #L.place(x=70,y=250)
                    messagebox.showinfo("Successful","you passed it")
                    root.destroy()
                else:
                    messagebox.showinfo("Fail test! ","press exit or retry  button below to exit ")
                    exit_button = Button(self.f, text="Exit", command=root.destroy)
                    retry_button=Button(self.f,text="Retry",command=self.clear)
                    exit_button.place(x=120,y=530)
                    retry_button.place(x=400,y=530)
            else:
                messagebox.showwarning("", "Select only four images!")
                   
    
root=Tk()
c=checkbox(root)


root.mainloop()


# In[ ]:





# In[ ]:




