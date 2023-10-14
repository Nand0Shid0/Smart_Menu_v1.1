from  tkinter import * 
import PyQt5

window = Tk()
window.geometry('1200x800')


frame_head = Frame(window,bg='blue')
frame_head.pack(side='top')

frame_contenido = Frame(window,bg='red')
frame_contenido.pack(side='left')




window.mainloop()