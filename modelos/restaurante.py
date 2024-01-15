from avaliacao import Avaliacao
class Restaurante:

    
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome
        self.categoria = categoria.upper()
        self._ativo = False # _ altera o modificador de acesso para privado
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'
        
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Ativo'} \n')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante._ativo}')

    def alternar_estado(self):
        self._ativo = not self._ativo
    
    def avalia_restaurante(self, Avaliacao):
        pass
