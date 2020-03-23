import random 

running = True
mao=100
aposta=10
while running:
    jogador = input("O que voce deseja fazer? apostar/sair: ")
    
    if jogador == 'sair':
        print(mao)
        running=False

    if jogador == 'apostar': 
        while True:
            dado1=random.randint(1,6)
            dado2=random.randint(1,6)

            if dado1+dado2 == 7 or dado1+dado2==11:
                mao=mao+ aposta +10
                running = False 

            if dado1+dado2 == 2 or dado1+dado2==3 or dado1+dado2==12:
                mao=mao-aposta
                running = False 

            else:
                running=False

        










