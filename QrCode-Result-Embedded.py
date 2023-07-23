#importing the various libraries 
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import qrcode
from tkinter import messagebox


import pyrebase

global file_detail  
global file 
global mat_no

firebaseConfig= {
  "apiKey": "AIzaSyAJx0AnOWR-vdj8io8N_3WsirfctisC5yQ",
  "authDomain": "certificatev-a4e74.firebaseapp.com",
  "projectId": "certificatev-a4e74",
  "storageBucket": "certificatev-a4e74.appspot.com",
  "messagingSenderId": "739844066998",
  "appId": "1:739844066998:web:a8a56dac4a4c326bff2017",
  "measurementId": "G-NYCRP47CNT",
  "databaseURL": ""
  }

firebase=pyrebase.initialize_app(firebaseConfig)

#define storage
storage=firebase.storage()



def conpage():
    root.destroy()
    root2 = Tk()
    root2.title('HOME PAGE')
    root2['bg'] = '#96C3EB'
    root2.resizable(False, False)  # This code helps to disable windows from resizing
    #setting window default size for home page
    window_height = 500
    window_width = 900

    screen_width = root2.winfo_screenwidth()
    screen_height = root2.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    root2.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    
    #Declaring global variable for file name & details 
 

    #System config

    
    #function to allow selection of file



    title = Label(root2,text="FPB CERTIFICATE QR CODE BUILDER ", bg='#96C3EB', fg='Blue',font=('Courier',20,'bold'))
    title.grid(column=0, row=1, columnspan=2)
    
    Label(root2, text='Enter Student Name', bg='#96C3EB',font=('Century 15')).grid(column=0, row=2, pady=2, padx=20)
    stud_name = Entry(root2, width = 35, font=('Century 15'))
    stud_name.grid(column=0, row=3, pady=2, padx=20)

    Label(root2, text='Enter Matric No', bg='#96C3EB',font=('Century 15')).grid(column=1, row=2, pady=2, padx=20)
    mat_no = Entry(root2, width = 35, font=('Century 15'))
    mat_no.grid(column=1, row=3, pady=2, padx=20)

    space = Label(root2, text='', bg='#96C3EB')
    space.grid(column=1, row=4, pady=2, padx=20)

    Label(root2, text='Enter Year of Entry', bg='#96C3EB',font=('Century 15')).grid(column=0, row=5, pady=2, padx=20)
    Eyear = Entry(root2, width = 35, font=('Century 15'))
    Eyear.grid(column=0, row=6, pady=4, padx=20)

    Label(root2, text='Enter Year of Graduation', bg='#96C3EB',font=('Century 15')).grid(column=1, row=5, pady=2, padx=20)
    Gyear = Entry(root2, width = 35, font=('Century 15'))
    Gyear.grid(column=1, row=6, pady=4, padx=20)
       
    wspace = Label(root2, text='', bg='#96C3EB')
    wspace.grid(column=1, row=7, pady=2, padx=20)

    Label(root2,text="Enter Certificate Name: ", bg='#96C3EB',font=('Century 15')).grid(column=0, row=8, columnspan=2)
    file_name = Entry(root2, width = 35, font=('Century 15'))
    file_name.grid(column=0, row=9, pady=2, columnspan=2)

 
    
    def generate():
        file = filedialog.askopenfilename(title="Select a File", filetype=(('all file','*.*'),('all files','*.*')))
        fileupload=file
        cloudfilename=mat_no.get()
        storage.child(cloudfilename).put(fileupload)

        urln = storage.child(cloudfilename).get_url(None)

        import os
        # checking if the directory demo_folder 
        # exist or not.
        if not os.path.exists("Qr"):
            
        # if the demo_folder directory is not present 
        # then create it.
            os.makedirs("Qr")
               
        img_bg = Image.open(file)
        qr = qrcode.QRCode(box_size=2)
        qr.add_data('Name: ' +stud_name.get()+ '\n' + 'Mat_No: '+mat_no.get()+ '\n' \
          + 'Entry Year: '+Eyear.get()+ '\n' + 'Graduation Year: '+Gyear.get()+ '\n'+ urln)
        qr.make()
        img_qr = qr.make_image()

        pos = (img_bg.size[0] - img_qr.size[0], img_bg.size[1] - img_qr.size[1])

        img_bg.paste(img_qr, pos)
        fileDirec=file_name.get() #Getting the directory where the file has to be save
        complete_name = os.path.join('Qr', fileDirec)
        img_bg.save(f'{complete_name}.png') #Saving the QR Code
    #Showing the pop up message on saving the file
        
        messagebox.showinfo("DataFlair QR Code Generator","QR Code is saved successfully!")
        mat_no.delete(0, END)
        Eyear.delete(0, END)
        Gyear.delete(0, END)
        file_name.delete(0, END)
        stud_name.delete(0, END)

    def close():
      root2.destroy()
    Exit= Button(root2, text="Exit App", font=('Century 12'), height=2, width=10, fg = 'red', command= close)
    Exit.grid(column=1, row= 10, ipadx=5, pady=15)
    button= Button(root2, text="Upload & \n Generate Qr Code", font=('Century 12'), height=2, width=12, fg = 'Blue', command= generate)
    button.grid(column=0, row= 10, ipadx=5, pady=15)

    root2.mainloop()

def second():
    en1 = username.get()
    en2 = password.get()
        
    if en1 == 'username'  and en2 =='password':
        conpage()
     
    else:
        label1 = Label(root, text='Invalid Credentials')
        label1.pack()
        username.delete(0, END)
        password.delete(0, END)  



#Homepage creation 
root = Tk()
root.title('HOME PAGE')
root['bg'] = 'orange'
root.resizable(False, False)  # This code helps to disable windows from resizing
#setting window default size for home page
window_height = 500
window_width = 900

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))



# Create an object for homepage
title1 = Label(root, text = 'DEPARTMENT OF COMPUTER SCIENCE', font=('Pickwick', 20, 'bold' ), fg = '#000080', bg ='orange', justify=CENTER)
title1.pack()
title2 = Label(root, text = 'FEDERAL POLYTECHNIC BIDA', font=('Bahnschrift', 20), fg = 'Red', bg ='orange', justify=CENTER)
title2.pack()
title2 = Label(root, text = 'CERTIFICATE QR CODE GENERATOR', font=('Bahnschrift', 20, 'bold'), fg = 'Black', bg ='orange',justify=CENTER)
title2.pack()
img = ImageTk.PhotoImage(Image.open("logo.png"))
label = Label(root, image = img, bg ='orange')
label.pack()



global password
global username

#Designing objects for login
us = Label(root, text='Enter Username', font=('Arial', 15, 'bold'), bg ='orange').pack()
username = Entry(root, width=25, font=('Arial 20'))
username.pack()
ps = Label(root, text='Enter Password', font=('Arial', 15, 'bold'), bg ='orange').pack()

password = Entry(root, show = '*', width=25, font=('Arial 20'))
password.pack()



    
admin = Button(root, text = 'Login',font=('Arial', 15), bg ='#5e1914', width=20, border=8, command=second)
admin.pack()

# Create a Label Widget to display the text or Image


root.mainloop()