import tkinter as tk
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

root = tk.Tk()

root.geometry('500x600')
root.title('STUDENT REGISTRATION AND MANAGEMENT SYSTEM')
bg_color = 'black'
login_student_icon=tk.PhotoImage(file='Image/login.png')
login_admin_icon=tk.PhotoImage(file='Image/admin.png')
add_student_icon=tk.PhotoImage(file='Image/addstd.png')
locked_icon=tk.PhotoImage(file='Image/locked.png')
unlocked_icon=tk.PhotoImage(file='Image/unlocked.png')
add_student_pic_icon=tk.PhotoImage(file='Image/student_profile_img.png')

def confirmation_box(message):

    answer=tk.BooleanVar()
    answer.set(False)

    def action(ans):
        answer.set(ans)
        confirmation_box_fm.destroy()

    confirmation_box_fm=tk.Frame(root,highlightbackground=bg_color,highlightthickness=3)

    message_lb=tk.Label(confirmation_box_fm,text=message,font=('Bold',15))
    message_lb.pack(pady=20)

    cancel_btn=tk.Button(confirmation_box_fm,text='Cancel',font=('Bold',15),bd=0,bg=bg_color,fg='white',
    command=lambda:action(False))
    cancel_btn.place(x=50,y=120)

    yes_btn=tk.Button(confirmation_box_fm,text='Yes',font=('Bold',15),bd=0,bg=bg_color,fg='white',
    command=lambda:action(True))
    yes_btn.place(x=170,y=120,width=80)

    confirmation_box_fm.place(x=100,y=120,width=310,height=220)
    
    root.wait_window(confirmation_box_fm)
    return answer.get()

def message_box(message):
    message_box_fm=tk.Frame(root,highlightbackground=bg_color,highlightthickness=3)
    close_btn=tk.Button(message_box_fm,text='X',bd=0,font=('Bold',13),fg=bg_color,command=lambda:message_box_fm.destroy())
    close_btn.place(x=290,y=5)
    message_lb=tk.Label(message_box_fm,text=message,font=('Bld',15))
    message_lb.pack(pady=50)


    message_box_fm.place(x=100, y=120,width=320,height=200)


def welcome_page():
    def forward_to_student_login_page():
        welcome_page_fm.destroy()
        root.update()
        student_login_page()

    def forward_to_admin_login_page():
        welcome_page_fm.destroy()
        root.update()
        admin_login_page()

    def forward_to_add_account_page():
        welcome_page_fm.destroy()
        root.update()
        add_account_page()
    

    welcome_page_fm=tk.Frame(root, highlightbackground=bg_color, highlightthickness=4)
    heading_lb= tk.Label(welcome_page_fm,text='WELCOME TO STUDENT\nREGISTRATION SYSTEM', bg=bg_color,fg='blue',font=('bold',18))

    heading_lb.place(x=0, y=0, width=800)

    student_login_btn=tk.Button(welcome_page_fm,text='LOGIN STUDENT',bg=bg_color,
                                fg='blue',font=('bold',18),bd=5,command=forward_to_student_login_page)
    student_login_btn.place(x=140,y=115,width=200)

    #PLACE FOR ICON
    student_login_img=tk.Button(welcome_page_fm, image=login_student_icon, bd=0,command=forward_to_student_login_page)
    student_login_img.place(x=60, y=120)




    admin_login_btn=tk.Button(welcome_page_fm,text='LOGIN ADMIN',bg=bg_color,
                                fg='blue',font=('bold',18),bd=5,command=forward_to_admin_login_page)
    admin_login_btn.place(x=140,y=190,width=200)


    # PLACE FOR ICON

    admin_login_img=tk.Button(welcome_page_fm, image=login_admin_icon, bd=0,command=forward_to_admin_login_page)
    admin_login_img.place(x=60, y=195)




    student_login_btn=tk.Button(welcome_page_fm,text='Create Account',bg=bg_color,
                                fg='blue',font=('bold',18),bd=5,command=forward_to_add_account_page)
    student_login_btn.place(x=140,y=265,width=200)

    #PLACE FOR ICON

    add_student_icon_img=tk.Button(welcome_page_fm, image=add_student_icon, bd=0,command=forward_to_add_account_page)
    add_student_icon_img.place(x=60, y=275)

    #kipm


    welcome_page_fm.pack(pady=100)
    welcome_page_fm.pack_propagate(False)
    welcome_page_fm.configure(width=800, height=420)

    #student login page
