class Pessoa:
    classe = 'mamifero'

    def __init__(self, nome, cor_olhos):
        self.nome = nome
        self.cor_olhos = cor_olhos
    
    def cadastrar(self):
        print(f'{self.nome} foi cadastrado no sistema')
    
    def excluir(self):
        print(f'{self.nome} foi excluído do sistema')

    def atualizar_nome(self, novo_nome):
        self.nome = novo_nome
        print(f'O nome foi atualizado. Agora é: {self.nome}')

class Crianca(Pessoa):
    #vai herdar todos os atributos da classe Pessoa
    def __init__(self, desenho_favorito, brinquedo_favorito, nome, cor_olhos):
        self.desenho_favorito = desenho_favorito
        self.brinquedo_favorito = brinquedo_favorito
        Pessoa.__init__(nome, cor_olhos)

henrique = Crianca('Boleto', 'azul', 'grisalho', 'vermelho', 0.50)
print(henrique.nome, henrique.altura)

fulano = Pessoa('João', 'castanhos', 'azul', 'amarelo', 1.97)
cicrano = Pessoa('Creisson', 'verde', 'preto', 'preto', 1.40)
henrique = Crianca()

cicrano.atualizar_nome('Vitoria')
print(cicrano.nome)

