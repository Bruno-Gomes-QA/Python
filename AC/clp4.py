import random   # Biblioteca para gerar aletoriaridade ao programa.
import math   # Biblioteca para calculos.


class Product:
    # Classe para gerenciar o objeto Produto.
    def __init__(self, id, name, description, price):
        # Inicia o objeto Produto e seus parametros.
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    def __repr__(self):
        # Exibi o Produto na nota.
        return f'{self.id} -- {self.name} -- R$ {self.price:.2f}'


class Cart:
    # Classe para gerenciar o carrinho de produtos.
    def __init__(self):
        # Inicia o objeto Cart.
        self.products = []

    def add(self, product):
        # Adiciona produtos ao carrinho
        self.products.append(product)

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
    # Contrui esse for pois estava fazendo esta mesma operação com if's para cada possível troco,
    # dessa maneira achei mais viavel armazenar as possibilidades em changes e ir iterando por elas.
    for c in changes:
        changes[c] += change // c
        change = round(change % c, 2) # Sem o round possiveis bugs como exemplo se total = 29.05!

    return changes


def main():
    # Função responsável por executar todo o programa e apresentar as informações no terminal.

    cart = Cart()
    for i in range(5):
        price = 1 + (random.randint(0, 180) * 5) / 100
        product = Product(i, f'Produto {i}', f'Descrição {i}', price)
        cart.add(product)
    print('\n----- Nota Fiscal -----\n')
    for product in cart.products:
        print(product)

    total = cart.calculate()
    change = round(50 - total, 2)
    print(f'\nTotal: R$ {total:.2f}')
    print('Valor Recebido: R$ 50')
    print(f'Troco: {50 - total}\n')
    changes = calc_change(total, 50)
    for t in changes:
        value = changes[t]
        if value > 0 and t >= 2:
            print(f'{value:.0f}, Notas de {t}')
        if value > 0  and t < 2:
            print(f'{value:.0f}, Moedas de {t}')

main()
