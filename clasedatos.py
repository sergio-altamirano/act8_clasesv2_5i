class informacion:
    
    def mi_lista(self):
        lista_nomperros=["boby", "dollar", "fany"]
        for x in lista_nomperros:
            print(x)

    def mi_tupla(self):
            tupla_gatos=("pelusa", "bola de nieve", "campanita")
            for x in tupla_gatos:
                print(x)

    def mi_conjunto(self):
            conjunto_rasasdeperro={"chihuaha", "pitbull", "pug"}
            for x in conjunto_rasasdeperro:
                print(x)

    def mi_diccionario(self):
            diccionario_tamañosdeperros={
                "perro 1: " : "chiquito",
                "perro 2: " : "mediano",
                "perro 3: " : "grandote"
            }
            for x, y in diccionario_tamañosdeperros.items():
                print(x, y)

            #creando el objeto

datos=informacion()
print("------------------------------------------------------")
print("listado de nombres de perros")
datos.mi_lista()
print("------------------------------------------------------")
print("tupla de nombres de gatos")
datos.mi_tupla()
print("------------------------------------------------------")
print("conjunto de rasas de perros")
datos.mi_conjunto()
print("------------------------------------------------------")
print("diccionario de tamaños de perros")
datos.mi_diccionario()
print("------------------------------------------------------")