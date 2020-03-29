import random 
import time

running = True
mao=100
aposta=10

def dados():
    dado_1=random.randint(1,6)
    dado_2=random.randint(1,6)

    return dado_1,dado_2

while running:
    jogador = input("O que voce deseja fazer? apostar/sair: ")
      
    if jogador == 'apostar':
        #aposta = float(input('Qual o valor da aposta?: '))
        game=True
        while game:
            dado1,dado2 = dados()
            soma=dado1+dado2
            print('Dados tirados: ',dado1,dado2,'|','Soma: ',soma)

            if soma == 7 or soma==11:
                mao=mao+ aposta +10
                print('Você ganhou')
    
                break

            if soma == 2 or soma==3 or soma==12: #craps
                print('Deu craps')
                mao=mao-aposta
    
                game = False 

            else: #Point
    
                print('########################')
                print('Você está na fase Point')
                print('########################')
    
                point = True
                while point:
                    dado_point1,dado_point2=dados()
                    soma_point=dado_point1+dado_point2
                    print('Dados tirados: ',dado_point1,dado_point2,'|','Soma: ',soma_point)

                    if soma == soma_point:
                        mao=mao+aposta
                        print("Você ganhou a fase Point")
                        break

                    if soma_point >= 7:
                        mao=mao-aposta
                        print('Você perdeu')
                        point=False

                    else:
                        print('Jogue de novo')
                        
                game = False

    if jogador == 'sair':
        print(mao)
        running=False

    
        










