import time as t
import os
import playsound as PS
import Index
from SendEmail import SendEmail
import time

Start_Time = time.time()


# loop principal
while True:

#Def que retorna o tamanho da pasta
    def GS(start_path = Index.FolderPath()):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)

        return total_size


#Função para escrever no arquivo o resultado de GS()
    with open('Logs/Render_Watch1.txt', 'a') as RW1:
        RW1.write(f'{GS()}\n')

#Função para ler o arquivo
    with open('Logs/Render_Watch1.txt', 'r') as RW1:

        LR1 = RW1.readline(15)

        print(f'esse é o valor x1 {LR1}')



    t.sleep(60)


#Função para escrever no arquivo o resultado de GS()
    with open('Logs/Render_Watch2.txt', 'a') as RW2:
        RW2.write(f'{GS()}\n')

#Função para ler o arquivo
    with open('Logs/Render_Watch2.txt', 'r') as RW2:

        LR2 = RW2.readline(15)

        print(f'esse é o valor x2 {LR2}')



    t.sleep(60)


#Função para escrever no arquivo o resultado de GS()
    with open('Logs/Render_Watch3.txt', 'a') as RW3:
        RW3.write(f'{GS()}\n')

#Função para ler o arquivo
    with open('Logs/Render_Watch3.txt', 'r') as RW3:

        LR3 = RW3.readline(15)

        print(f'esse é o valor x3 {LR2}')


    t.sleep(60)


#def para apagar o texto dos arquivos.
    def ereaseText():
        with open('Logs/Render_Watch1.txt', 'r+') as RWE1:
            RWE1.truncate(0)

        with open('Logs/Render_Watch2.txt', 'r+') as RWE2:
            RWE2.truncate(0)

        with open('Logs/Render_Watch3.txt', 'r+') as RWE3:
            RWE3.truncate(0)


        #print('Os arquvios foram limpos.')


#logica para comparar os valores e avaliar se a renderização acabou

    if LR2 == LR3:

        ereaseText()
        #print('Render finalizado!')
        PS.playsound('FrontEnd/FinishSound.mp3')
        SendEmail()
        Index.ShutDown()


        #print(f'Se passaram {Get_H} Horas, {Get_M} Minutos e {Get_time_S} Segundos desde que o render começou')



        exit()

    else :


        #print('os valores não são iguais!')
        ereaseText()
        #print('os arquivos foram limpos, o scan vai começar denovo')





#def Render_Totaltime():
    #RTT = f'Your  render is over, its been passed {Get_H} hours and {Get_M} minutes'