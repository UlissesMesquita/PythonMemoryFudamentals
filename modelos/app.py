from restaurante import Restaurante

def main():
    restaurante_ifood = Restaurante("Restaurante ifood", "comun")
    restaurante_lasanha = Restaurante("Restaurante lasanha", "pé sujo")
    restaurante_chique = Restaurante("Restaurante chique", "comum")

    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()



    
