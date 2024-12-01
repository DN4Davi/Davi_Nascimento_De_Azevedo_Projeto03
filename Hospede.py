from Pessoa import Pessoa


class Hospede(Pessoa):
    def __init__(self, nome, email):
        super().__init__(nome, email)
        self.__reservas = []

    def fazer_reserva(self, reserva):
        if reserva not in self.__reservas:
            self.__reservas.append(reserva)

    def cancelar_reserva(self, reserva):
        self.__reservas = [r for r in self.__reservas if r is not reserva]

    def consultar_reservas(self):
        return self.__reservas
