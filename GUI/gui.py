from math import comb
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
from tkinter import filedialog as FileDialog
from threading import Thread
import formulas

#Listas utilizadas para las ListView
rango_edades = ["18-30","30-60","60+"]
enfermedades = ["Hipertensión","Síndrome de Cushing","Hipotiroidismo"]
enfermedades_catabolicas = ["Cáncer","SIDA","Quemaduras","Sepsis","Neurológicas"]
enfermedades_agregadas = []
combos = []
sexos = ['Hombre','Mujer']
enfermedades_metabolicas = ['sobrepeso','obesidad','hipertensión','síndrome de Cushing','hipotiroidismo']
alimentos_p_metabolicas = ['alimento 1','alimento 2','alimento 3','alimento 4','alimento 5']
alimentos_permetidos_lista = []
alimentos_prohibidos_lista = []


def agregar_efermedades():
    #agrega las enferedades seleccionadas
    '''
    En la lista de los objetos de tipo listview
    para poder revisar si alguno tiene una opcion
    seleccionada
    '''
    salida_enfermedades.insert(END, '')
    for objeto in combos:
        tmp = objeto.get()
        print(tmp)
        
        if tmp != '':
            if not (tmp in enfermedades_agregadas):
                enfermedades_agregadas.append(tmp)
    print(enfermedades_agregadas)           
    salida_enfermedades.insert(END, enfermedades_agregadas)
    


def calcular():
    peso = P.get()
    altura = T.get()
    edad = combo_edad.current()
    genero = sexo.get()
    activi = float(actividad_var.get())
    imc = formulas.imc(peso, altura)
    get = formulas.geb(edad, peso, genero,activi)
    resultado = f"IMC: {imc}\nGET: {get}"
    output.insert(END, resultado)


def alimentos(enfermedades):
    for enfermedad in enfermedades:
        if enfermedad in enfermedades_metabolicas:
            alimentos_permetidos_lista = alimentos_p_metabolicas
            


# Decoracion
#Creacion de la ventana
root = Tk()
root.title("Proyecto Nutricón")
root.config(bg="black",bd=5)
root.resizable(1, 1)



#Montaje de un frame
frame = Frame(root)
frame.pack()
frame.config(width=1280, height=1580)
frame.config(bg="white")

#Titulo
label = Label(frame, text="Lo Mejor para tu nutrición")
label.config(bg='White', fg='black', font=("Times New Roman", 24))
label.place(x=500, y=2)

# Diseño
nom = Label(frame, text="Datos Del Paciente: ")
nom.config(bg='white', fg='black', font=(" 'Roman'", 20))
nom.place(x=20, y=30)

nom = Label(frame, text="Nombre del paciente ")
nom.config(bg='white', fg='black', font=("Times New Roman", 15))
nom.place(x=70, y=80)

noml = StringVar()
NOMLbol = Entry(frame, textvariable=noml)
NOMLbol.config(bg='white', fg='black', width=15, justify="center", state="normal", font=("Arial Narrow", 12))
NOMLbol.place(x=30, y=120)
NOMLbol.config(width=35)

G = Label(frame, text="Genero ")
G.config(bg='white', fg='black', font=("Arial Narrow", 15))
G.place(x=120, y=150)

sexo = StringVar()
combo_sexo = ttk.Combobox(frame, state="readonly", values=sexos,textvariable=sexo)
combo_sexo.config(width=20, height=20, font=('Arial', 12))
combo_sexo.place(x=60, y=190)

T = Label(frame, text="Talla ")
T.config(bg='white', fg='black', font=("Arial Narrow", 15))
T.place(x=120, y=230)

T = Label(frame, text="Edad: ")
T.config(bg='white', fg='black', font=("Arial Narrow", 15))
T.place(x=340, y=150)
combo_edad = ttk.Combobox(frame, state="readonly", values=rango_edades)
combo_edad.config(width=20, height=20, font=('Arial', 12))
combo_edad.place(x=345, y=189)

T = IntVar()
Tbol = Entry(frame, textvariable=T)
Tbol.config(bg='White', fg='black', width=20, justify="center", state="normal", font=("Arial Narrow", 15))
Tbol.place(x=90, y=270)
Tbol.config(width=12)

