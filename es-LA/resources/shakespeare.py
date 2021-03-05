import random
from guizero import App, PushButton, Text

def insultame():
    palabra_a = random.choice(lista_a)
    palabra_b = random.choice(lista_b)
    palabra_c = random.choice(lista_c)
    insulto = "¡Tú " + palabra_a + " " + palabra_b + " " + palabra_c + "!"
return insulto

def nuevo_insulto():
    nuevo_insulto = insultame()
    mensaje.value = nuevo_insulto

lista_a = []
lista_b = []
lista_c = []

with open("insultos.csv", "r") as archivo:
    for linea in archivo:
        palabras = linea.split(",")
        lista_a.append(palabras[0])
        lista_b.append(palabras[1])
        lista_c.append(palabras[2].strip())

app = App("Generador de insultos Shakespearianos")
mensaje = Text(app, insultame() )
boton = PushButton(app, nuevo_insulto, text="Insúltame de nuevo")
app.display()
