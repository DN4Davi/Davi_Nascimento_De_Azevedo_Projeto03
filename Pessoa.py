class Pessoa:
    id = 0
    def __init__(self, nome, email):
        self.__id = Pessoa.id
        self.__nome = nome
        self.__email = email
        Pessoa.id += 1

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email
