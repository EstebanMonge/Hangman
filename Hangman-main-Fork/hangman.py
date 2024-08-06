from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random

# Funcion que crea un nuevo juego
def juegoNuevo():
    # Crea dos variables, una con la palabra a adivinar con espacios y otra la cantidad de intentos
    global la_palabra_conEspacios
    global numeroDeIntentos
    numeroDeIntentos =0

    # Escoje una palabra de la lista
    la_palabra=random.choice(lista_palabras)
    # Separa la palabra con espacios
    la_palabra_conEspacios = " ".join(la_palabra)
    # Asigna a la etiqueta la palabra reemplazando letras con guiones bajos
    etiquetaPalabra.set(' '.join("_"*len(la_palabra)))
    imgEtiqueta.config(image="")

# Funcion que tiene la logica para adivinar
def adivinar(letra):
        # Obtiene el numero de intentos
        global numeroDeIntentos
        # Si es menor a 11 otorga un intento
        if numeroDeIntentos<11:
                texto = list(la_palabra_conEspacios)
                adivinado = list(etiquetaPalabra.get())
                if la_palabra_conEspacios.count(letra)>0:
                        for c in range(len(texto)):
                                if texto[c]==letra:
                                        adivinado[c]=letra
                                        ventana.nametowidget("."+letra.lower()).destroy()
                                etiquetaPalabra.set("".join(adivinado))
                                if etiquetaPalabra.get()==la_palabra_conEspacios:
                                        messagebox.showinfo("Ahoracado","Ganaste! =)")
                                        break
                else:
                        numeroDeIntentos += 1
                        imgEtiqueta.config(image=fotos[numeroDeIntentos])
                        if numeroDeIntentos==11:
                                        messagebox.showwarning("Ahocado","Perdiste =(")


#Crear la ventana principal y agregar un  titulo
ventana = Tk()
ventana.title('Ahorcado')

#Lista de palabras a adivinar
lista_palabras= ['PUNTARENAS','SANJOSE','LIMON','ALAJUELA','HEREDIA','GUANCASTE']

#Se crea una lista con todas las imagenes que dibujan el ahorcado
fotos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"),
PhotoImage(file="images/hang3.png"), PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"),
PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"), PhotoImage(file="images/hang8.png"),
PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]

#Se crea el espacio donde se dibuja el ahorcado
imgEtiqueta=Label(ventana)
imgEtiqueta.grid(row=0, column=0, columnspan=3, padx=10, pady=40)


#Se crea el espacio donde se dibuja los espacios con las letras de la palabra a adivinar
etiquetaPalabra = StringVar()
Label(ventana, textvariable  =etiquetaPalabra,font=('consolas 24 bold')).grid(row=0, column=3 ,columnspan=6,padx=10)

#Crea la butonera con todos las letras
#Cada vez que se oprime una letra llama a la función adivinar
n=0
for c in ascii_uppercase:
    Button(ventana, name=c.lower(), text=c, command=lambda c=c: adivinar(c), font=('Helvetica 18'), width=4).grid(row=1+n//9,column=n%9)
    n+=1

#Crea el botón de juego nuevo
Button(ventana, text="Juego\nnuevo", command=lambda:juegoNuevo(), font=("Helvetica 10 bold")).grid(row=3, column=8)
# Inicializa el juego
juegoNuevo()
ventana.mainloop()
