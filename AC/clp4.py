import os    # Biblioteca para comandos do sistema.
import time  # Biblioteca para pausas no terminal.
import random   # Biblioteca para gerar aleatoriedade ao programa.
import math   # Biblioteca para cálculos.


class Product:
    # Classe para gerenciar o objeto Produto.
    def __init__(self, id, name, description, price):
        # Inicia o objeto Produto e seus parâmetros.
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    def __repr__(self):
        # Exibe o Produto na nota.
        return f'{self.id} -- {self.name} -- R$ {self.price:.2f}'


class Cart:
    # Classe para gerenciar o carrinho de produtos.
    def __init__(self):
        # Inicia o objeto Cart.
        self.products = []

    def add(self, product):
        # Adiciona produtos ao carrinho
        self.products.append(product)

    def remove(self, product_id):
        # Remove produto do carrinho pelo ID
        self.products = [p for p in self.products if p.id != product_id]

    def list_products(self):
        # Lista os produtos no carrinho
        return self.products

    def calculate(self):
        # Calcula o valor total no carrinho
        self.total = round(sum(p.price for p in self.products), 2)
        return self.total


def calc_change(total, value):
    # Função que calcula o troco.
    changes = {5: 0, 2: 0, 1: 0, 0.5: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}

    if total == value:
        return 'Não há Troco'
    if total > value:
        return f'Falta - R$ {total - value:.2f}'

    change = round(value - total, 2)
    for c in changes:
        changes[c] += change // c
        change = round(change % c, 2)  # Sem o round possíveis bugs como exemplo se total = 29.05!

    return changes


def clear_screen():
    # Função para limpar o terminal.
    os.system('cls' if os.name == 'nt' else 'clear')


def show_products(products_list):
    # Função para mostrar os produtos disponíveis.
    print("\nProdutos disponíveis:")
    for product in products_list:
        print(product)
    print()


def add_to_cart(cart, products_list):
    # Função para adicionar produtos ao carrinho.
    while True:
        clear_screen()
        show_products(products_list)
        product_id = int(input("\nDigite o Código do produto que deseja adicionar ao carrinho (ou 0 para finalizar): "))
        if product_id == 0:
            break
        selected_product = next((p for p in products_list if p.id == product_id), None)
        if selected_product:
            cart.add(selected_product)
            print(f"\n{selected_product.name} adicionado ao carrinho.")
        else:
            print("\nProduto não encontrado. Tente novamente.")
        input("\nPressione Enter para continuar...")


def remove_from_cart(cart):
    # Função para remover produtos do carrinho.
    while True:
        clear_screen()
        print("Produtos no carrinho:")
        for product in cart.products:
            print(product)
        print()
        product_id = int(input("\nDigite o ID do produto que deseja remover do carrinho (ou 0 para finalizar): "))
        if product_id == 0:
            break
        cart.remove(product_id)
        print(f"\nProduto {product_id} removido do carrinho.")
        input("\nPressione Enter para continuar...")


def checkout(cart):
    # Função para finalizar a compra e calcular o troco.
    if not cart.products:
        print("\nNenhum produto no carrinho. Encerrando o programa.")
        return

    clear_screen()
    print('\n----- Nota Fiscal -----\n')
    for product in cart.products:
        print(product)

    total = cart.calculate()
    print(f'\nTotal: R$ {total:.2f}')
    
    value_received = float(input('\nInforme o valor recebido: R$ '))
    print(f'\nValor Recebido: R$ {value_received:.2f}')
    
    changes = calc_change(total, value_received)
    if isinstance(changes, str):
        print(changes)
    else:
        print(f'\nTroco: R$ {value_received - total:.2f}')
        for t in changes:
            value = changes[t]
            if value > 0 and t >= 2:
                print(f'{value:.0f}, Notas de {t}')
            if value > 0 and t < 2:
                print(f'{value:.0f}, Moedas de {t}')
    print()


def main():
    # Função responsável por executar todo o programa e apresentar as informações no terminal.
    clear_screen()
    print(r"""
|============================================================|        
|       ____                   _     _                       |
|      / ___|   __ _   _ __   | |_  (_)  _ __     __ _       |
|     | |      / _` | | '_ \  | __| | | | '_ \   / _` |      |
|     | |___  | (_| | | | | | | |_  | | | | | | | (_| |      |
|      \____|  \__,_| |_| |_|  \__| |_| |_| |_|  \__,_|      |
|                                                            |
|============================================================|                                                                    
    """)
    time.sleep(4)

    products_list = [
        Product(1, 'Chocolate', 'Sonho de Valsa, Snikers, Kit Kat', 1.98),
        Product(2, 'Refrigerante 600ml', 'Coca-Cola, Pepsi, Fanta Sabores', 4.99),
        Product(3, 'Salgado', 'Presunto, Queijo, Bauru', 2.49),
        Product(4, 'Café', 'Capputino, Expresso', 3.98),
        Product(5, 'Bolo', 'Chocolate, Limão, Abacaixi', 7.95)
    ]

    cart = Cart()

    while True:
        try:
            clear_screen()
            print("""
    =================================
                Menu Inicial
    =================================

    1. Adicionar produtos ao carrinho
    2. Remover produtos do carrinho
    3. Consultar produtos no carrinho
    4. Finalizar compra
    5. Sair
    """)
            choice = int(input("Escolha uma opção: "))

            if choice == 1:
                add_to_cart(cart, products_list)
            elif choice == 2:
                remove_from_cart(cart)
            elif choice == 3:
                clear_screen()
                print("\nProdutos no carrinho:")
                for product in cart.products:
                    print(product)
                print()
                input("Pressione Enter para continuar...")
            elif choice == 4:
                checkout(cart)
                input("Pressione Enter para sair...")
                break
            elif choice == 5:
                break
            else:
                print("\nOpção inválida. Tente novamente.")
                input("\nPressione Enter para continuar...")
        except:
            print("\nDado inválido. Tente novamente")
            input("\nPressione Enter para continuar...")

main()
