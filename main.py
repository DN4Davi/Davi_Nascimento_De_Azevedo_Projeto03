from Funcionario import Funcionario
from Hospede import Hospede
from Quarto import Quarto
from Hotel import Hotel

funcionario = Funcionario("João", "joao@hotel.com")
print(f"funcionario {funcionario.get_id()} criado")

hospede = Hospede("Renato", "renato@hospede.com")
print(f"hospede {hospede.get_id()} criado")

hospede_1 = Hospede("Luide", "luide@hospede.com") # Alterado após a gravação
print(f"hospede {hospede_1.get_id()} criado")

quarto = Quarto(12, "Suite")
print(f"quarto {quarto.get_numero()} criado")

quarto_1 = Quarto(41, "Comum") # Alterado após a gravação
print(f"quarto {quarto_1.get_numero()} criado")

hotel = Hotel()
print("Hotel criado")

funcionario.registrar_hospede(hotel, hospede)
assert hospede in hotel.get_hospedes()

funcionario.registrar_hospede(hotel, hospede_1)
assert hospede_1 in hotel.get_hospedes()

funcionario.add_quarto(hotel, quarto)
assert quarto in hotel.get_quartos()

funcionario.remover_quarto(hotel, quarto)
assert quarto not in hotel.get_quartos()

funcionario.add_quarto(hotel, quarto_1)
assert quarto_1 in hotel.get_quartos()

reserva = funcionario.fazer_reserva(hotel, hospede, quarto_1)
assert reserva in hotel.get_reservas()

funcionario.cancelar_reserva(hotel, reserva)
assert reserva not in hotel.get_reservas()
