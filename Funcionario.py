from Pessoa import Pessoa
from Hotel import Hotel
from Quarto import Quarto
from Hospede import Hospede
from Reserva import Reserva


class Funcionario(Pessoa):
    id = 0
    def __init__(self, nome, email):
        super().__init__(nome, email)

    def add_quarto(self, hotel, quarto):
        hotel.add_quarto(quarto)
        

    def remover_quarto(self, hotel, quarto):
        hotel.remover_quarto(quarto)

    def registrar_hospede(self, hotel, hospede):
        hotel.registrar_hospede(hospede)

    def fazer_reserva(self, hotel, hospede, quarto):
        reserva = Reserva(hospede, quarto)
        hotel.fazer_reserva(reserva)
        return reserva

    def cancelar_reserva(self, hotel, reserva):
        hotel.cancelar_reserva(reserva)
        reserva.get_hospede().cancelar_reserva(reserva)
        reserva.get_quarto().liberar()
