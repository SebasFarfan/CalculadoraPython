from os import remove
from tkinter import *
from turtle import right

root=Tk()
root.title('CALCULADORA')
frame=Frame(root)
frame.config(bg='orange', width=400, height=500)
frame.pack()

operacion=''
resultado=0


# pantalla-----------------------------------
numeroPantalla=StringVar()
pantalla=Entry(frame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=0, columnspan=4, padx=20, pady=20)
pantalla.config(fg='Green', font=('Serif',30), justify='right')
numeroPantalla.set('0')

# ----- tecla pulsada-----------------------------
def numeroPulsado(num):
    global operacion
    if operacion!='':
        numeroPantalla.set(num)
        operacion=''
    elif len(numeroPantalla.get())==0 and num=='0':
        pass
    elif len(numeroPantalla.get())==1 and numeroPantalla.get()=='0' and num!='.':
        numeroPantalla.set(num)
    else:
        numeroPantalla.set(numeroPantalla.get()+num)

# ---------------- convertidor de número---------------
def convertidor(num):
    dato=None
    for conv in (int, float, complex):
        try:
            dato=conv(num)
            break
        except ValueError:
            pass
    return dato

# --------------- boton OFF -------------------------
def apagar():
    root.destroy()

# --------------- operación suma---------------------
def sumar(num):
    global operacion
    global resultado
    dato=convertidor(num)
    if dato!=None:
      resultado+=dato
    else:
      resultado='Error'        
    operacion = 'suma'

    numeroPantalla.set(resultado)


#----------------- funcion el_resultado------------------
def elResultado():
    global resultado
    try:
        numeroPantalla.set(resultado+convertidor(numeroPantalla.get()))          
    except:
      numeroPantalla.set('Error!!')
    
    resultado=0

# --------------------- función delete-------------------------
def borrar():
    if len(numeroPantalla.get())>1 and numeroPantalla.get().isnumeric():
        dato=numeroPantalla.get()
        modificado=dato[0:len(dato)-1]
        numeroPantalla.set(modificado)
    elif (len(numeroPantalla.get())==1 and numeroPantalla.get()=='0'):
        numeroPantalla.set('0')    
    else:
        numeroPantalla.set('0')



# filas de teclado----
# fila de funciones especiales-----------------
botonOff=Button(frame, text='OFF', width=7, font=('Serif', 20), command=lambda:apagar())
botonOff.grid(row=2, column=0)
botonOff=Button(frame, text='AC', width=7, font=('Serif', 20))
botonOff.grid(row=2, column=1)
botonOff=Button(frame, text='C', width=7, font=('Serif', 20))
botonOff.grid(row=2, column=2)
botonOff=Button(frame, text='DEL', width=7, font=('Serif', 20), command=lambda:borrar())
botonOff.grid(row=2, column=3)
# primer fila--------------
boton7=Button(frame, text='7', width=7, font=('Serif', 20), command=lambda:numeroPulsado('7'))
boton7.grid(row=3, column=0)
boton8=Button(frame, text='8', width=7, font=('Serif', 20), command=lambda:numeroPulsado('8'))
boton8.grid(row=3, column=1)
boton9=Button(frame, text='9', width=7, font=('Serif', 20), command=lambda:numeroPulsado('9'))
boton9.grid(row=3, column=2)
botonDivsion=Button(frame, text='/', width=7, font=('Serif', 20))
botonDivsion.grid(row=3, column=3)
# segunda fila-----------------
boton4=Button(frame, text='4', width=7, font=('Serif', 20), command=lambda:numeroPulsado('4'))
boton4.grid(row=4, column=0)
boton5=Button(frame, text='5', width=7, font=('Serif', 20), command=lambda:numeroPulsado('5'))
boton5.grid(row=4, column=1)
boton6=Button(frame, text='6', width=7, font=('Serif', 20), command=lambda:numeroPulsado('6'))
boton6.grid(row=4, column=2)
botonProducto=Button(frame, text='x', width=7, font=('Serif', 20))
botonProducto.grid(row=4, column=3)

# tercera fila-----------------------
boton1=Button(frame, text='1', width=7, font=('Serif', 20), command=lambda:numeroPulsado('1'))
boton1.grid(row=5, column=0)
boton2=Button(frame, text='2', width=7, font=('Serif', 20), command=lambda:numeroPulsado('2'))
boton2.grid(row=5, column=1)
boton3=Button(frame, text='3', width=7, font=('Serif', 20), command=lambda:numeroPulsado('3'))
boton3.grid(row=5, column=2)
botonResta=Button(frame, text='-', width=7, font=('Serif', 20))
botonResta.grid(row=5, column=3)

# cuarta fila-------------------
boton0=Button(frame, text='0', width=16, font=('Serif', 20), command=lambda:numeroPulsado('0'))
boton0.grid(row=6, column=0, columnspan=2)
botonPunto=Button(frame, text='.', width=7, font=('Serif', 20), command=lambda:numeroPulsado('.'))
botonPunto.grid(row=6, column=2)
botonMas=Button(frame, text='+', width=7, font=('Serif', 20), command=lambda : sumar(numeroPantalla.get()))
botonMas.grid(row=6, column=3)

# quinta fila
botonIgual=Button(frame, text='=', width=34, font=('Serif', 20), command=lambda : elResultado())
botonIgual.grid(row=7, column=0, columnspan=4)


root.mainloop()