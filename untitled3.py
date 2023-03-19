from tkinter import*

root=Tk()
root.geometry("400x400")
root.title("Driving license")

label1=Label(root,text="DRIVING LICENSE",bg="red",fg="white",width=60,height=2,font=30)
label_id=Label(root,text="ID: 19827198349",font="bold")
label_name=Label(root,text="Name: Winnie The Pooh",font="bold")
label_birth=Label(root,text="Date Of Birth: 21 August 1921",font="bold")
label_pin=Label(root,text="Pin: 451478",font="bold")
label_vechile_type=Label(root,text="Authorisation to drive the following vechile: Two Four",font="bold")



label1.pack()
label_id.place(relx=0.0,rely=0.1)
label_name.place(relx=0.0,rely=0.2)
label_birth.place(relx=0.0,rely=0.3)
label_pin.place(relx=0.0,rely=0.4)
label_vechile_type.place(relx=0.0,rely=0.5)
root.mainloop()