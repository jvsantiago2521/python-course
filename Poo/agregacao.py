class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])
    
    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
            print()

    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()
p1, p2 = Produto("Leite", 12), Produto("Macarrao", 36)
p3 = Produto("Ovo", 22)

carrinho.inserir_produtos(p1, p2, p3)
carrinho.listar_produtos()