def student_login_page():
    def show_hide_password():

        if password_ent['show']=='*':
            password_ent.config(show='')
            show_hide_btn.config(image=unlocked_icon)

        else:
            password_ent.config(show='*')
            show_hide_btn.config(image=locked_icon)
    def forward_to_welcome_page():
        student_login_page_fm.destroy()
        root.update()
        welcome_page()

    student_login_page_fm =tk.Frame(root, highlightbackground=bg_color, highlightthickness=4)

    heading_lb=tk.Label(student_login_page_fm, text='STUDENT LOGIN PAGE',bg=bg_color,fg='white',font=('Bold',18))

    heading_lb.place(x=0,y=0,width=395)

    back_btn=tk.Button(student_login_page_fm,text='←',font=('bold',12),fg=bg_color,bd=1,command=forward_to_welcome_page)
    back_btn.place(x=5,y=40)

    stud_icon_lb=tk.Label(student_login_page_fm,image=login_student_icon)
    stud_icon_lb.place(x=170,y=45)

    roll_number_lb=tk.Label(student_login_page_fm,text='Enter Student Roll Number.',font=('bold',15),fg=bg_color)
    roll_number_lb.place(x=80,y=130)

    roll_number_ent=tk.Entry(student_login_page_fm,font=('bold',16),justify=tk.CENTER,highlightcolor=bg_color,highlightbackground='gray',highlightthickness=2)
    roll_number_ent.place(x=80,y=170)

    password_lb=tk.Label(student_login_page_fm,text='Enter Student Password.',font=('bold',15),fg=bg_color)
    password_lb.place(x=80,y=220)

    password_ent=tk.Entry(student_login_page_fm,font=('bold',16),justify=tk.CENTER,highlightcolor=bg_color,highlightbackground='gray',highlightthickness=2,show='*')

    password_ent.place(x=80,y=260)

    show_hide_btn=tk.Button(student_login_page_fm,image=locked_icon,bd=0,command=show_hide_password)
    show_hide_btn.place(x=330,y=270)

    login_btn=tk.Button(student_login_page_fm,text='Login',font=('bold,15'),bg=bg_color,fg='white')
    login_btn.place(x=105,y=320,width=200,height=40)

    student_login_page_fm.pack_propagate(False)
    student_login_page_fm.pack_propagate(False)
    forget_password_btn=tk.Button(student_login_page_fm,text='🙄Forget Password🙄',fg=bg_color,bd=1)
    forget_password_btn.place(x=140,y=370)

    student_login_page_fm.pack(pady=100)
    student_login_page_fm.pack_propagate(False)
    student_login_page_fm.configure(width=400, height=430)
#for password hide 
def admin_login_page():
    def show_hide_password():

        if password_ent['show']=='*':
            password_ent.config(show='')
            show_hide_btn.config(image=unlocked_icon)

        else:
            password_ent.config(show='*')
            show_hide_btn.config(image=locked_icon)

    def forward_to_welcome_page():
        admin_login_page_fm.destroy()
        root.update()
        welcome_page()

#admin login page


    admin_login_page_fm=tk.Frame(root,highlightbackground=bg_color, highlightthickness=4)

    heading_lb=tk.Label(admin_login_page_fm ,text='ADMIN LOGIN PAGE',font=('bold',18),bg=bg_color,fg='white')
    heading_lb.place(x=0,y=0,width=400)

    back_btn=tk.Button(admin_login_page_fm,text='←',font=('bold',12),fg=bg_color,bd=1,command=forward_to_welcome_page)
    back_btn.place(x=5,y=40)



    admin_icon_lb=tk.Label(admin_login_page_fm,image=login_admin_icon)
    admin_icon_lb.place(x=170,y=60)


    username_lb=tk.Label(admin_login_page_fm,text='Enter Admin User Name.',font=('bold',15),fg=bg_color)
    username_lb.place(x=80,y=130)

    username_ent=tk.Entry(admin_login_page_fm,font=('bold',16),justify=tk.CENTER,highlightcolor=bg_color,highlightbackground='gray',highlightthickness=2)
    username_ent.place(x=80,y=170)

    password_lb=tk.Label(admin_login_page_fm,text='Enter Admin Password.',font=('bold',15),fg=bg_color)
    password_lb.place(x=80,y=220)

    password_ent=tk.Entry(admin_login_page_fm,font=('bold',16),justify=tk.CENTER,highlightcolor=bg_color,highlightbackground='gray',highlightthickness=2,show='*')

    password_ent.place(x=80,y=260)

    show_hide_btn=tk.Button(admin_login_page_fm,image=locked_icon,bd=0,command=show_hide_password)
    show_hide_btn.place(x=330,y=270)

    login_btn=tk.Button(admin_login_page_fm,text='Login',font=('bold,15'),bg=bg_color,fg='white')
    login_btn.place(x=105,y=320,width=200,height=40)


    admin_login_page_fm.pack(pady=100)
    admin_login_page_fm.pack_propagate(False)
    admin_login_page_fm.configure(width=400, height=430)

student_gender=tk.StringVar()
branch_list=['CSE','AI&ML','ME','CE','ECE']

