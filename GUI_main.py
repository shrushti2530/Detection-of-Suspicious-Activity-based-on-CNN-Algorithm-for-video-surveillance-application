import tkinter as tk
#from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk



##############################################+=============================================================
root = tk.Tk()
root.configure(background="#104E8B")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Suspicious Activity Detection System")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
# image2 = Image.open('crop5.jpg')
# image2 = image2.resize((w,h), Image.ANTIALIAS)

# background_image = ImageTk.PhotoImage(image2)

# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image

# background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)


label_l1 = tk.Label(root,background="#104E8B", fg="white", width=67, height=2)
label_l1.place(x=0, y=0)

#
label_l2 = tk.Label(root, text="___Suspicious Activity Detection System___",font=("times", 30, 'bold'),
                    background="#104E8B", fg="white", width=50, height=2)
label_l2.place(x=0, y=0)

img = Image.open('logo.png')
img = img.resize((100,75), Image.ANTIALIAS)
logo_image = ImageTk.PhotoImage(img)

logo_label = tk.Label(root, image=logo_image)
logo_label.image = logo_image
logo_label.place(x=21, y=10)




img=ImageTk.PhotoImage(Image.open("slide1.jpg"))

img2=ImageTk.PhotoImage(Image.open("slide2.jpg"))

img3=ImageTk.PhotoImage(Image.open("slide3.jpg"))


logo_label=tk.Label()
logo_label.place(x=0,y=95)


logo_label1=tk.Label(text='\n\n ...Suspicious Activity Detection System ... \n \n This application use in government level to detect the criminal and to overcome the \n crime graph in India or in world. This project can be used for surveillance \n in public places. Through the visual surveillance, human activities \n can be monitored in sensitive and  public areas such as \n bus stations, railway stations, airports, banks,shopping malls,\n school and colleges, parking lots, roads, etc. to prevent terrorism, theft, \n accidents and illegal parking, vandalism, fighting, chain snatching, crime and other suspicious activities. \n \n',compound='bottom',font=("Times New Roman", 15, 'bold', 'italic'),bd=5,width=100, bg="#CD6090", fg="black")
#logo_label=tk.Label(height=500, width=400)
logo_label1.place(x=250,y=400)

logo_label4=tk.Label(logo_label1,text='*****************************************************************',compound='bottom',font=("Times New Roman", 20, 'bold', 'italic'),bd=5,width=65, bg="#CD6090", fg="white")
#logo_label=tk.Label(height=500, width=400)
logo_label4.place(x=0,y=0)

logo_label4=tk.Label(logo_label1,text='****************************************************************',compound='bottom',font=("Times New Roman", 20, 'bold', 'italic'),bd=5,width=65, bg="#CD6090", fg="white")
#logo_label=tk.Label(height=500, width=400)
logo_label4.place(x=0,y=260)

# using recursion to slide to next image
x = 1

# function to change to next image
def move():
	global x
	if x == 4:
		x = 1
	if x == 1:
		logo_label.config(image=img,width=1800,height=700)
	elif x == 2:
		logo_label.config(image=img2,width=1800,height=700)
	elif x == 3:
		logo_label.config(image=img3,width=1800,height=700)
	x = x+1
	root.after(2000, move)

# calling the function
move()

frame_alpr = tk.LabelFrame(root, text=" --Login & Register-- ", width=800, height=100, bd=5, font=('times', 14, ' bold '),bg="pink")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=400, y=200)


#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def log():
    from subprocess import call
    call(["python","login.py"])
    #root.destroy()
    
def reg():
    from subprocess import call
    call(["python","registration.py"])
    #root.destroy()
    
def window():
  root.destroy()
  
  

#####################################################################################################################

button1 = tk.Button(frame_alpr, text="Login", command=log, width=15, height=1,font=('times', 15, ' bold '), bg="red", fg="white")
button1.place(x=170, y=20)

button2 = tk.Button(frame_alpr, text="Registration",command=reg,width=15, height=1,font=('times', 15, ' bold '), bg="green", fg="white")
button2.place(x=470, y=20)

# button3 = tk.Button(frame_alpr, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="red", fg="white")
# button3.place(x=150, y=300)


label_l1 = tk.Label(root, text="** Suspicious Activity Detection System @ 2021 by _____________ **",font=("Times New Roman", 10, 'bold'),
                    background="black", fg="white", width=100, height=2)
label_l1.place(x=400, y=798)


root.mainloop()