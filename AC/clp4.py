import random # Biblioteca para gerar aletoriaridade ao programa.
import math # Biblioteca para calculos.


class Product:
# Classe para gerenciar o objeto Produto.
    def __init__(self, id, name, description, price):
        # Função que inicia o objeto Produto e seus parametros.
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    def __repr__(self):
        # Função para exibir o Produto na nota.
        return f"{self.id} -- {self.name} -- R$ {self.price:.2f}"


class Cart:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)
    
    def calculate(self):
        self.total = round(sum(p.price for p in self.products), 2)
        return self.total

def calc_change(total, value):
    trocos = {
        5: 0,
        2: 0,
        1: 0,
        0.5: 0,
        0.25: 0,
        0.10: 0,
        0.05: 0,
        0.01: 0
    }

    if total == value:
        return 'Não há Troco'
    if total > value:
        return f'Falta - R$ {total - value:.2f}'

    change = round(value - total, 2)

    for troco in trocos:
        trocos[troco] += change // troco
        change = change % troco

    return trocos


def main():
    cart = Cart()
    for i in range(5):
        price = 1 + (random.randint(0, 180) * 5) / 100
        product = Product(i, f'Product {i}', f'Description Product {i}', price)
        cart.add(product)
    print('\n----- Nota Fiscal -----\n')
    for product in cart.products:
        print(product)

    total = cart.calculate()
    print(f"\nTotal: R$ {total:.2f}")
    print('Valor Recebido: R$ 50')
    print(f'Troco: {50 - total}\n')
    print(calc_change(total, 50))

main()
