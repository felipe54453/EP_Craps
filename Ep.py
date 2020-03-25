import random 

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
                game = False 

            if soma == 2 or soma==3 or soma==12: #craps
                mao=mao-aposta
                game = False 

            else: #Point
                game=False

    if jogador == 'sair':
        print(mao)
        running=False

    
        










