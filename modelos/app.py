from restaurante import Restaurante


restaurante_praca = Restaurante("Gui", "Gourmet")
restaurante_praca.receber_avaliacao("Gui", 10)

def main():    
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()



    
