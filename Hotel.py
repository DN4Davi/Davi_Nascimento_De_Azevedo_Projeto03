class Hotel:
    def __init__(self):
        self.__hospedes = []
        self.__quartos = []
        self.__reservas = []

    def add_quarto(self, quarto):
        if quarto not in self.__quartos:
            self.__quartos.append(quarto)

    def remover_quarto(self, quarto):
        self.__quartos = [q for q in self.__quartos if q is not quarto]

    def registrar_hospede(self, hospede):
        if hospede not in self.__hospedes:
            self.__hospedes.append(hospede)

    def fazer_reserva(self, reserva):
        if reserva.get_hospede() not in self.get_hospedes():
            raise Exception("Hospede não registrado")
        if reserva.get_quarto() not in self.get_quartos():
            raise Exception("Quarto não encontrado")
        if reserva.get_quarto().esta_disponivel() is False:
            raise Exception("Quarto está ocupado")
        if reserva not in self.__reservas:
            reserva.get_hospede().fazer_reserva(reserva)
            reserva.get_quarto().reservar()
            self.__reservas.append(reserva)

    def cancelar_reserva(self, reserva):
        self.__reservas = [r for r in self.__reservas if r is not reserva]

    def get_hospedes(self):
        return self.__hospedes

    def get_reservas(self):
        return self.__reservas

    def get_quartos(self):
        return self.__quartos
