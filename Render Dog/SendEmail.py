import smtplib
from Index import Get_ShutDown_Vallue
import time
from RenderDog import STRtime



# ====== Get Shutdown time
def PC_Shutdown_Time():
    Now = time.time()
    ShutDown_time = Now + 300
    PCSDT = time.strftime(" %H:%M %p", time.localtime(ShutDown_time))

    return PCSDT

# ========= Render Total Time
def Render_Totaltime():

    Get_time_S = int(time.time() - Start_Time)
    Get_M = int(Get_time_S / 60)
    Get_H = int(Get_M / 60)

    RTT = f'Your  render is over, its been passed {Get_H} hours and {Get_M} minutes'
    return RTT

# ====== Email Message
def messageDef():
    if Get_ShutDown_Vallue() == 1:
        ShutDown_Message = f'{Render_Totaltime()} \n \n Your computer will Turn off {PC_Shutdown_Time()}' \
                           f'\n \n Thank you for using Render Watch!'

        return ShutDown_Message

    else :
        Finish_message = f'{Render_Totaltime()}!\n \n Thank you for using Render Watch! '
        return Finish_message

# ==== Var that carrt the STR to SendEmail()
Message = messageDef()

def SendEmail():
# ======= Variaveis
    Sender_Email = 'RenderdogSrvr@gmail.com'
    password = 'ZqA12345!@'

# ====== Read the email writed in Index
    with open('FrontEnd/Email.txt', 'r') as Rec_Email:
        Reciver_mail = Rec_Email.read()

# ======= Mandar Email
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()
    server.login(Sender_Email, password)

    server.sendmail(Sender_Email, Reciver_mail, Message)






