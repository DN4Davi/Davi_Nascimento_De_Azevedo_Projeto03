class Quarto:
    def __init__(self, numero, tipo):
        self.__numero = numero
        self.__tipo = tipo
        self.__disponivel = True

    def get_numero(self):
        return self.__numero

    def get_tipo(self):
        return self.__tipo

    def reservar(self):
        self.__disponivel = False

    def liberar(self):
        self.__disponivel = True

    def esta_disponivel(self):
        return self.__disponivel
