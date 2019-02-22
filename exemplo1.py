#POO

class Bolo:
    #pass
    #passa o pass quando não tem nada definido dentro do bloco

    tamanho = 'grande'

    def __init__(self, sabor, cobertura):
                   #instancia, sabor, ...
        self.sabor = sabor
        self.cobertura = cobertura
        #instancia.tamanho = tamanho

    def assar(self):
        print('Bolo está assando')
        return True

    def comer(self):
        pass
    
    def esta_estragado(self):
        pass

bolo1 = Bolo('chocolate', 'chocolate')
#bolo1 é uma instância de Bolo
bolo2 = Bolo('laranja', 'leite condensado')

bolo1.assar()

#print(bolo1.sabor, bolo1.tamanho)

if bolo1.assar():
    print('voce mandou o bolo assar')
else:
    if bolo1.sabor == bolo2.sabor:
        print('Você tem 2 bolos com sabores iguais')
    else:
        print('Você tem 2 bolos com sabores diferentes')