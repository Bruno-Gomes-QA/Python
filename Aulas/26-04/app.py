import os
from database import Database
import tkinter
import time

db = Database()

def create_worker():
    # worker expect = name, hours, value_hours, worked_days
    os.system('clear')
    while True:
        try:
            print('-- Informe os dados do funcionário --\n')
            name = str(input('Nome: '))
            hours = float(input('Horas Trabalhadas P/Dia: '))
            worked_days = float(input('Dias trabalhados no mês: '))
            value_hours = float(input('Valor por Hora: R$ '))
            worker = [name, hours, value_hours, worked_days]
            break
        except:
            os.system('clear')
            raise Exception('\n-- Dados invalidos, tente novamente --\n')

    db.insert_worker(worker)


def search_worker():
    os.system('clear')
    try:
        id = int(input('\nInforme o ID do funcionário: '))
        print(db.search_worker_by_id(id))
        time.sleep(1000)
    except:
        os.system('clear')
        print('-- Tipo de dado inválido, tente novamente --\n')

def welcome():
    print('----- Seja Bem-vindo -----\n')
    while True:
        try:
            print('\n-- Menu Inicial --\n')
            print('1 - Cadatrar novo funcionário\n2 - Consultar folha de pagamento\n3 - Sair')
            choice = int(input('\nEscolha uma das opções: '))
            if choice == 1:
                result = create_worker()
            elif choice == 2:
                search_worker()
            elif choice == 3:
                print('\n\nEncerrando ...')
                time.sleep(2)
                os.system('clear')
                break
            else:
                raise Exception('\n-- Opção Inválida, tente novamente --\n')
        except:
            os.system('clear')
            print('\n-- Opção Inválida, tente novamente --\n')
    

print(db.search_worker_by_id('1'))
time.sleep(400000)
welcome()



    