print("clases version 2 el constuctor")

class Perro:
    #funcion constructor
    def __init__(self, color, edad):
        self.color=color
        self.edad=edad
        #funciones creadas por el usuario
    def muerde(self):
        print("chale el perro me mordio")
    def chatperro(self,mensaje):
        print(f"chat perro: {mensaje}")
    def chatperra(self,mensajep):
        print(f"chat perro: {mensajep}")
    def datos(self):
        print(f"color {self.color} edad {self.edad}")
#crear el objeto
chihuas=Perro("Negro",2)
#llamas a funciones
chihuas.datos()
chihuas.muerde()
chihuas.chatperro("hola canina")
chihuas.chatperra("hola boby")
chihuas.chatperro("quieres ser mi guggu?")
chihuas.chatperra("grrrruu......")