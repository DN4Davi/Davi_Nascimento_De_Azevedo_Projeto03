class Reserva:
    def __init__(self, hospede, quarto):
        self.__hospede = hospede
        self.__quarto = quarto

    def get_hospede(self):
        return self.__hospede

    def get_quarto(self):
        return self.__quarto
