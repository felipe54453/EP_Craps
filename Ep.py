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
    jogador = input("O que voce deseja fazer? pass/field/any/twelve/sair: ")
      
    if jogador == 'pass':
        aposta = float(input('Qual o valor da aposta?: '))
        game=True
        while game:
            dado1,dado2 = dados()
            soma=dado1+dado2
            print('Dados tirados: ',dado1,'e',dado2,'|','Soma: ',soma)

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
                    print('Dados tirados: ',dado_point1,'e',dado_point2,'|','Soma: ',soma_point)

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
    if jogador  == 'field':
        game=True
        while game:
            dado1,dado2 = dados()
            soma=dado1+dado2
            print('Dados tirados: ',dado1,'e',dado2,'|','Soma: ',soma)
            if soma == 3 or soma == 4 or soma == 9 or soma == 10 or soma == 11:
                mao = mao + aposta
                print ('vc ganhou')
            if soma == 2:
                mao = mao + aposta + 2(aposta)
                print ('vc ganhou o dobro')
            if soma == 12 :
                mao = mao + aposta + 3(aposta)
                print ('vc ganhou o triplo')
            if soma == 5 or soma == 6 or soma == 7 or soma == 8:
                mao = mao - mao 
                print ('Voce perdeu tudo')
                
                game = False

    if jogador == 'any':
        aposta = float(input('Qual o valor da aposta?: '))
        dado_any1,dado_any2=dados()
        soma_any = dado_any1+dado_any2
        print('Dados tirados: ',dado_any1,dado_any2,'|','Soma: ',soma_any)
        
        if soma_any == 2 or soma_any==3 or soma_any==12:
            mao=mao+aposta*7
            print('Você ganhou')
        
        else:
            mao=mao-aposta
            print('Voce perdeu')
                
                

    if jogador == 'sair':
        print(mao)
        running=False

    
        










