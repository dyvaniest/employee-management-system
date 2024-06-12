from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk


class Employee:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('Unila Employee Management System')


        lbl_title=Label(self.root, text='UNILA EMPLOYEE MANAGEMENT SYSTEM', font=('times new roman',37,'bold'),fg='#1d91ff',bg='white')
        lbl_title.place(x=0,y=0,width=1350,height=50)

        #logo
        img_logo=Image.open('college_images/logo-unila.png')
        img_logo=img_logo.resize((50,50),Image.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=100,y=0,width=50,height=50)

        # Image Frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE, bg='white')
        img_frame.place(x=0,y=50,width=1530,height=130)

        #1st
        img1=Image.open('college_images/rektorat.jpg')
        img1=img1.resize((540,160),Image.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame, image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=160)

        #2st
        img2=Image.open('college_images/bundaran.jpg')
        img2=img2.resize((540,160),Image.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img2)

        self.img_2=Label(img_frame, image=self.photo2)
        self.img_2.place(x=540,y=0,width=540,height=160)

        #3st
        img3=Image.open('college_images/embung.jpg')
        img3=img3.resize((540,160),Image.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img3)

        self.img_3=Label(img_frame, image=self.photo3)
        self.img_3.place(x=1000,y=0,width=540,height=160)

        # Main Frame
        Main_frame=Frame(self.root,bd=2,relief=RIDGE, bg='white')
        Main_frame.place(x=10,y=200,width=1260,height=520)

        # upper Frame
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE, bg='white', text='Employee Information', font=('times new roman',11,'bold'), fg='black')
        upper_frame.place(x=10,y=10,width=1240,height=150)

        # Label and Entry Fields
        lbl_dep=Label(upper_frame, text='Department:', font=('arial',12,'bold'), bg='white')
        lbl_dep.grid(row=0, column=0, padx=2, sticky=W)

        combo_dep=ttk.Combobox(upper_frame, font=('arial',11,'bold'), width=17, state='readonly')
        combo_dep['values']=('Select Department', 'HR', 'Software Engineer', 'Manager')
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=2, pady=10,sticky=W)

        #Name
        lbl_name=Label(upper_frame, font=('arial',12,'bold'), text="Name:", bg='white')
        lbl_name.grid(row=0, column=2, padx=2, pady=7, sticky=W)

        text_name=ttk.Entry(upper_frame, width=22, font=('arial',11,'bold'))
        text_name.grid(row=0, column=3, padx=2, pady=7)

        #Designition
        lbl_Designition=Label(upper_frame, font=('arial',12, 'bold'), text="Designition:", bg='white')
        lbl_Designition.grid(row=1, column=0, padx=2, pady=7, sticky=W)

        text_Designition=ttk.Entry(upper_frame, width=22, font=('arial',11,'bold'))
        text_Designition.grid(row=1, column=1, sticky=W, padx=2, pady=7)

        #Email
        lbl_email=Label(upper_frame, font=('arial',12,'bold'), text="Email:", bg='white')
        lbl_email.grid(row=1, column=2, padx=2, pady=7, sticky=W)

        text_email=ttk.Entry(upper_frame, width=22, font=('arial',11,'bold'))
        text_email.grid(row=1, column=3, padx=2, pady=7)

        #Address
        lbl_address=Label(upper_frame, font=('arial',12, 'bold'), text="Address:", bg='white')
        lbl_address.grid(row=2, column=0, padx=2, pady=7, sticky=W)

        text_Designition=ttk.Entry(upper_frame, width=22, font=('arial',11,'bold'))
        text_Designition.grid(row=2, column=1, sticky=W, padx=2, pady=7)


        # down Frame
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE, bg='white', text='Employee Information Table', font=('times new roman',11,'bold'), fg='black')
        down_frame.place(x=10,y=160,width=1240,height=150)

        # Label and Entry Fields
        self.var_dep=StringVar()

if __name__=="__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()
