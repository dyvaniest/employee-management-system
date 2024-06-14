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
        upper_frame.place(x=10,y=10,width=1240,height=230)

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

        # Married
        lbl_married_status=Label(upper_frame, font=("arial",12,"bold"), text="Married Status:", bg='white')
        lbl_married_status.grid(row=2, column=2, sticky=W, padx=2, pady=7)

        com_txt_married=ttk.Combobox(upper_frame, state="readonly", font=("arial",12, "bold"), width=18)
        com_txt_married['value']=("Married", "Unmarried")
        com_txt_married.current(0)
        com_txt_married.grid(row=2, column=3, sticky=W, padx=2, pady=7)

        # Dob
        lbl_dob=Label(upper_frame, font=("arial",12, "bold"), text="DOB:", bg="white")
        lbl_dob.grid(row=3, column=0, sticky=W, padx=2, pady=7)

        txt_dob=ttk.Entry(upper_frame, width=22, font=('arial',11,'bold'))
        txt_dob.grid(row=3, column=1, padx=2, pady=7)

        # Doj
        lbl_doj=Label(upper_frame, font=("arial",12, "bold"), text="DOJ:", bg="white")
        lbl_doj.grid(row=3, column=2, sticky=W, padx=2, pady=7)

        txt_doj=ttk.Entry(upper_frame, width=22, font=('arial',11,'bold'))
        txt_doj.grid(row=3, column=3, padx=2, pady=7)

        # Id Proof
        com_txt_proof=ttk.Combobox(upper_frame, state="readonly", font=("arial",12, "bold"), width=18)
        com_txt_proof['value']=("Select ID Proof", "PAN CARD", "ADHAR CARD", "DRIVING LICENCE")
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4, column=0, sticky=W, padx=2, pady=7)

        txt_proof=ttk.Entry(upper_frame, width=22, font=('arial',11,'bold'))
        txt_proof.grid(row=4, column= 1, padx=2, pady=7)

        # gender
        lbl_gender=Label(upper_frame, font=("arial",12,"bold"), text="Gender:", bg='white')
        lbl_gender.grid(row=4, column=2, sticky=W, padx=2, pady=7)

        com_txt_gender=ttk.Combobox(upper_frame, state="readonly", font=("arial",12, "bold"), width=18)
        com_txt_gender['value']=("Male", "Female", "Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4, column=3, sticky=W, padx=2, pady=7)

        # phone
        lbl_phone=Label(upper_frame, font=("arial",12, "bold"), text="Phone No:", bg="white")
        lbl_phone.grid(row=0, column=4, sticky=W, padx=2, pady=7)

        txt_phone=ttk.Entry(upper_frame, width=22, font=('arial',11,'bold'))
        txt_phone.grid(row=0, column=5, padx=2, pady=7)

        # country
        lbl_country=Label(upper_frame, font=("arial",12, "bold"), text="Country:", bg="white")
        lbl_country.grid(row=1, column=4, sticky=W, padx=2, pady=7)

        txt_country=ttk.Entry(upper_frame, width=22, font=('arial',11,'bold'))
        txt_country.grid(row=1, column=5, padx=2, pady=7)

        # CTC
        lbl_ctc=Label(upper_frame, font=("arial",12, "bold"), text="Salary(CTC):", bg="white")
        lbl_ctc.grid(row=2, column=4, sticky=W, padx=2, pady=7)

        txt_ctc=ttk.Entry(upper_frame, width=22, font=('arial',11,'bold'))
        txt_ctc.grid(row=2, column=5, padx=2, pady=7)

        # mask image
        # img_mask=Image.open('college_images/pekerja.jpeg')
        # img_mask=img_mask.resize((220,220), Image.LANCZOS)
        # self.photomask=ImageTk.PhotoImage(img_mask)

        # self.img_mask=Label(upper_frame, image=self.photomask)
        # self.img_mask.place(x=1000, y=0, width=220, height=220)

        # Button Frame
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE, bg='white')
        button_frame.place(x=1000,y=2,width=170,height=200)

        btn_add=Button(button_frame,text="Save",font=("arial",15, "bold"), width=13, bg='blue',fg='white')
        btn_add.grid(row=0, column= 0, padx=1, pady=2)

        btn_update=Button(button_frame,text="Update",font=("arial",15, "bold"), width=13, bg='blue',fg='white')
        btn_update.grid(row=1, column= 0, padx=1, pady=5)

        btn_delete=Button(button_frame,text="Delete",font=("arial",15, "bold"), width=13, bg='blue',fg='white')
        btn_delete.grid(row=2, column= 0, padx=1, pady=5)

        btn_clear=Button(button_frame,text="Clear",font=("arial",15, "bold"), width=13, bg='blue',fg='white')
        btn_clear.grid(row=3, column= 0, padx=1, pady=5)

        # down Frame
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE, bg='white', text='Employee Information Table', font=('times new roman',11,'bold'), fg='black')
        down_frame.place(x=10,y=250,width=1240,height=180)

        # Label and Entry Fields
        self.var_dep=StringVar()



if __name__=="__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()
