import random # Biblioteca para gerar aletoriaridade ao programa.

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
        self.total = sum(p.price for p in self.products)
        return self.total

def calc_change(total, pay):
    if total == pay:
        return 0 
    if total % 5 == 0:
        ...

    ...

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
    print(f"\nTotal: {total:.2f}\n")

main()
