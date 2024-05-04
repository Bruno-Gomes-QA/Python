import os
import time
# churrasco, japonesa, pizza, outras
options = {1: 0, 2: 0, 3: 0, 4: 0}

def vote():
    print('-- Escolha uma das opções --\n')
    try:
        print('1 - Churrasco\n2 - Comida Japonesa\n3 - Pizza\n4 - Outras')
        choice = int(input('\nSeu Voto: '))
        options[choice] += 1
    except:
        return ...
    print('\nVoto registrado com sucesso!!!\n...')
    time.sleep(2)
    os.system('clear')

print('----- Bem-Vindo -----')
while True:
    print('\n\n-- Menu Inicial --\n')
    print('\n1 - Votar\n2 - Encerrar Votação')
    op = input('\nEscolha uma das opções: ')
    if op == '1':
        os.system('clear')
        vote()
    elif op == '2':
        os.system('clear')
        print('--- Resultado ---\n')
        print(f'Churrasco: {options[1]}')
        print(f'Comida Japonesa: {options[2]}')
        print(f'Pizza: {options[3]}')
        print(f'Outros: {options[4]}')
        break
    else:
        os.system('clear')
        print('-- Opção Inválida, tente novamente --')