P = Label(frame, text="Peso")
P.config(bg='white', fg='black', font=("Arial Narrow", 15))
P.place(x=120, y=320)

P = IntVar()
Pbol = Entry(frame, textvariable=P)
Pbol.config(bg='White', fg='black', width=20, justify="center", state="normal", font=("Arial Narrow", 15))
Pbol.place(x=90, y=360)
Pbol.config(width=11)

IMC = Label(frame, text="IMC ")
IMC.config(bg='white', fg='black', font=("Arial Narrow", 15))
IMC.place(x=125, y=400)


#TextBox
output = Text(frame)
output.config(bg='White', fg='black', width=20,height=6, state="normal", font=("Arial Narrow", 15))
output.place(x=350, y=420)

#Botones de calculo
cimc = Button(frame, text="Calcular IMC", activebackground="green", command=calcular)
cimc.config(width=15, height=2, font=("Arial", 8))
cimc.place(x=90, y=490)

#Enfermedades
T1 = Label(frame, text="Enfermedad: ")
T1.config(bg='white', fg='black', font=("Arial Narrow", 15))
T1.place(x=342, y=230)
combo_enfermedades = ttk.Combobox(frame, state="readonly",values=enfermedades)
combo_enfermedades.config(width=20, height=20, font=('Arial', 12))
combo_enfermedades.place(x=345, y=259)

T1 = Label(frame, text="Enfermedad catabólicas:")
T1.config(bg='white', fg='black', font=("Arial Narrow", 15))
T1.place(x=342, y=300)
combo_enfermedades_catabolicas = ttk.Combobox(frame, state="readonly",values=enfermedades_catabolicas)
combo_enfermedades_catabolicas.config(width=20, height=20, font=('Arial', 12))
combo_enfermedades_catabolicas.place(x=345, y=329)

btn_enfermedades = Button(frame, text='Agregar enfermedad',command=agregar_efermedades)
btn_enfermedades.config(width=15,height=2,font=('Arial',8))
btn_enfermedades.place(x=600,y=259)

'''enfermedades_var = StringVar()
label_enfermedades = Entry(frame, textvariable=enfermedades_var)
label_enfermedades.config(bg='white', fg='black', font=("Arial", 8))
label_enfermedades.place(x=600,y=300)'''

salida_enfermedades = Text()
salida_enfermedades.config(bg='White', fg='black', width=20,height=6, state="normal", font=("Arial", 15))

salida_enfermedades.place(x=600,y=300)

#slider de actividad fisica
label_actividad = Label(frame,text="\% de actividad fisica")
label_actividad.config(bg='white', fg='black', font=("Arial Narrow", 15))
label_actividad.place(x=600,y=400)
actividad_scale = Scale(frame, from_=0.0, to= 100.0, orient=HORIZONTAL)
actividad_scale.set(1)
actividad_scale.place(x=600,y =430)
actividad_var = StringVar()
actividad_entry = Entry(frame,textvariable=actividad_var)
actividad_entry.config(bg='white', fg='black', font=("Arial", 8))
actividad_entry.place(x=600,y=460)

#Despliegue de alimentos
texto = Label(frame, text="Alimentos permitidos")
texto.config(bg='white', fg='black', font=("Arial Narrow", 15))
texto.place(x=750,y=170)
alimentos_permitidos_text = Text(frame)
alimentos_permitidos_text.config(bg='White', fg='black', width=20,height=6, state="normal", font=("Arial", 15))
alimentos_permitidos_text.configure(state=DISABLED)
alimentos_permitidos_text.place(x=750,y=200)

texto = Label(frame, text="Alimentos prohibidos")
texto.config(bg='white', fg='black', font=("Arial Narrow", 15))
texto.place(x=1000,y=170)
alimentos_prohibidos_text = Text(frame)
alimentos_prohibidos_text.config(bg='White', fg='black', width=20,height=6, state="normal", font=("Arial", 15))
alimentos_prohibidos_text.configure(state=DISABLED)
alimentos_prohibidos_text.place(x=1000,y=200)

#Loop para mantener gui abierta
combos = [combo_enfermedades,combo_enfermedades_catabolicas]
root.mainloop()