def add_account_page():


    pic_path=tk.StringVar()
    pic_path.set('')

    def open_pic():
        path=askopenfilename()
        
        if path:
            
            img=ImageTk.PhotoImage(Image.open(path).resize((100,100)))
            pic_path.set(path)

            add_pic_btn.config(image=img)
            add_pic_btn.image=img

    
    
    def forward_to_welcome_page():

        ans=confirmation_box(message='Do You Want To Leave\nRegistration Form?')
        if ans:
            add_account_page_fm.destroy()
            root.update()
            welcome_page()


    add_account_page_fm=tk.Frame(root,highlightbackground=bg_color, highlightthickness=4)


    add_pic_section_fm=tk.Frame(add_account_page_fm,highlightbackground=bg_color, highlightthickness=2)
    add_pic_btn=tk.Button(add_pic_section_fm,image=add_student_pic_icon,command=open_pic)
    add_pic_btn.pack()

    add_pic_section_fm.place(x=5,y=5,width=105,height=105)
    student_name_lb=tk.Label(add_account_page_fm,text='Enter Student Full Name.',font=('Bold',15))
    student_name_lb.place(x=5,y=130)

    student_name_ent=tk.Entry(add_account_page_fm,font=('Bold',15),highlightcolor=bg_color,highlightbackground='gray',highlightthickness=2)
    student_name_ent.place(x=6,y=160,width=190)

    student_gender_lb=tk.Label(add_account_page_fm,text='Select Student Gender.',font=('bold',15))
    student_gender_lb.place(x=5,y=200)


    male_gender_btn=tk.Radiobutton(add_account_page_fm,text='Male',font=('bold',15),variable=student_gender,value='male')
    male_gender_btn.place(x=5,y=225)

    female_gender_btn=tk.Radiobutton(add_account_page_fm,text='Female',font=('bold',15),variable=student_gender,value='female')
    female_gender_btn.place(x=95,y=225)

    student_gender.set('male')

    student_age_lb=tk.Label(add_account_page_fm,text='Enter Student Age.',font=('Bold',15))
    student_age_lb.place(x=5,y=265)

    student_age_ent=tk.Entry(add_account_page_fm,font=('Bold',15),highlightcolor=bg_color,highlightbackground='gray',highlightthickness=2)
    student_age_ent.place(x=6,y=295,width=190)

    student_contact_lb=tk.Label(add_account_page_fm,text='Enter Contact Number.',font=('Bold',15))
    student_contact_lb.place(x=5,y=330)

    student_contact_ent=tk.Entry(add_account_page_fm,font=('Bold',15),highlightcolor=bg_color,highlightbackground='gray',highlightthickness=2)
    student_contact_ent.place(x=6,y=360,width=190)

    student_Branch_lb=tk.Label(add_account_page_fm,text='Select Branch.',font=('Bold',15))
    student_Branch_lb.place(x=5,y=395)

    select_branch_btn=Combobox(add_account_page_fm,font=('Bold',15),state='readonly',values=branch_list)
    select_branch_btn.place(x=5,y=425,width=180,height=30)

    student_id_lb=tk.Label(add_account_page_fm,text='Student ID Number:-',font=('Bold',15))
    student_id_lb.place(x=200,y=25)

    student_id=tk.Entry(add_account_page_fm,font=('Bold',18),bd=0)
    student_id.place(x=380,y=25,width=80)

    student_id.insert(tk.END,'123456')

    student_id.config(state='readonly')

    id_info_lb=tk.Label(add_account_page_fm,text="""Automatically Generate ID Number.  
Remember Using This ID Number.
Student will Login Account.""",justify=tk.LEFT)
    id_info_lb.place(x=240,y=55)

    student_email_lb=tk.Label(add_account_page_fm,text='Enter Email Address.',font=('Bold',15))
    student_email_lb.place(x=240,y=130)

    student_email_ent=tk.Entry(add_account_page_fm,font=('Bold',15),highlightcolor=bg_color,highlightbackground='gray',highlightthickness=2)
    student_email_ent.place(x=245,y=160,width=190)

    email_info_lb=tk.Label(add_account_page_fm,text="""Through Email Student can recover 
Account.""",justify=tk.LEFT )
    email_info_lb.place(x=240,y=200)

    account_password_lb=tk.Label(add_account_page_fm,text='Create Account Password',font=('Bold',14))
    account_password_lb.place(x=240,y=265)

    account_password_ent=tk.Entry(add_account_page_fm,font=('Bold',15),highlightcolor=bg_color,highlightbackground='gray',highlightthickness=2)
    account_password_ent.place(x=245,y=295,width=190)

    account_password_info_lb=tk.Label(add_account_page_fm,text="""Vie Created Password
Student can Login Account.""",justify=tk.LEFT)
    account_password_info_lb.place(x=240,y=335)

    home_btn=tk.Button(add_account_page_fm,text='Home',font=('Bold',15),bg='red',fg='white',bd=2,command=forward_to_welcome_page)
    home_btn.place(x=240,y=420)

    submit_btn=tk.Button(add_account_page_fm,text='Submit',font=('Bold',15),bg='blue',fg='white',bd=2)
    submit_btn.place(x=360,y=420)


    add_account_page_fm.pack(pady=5)
    add_account_page_fm.pack_propagate(False)
    add_account_page_fm.configure(width=480, height=550)

message_box(message='hello')

root.mainloop()