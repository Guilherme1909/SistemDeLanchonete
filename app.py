import os


class Pedido:
    def __init__(self):
        self.nome_cliente = ''
        self.taxa_de_servico = 0
        self.itens_consumidos = []

    def calcular_total(self):
        total = 0
        for i in self.itens_consumidos:
            total += i.preco
        self.taxa_de_servico = (total * 5) / 100
        total += self.taxa_de_servico
        return total

    def mostrar_fatura(self):
        print(f'Conta fechada *{self.nome_cliente}*')
        total = self.calcular_total()
        for i in self.itens_consumidos:
            print(f'{i.__class__.__name__} de {i.recheio} ------------- R${i.preco}')
        print(f'Taxa de Serviço (5%) ------------- R${self.taxa_de_servico}')
        print(f'Valor total ---------------------- R${total}')
                


class Lanche:
    def __init__(self, pao, recheio, molho):
        self.pao = pao
        self.recheio = recheio
        self.molho = molho
        self.preco = 15


class Pizza:
    def __init__(self, recheio, borda):
        self.borda = borda
        self.recheio = recheio
        self.preco = 20       


class Salgado:
    def __init__(self, massa, recheio):
        self.massa = massa
        self.recheio = recheio
        self.preco = 10


def menu():
    print('- Menu Principal:\n'
          '1. Ver Cardápio.\n'
          '2. Ver pedidos.\n'
          '3. Fechar Pedidos.\n'
          '4. Encerrar Sistema.\n')


def cardapio(tipo):
    if tipo == 'geral':
        print('- Cardápio:\n'
            '1. Pizzas\n'
            '2. Lanches\n'
            '3. Salgados\n'
            '4. Encerrar Pedido.\n')
    if tipo == 'pizza':
        print('#PIZZAS:\n'
            '1. Calabresa\n'
            '2. Mussarela\n'
            '3. Portuguesa\n')
    if tipo == 'lanche':
        print('#LANCHES:\n'
            '1. Hamburger, pão Brioche e molho barbecue\n'
            '2. Hamburger, pão Australiano e maionese caseira da casa\n'
            '3. Hamburger, pão Americano e cebola caramelizada\n')
    if tipo == 'salgado':
        print('#SALGADOS:\n'
            '1. Pastel de carne\n'
            '2. Pastel de queijo\n'
            '3. Coxinha de frango\n')


def insere_opcao(menor, maior):
    opcao = int(input('- Digite uma opção: '))
    while opcao < menor or opcao > maior:
        opcao = int(input('(!) Opção inválida! Tente novamente: '))
    os.system('cls')
    return opcao


if __name__ == '__main__':
    pizza = [
        Pizza('calabresa', 'sim'),
        Pizza('mussarela', 'sim'),
        Pizza('portuguesa', 'sim'),
    ]

    lanche = [
        Lanche('Brioche', 'carne', 'barbecue'),
        Lanche('Australiano', 'carne', 'maionese caseira'),
        Lanche('Americano', 'carne', 'cebola'),
    ]

    salgado = [
        Salgado('pastel', 'queijo'),
        Salgado('pastel', 'carne'),
        Salgado('coxinha', 'frango'),
    ]

    pedidos = []

    print('Bem vindo(a) à Lanchonete Quase Três Lanches!')
    opcao_menu = 0
    while opcao_menu != 4:
        pedido = Pedido()
        menu()
        opcao_menu = insere_opcao(1, 4)

        if opcao_menu == 1:
            opcao_cardapio = 0

            while opcao_cardapio != 4:
                cardapio(tipo='geral')
                print('- Para escolher um prato: ')
                opcao_cardapio = insere_opcao(1, 4)
                if opcao_cardapio == 1:
                    cardapio(tipo='pizza')
                    print('- Para escolher sua pizza: ')
                    opcao_pizza = insere_opcao(1, 4)
                    pedido.itens_consumidos.append(pizza[opcao_pizza-1])
                    print('Pedido adicionado!')
                if opcao_cardapio == 2:
                    cardapio(tipo='lanche')
                    print('- Para escolher seu lanche: ')
                    opcao_lanche = insere_opcao(1, 4)
                    pedido.itens_consumidos.append(lanche[opcao_lanche-1])
                    print('Pedido adicionado!')
                if opcao_cardapio == 3:
                    cardapio(tipo='salgado')
                    print('- Para escolher seu salgado: ')
                    opcao_salgado = insere_opcao(1, 4)
                    pedido.itens_consumidos.append(salgado[opcao_salgado-1])
                    print('Pedido adicionado!')
                print()

            pedido.nome_cliente = input('Para finalizar seu pedido, digite seu nome: ')
            pedido.calcular_total()
            pedidos.append(pedido)
        
        if opcao_menu == 2:
            if len(pedidos) == 0:
                print('Nenhum pedido foi registrado por enquando...!')
                continue
            print('Lista de pedidos:')
            num_pedido = 1
            for p in pedidos:
                print(f'Pedido {num_pedido} - {p.nome_cliente}')
                num_pedido += 1
                num_prato = 1
                for i in p.itens_consumidos:
                    print(f'{num_prato}. {i.__class__.__name__} de {i.recheio}')
                    num_prato += 1
                print()
            print()

        if opcao_menu == 3:
            if len(pedidos) == 0:
                print('Nenhum pedido foi registrado por enquando...!')
                continue
            for p in pedidos:
                p.mostrar_fatura()
                print()
        
        if opcao_menu == 4:
            print('Obrigado por usar o nosso sistema! Até logo o/')
