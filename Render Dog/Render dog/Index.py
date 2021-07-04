import tkinter
from tkinter import *
from tkinter import messagebox
import os
from tkinter import ttk
from tkinter import filedialog






# ========== criar janela
jan = Tk()


# ========== Style = style()
jan.title('Render Dog')
jan.geometry("360x100")
jan.configure(background='grey9')
jan.resizable(width=False, height=False)
jan.attributes('-alpha', 0.9)
jan.iconbitmap(default='FrontEnd/RDIcon.ico')

# =========== Carregando imagens

#logo = PhotoImage(file="Icon.png")

# ========== images

Watch_Button_Image = PhotoImage(file='FrontEnd/bruh.png')



# ========== WIDGETS

'''
LeftFrame = Frame(jan, width=600, height=600, bg='grey', relief='raise')
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=100, height=600, bg='grey', relief='raise')
RightFrame.pack(side=RIGHT)
'''


'''
LogoLabel = Label(LeftFrame, image=logo, bg='MIDNIGHTBLUE')
LogoLabel.place(x=50, y=100)
'''



#Botão

def Start_RW():

    if FolderPath_Value() == 0:
        messagebox.showinfo('No folder', 'Select the folder before start watching')

    else:
        jan.destroy()


WatchButton = tkinter.Button(text="Watch", width='20', height='6', command=Start_RW).place(x= 0, y= 0)


# ========= Shutdown BUtton
def Get_ShutDown_Vallue():

    valor = ShutDown_Button.get()
    return valor


def ShutDown():

    if Get_ShutDown_Vallue() == 1:
        os.system('shutdown /s /t 300')


ShutDown_Button = IntVar()

ShutDownCB = Checkbutton(jan, text='Shutdown PC after render finishes', variable = ShutDown_Button,
                         onvalue=1, offvalue=0).place(x= 150, y= 75, command=ShutDown())


# ========= Get Folder
def getFolderPath():

    folder_selected = filedialog.askdirectory()
    folderPath.set(folder_selected)


def FolderPath():

    folder = folderPath.get()
    return folder


# ==== Detect if folder path is empty
def FolderPath_Value():

    Path = folderPath.get()

    if Path == '':
        return 0

    else:
        return 1



folderPath = StringVar()

btnFind = ttk.Button(jan, text="Browse Folder",command=getFolderPath)
btnFind.place(x= 150, y=20 )


SearchBox = Entry(jan,textvariable=folderPath)
SearchBox.place(x= 150,y= 0)


# === Textbox // Get Email
def GetEmail():

    Rec_Email = Email.get(1.0, END)
    print(Rec_Email)
    Email_File = open('FrontEnd/Email.txt').read()
    if Email_File != '':

        with open('FrontEnd/Email.txt', 'r+') as ELC:
            ELC.truncate(0)


    with open('FrontEnd/Email.txt', 'a') as Write_EmailString:
        Write_EmailString.write(f'{Rec_Email}')

    return Rec_Email



def Email_String():
    Email_Text = GetEmail()
    return Email_Text




Email = Text(jan, height='1', width='26' ,font= ('Helvetica', 8))
Email.place(x= 150, y= 46)



# ======== Get Email Text
GetEmail = Button(jan, text='Confirm Email', command= GetEmail)
GetEmail.place(x= 235, y= 20)



# ========== Exit

def Explicity_CloseRW():
        exit()

jan.protocol("WM_DELETE_WINDOW", Explicity_CloseRW)
jan.mainloop()



















