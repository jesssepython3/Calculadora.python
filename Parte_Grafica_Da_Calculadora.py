from tkinter import *

age=Tk()
age.geometry('500x500')
age.configure(bg='#599')
age.title("Agenda")

def salva():
    arq=open('agenda.txt', 'a')
    arq.write('Nome: ')
    arq.write(xnome.get())
    arq.write('\n')
    arq.write('Contato: ')
    arq.write(xfone.get())
    arq.write('\n')
    arq.write('\n')
    arq.close()

Label(age,text='Adiciona Nome',).place(x=10,y=10)
xnome=Entry(age)
xnome.place(x=130,y=10)

Label(age,text='Adiciona Telefone',).place(x=10,y=50)
xfone=Entry(age)
xfone.place(x=130,y=50)

Button(age,text='Salvar',command=salva).place(x=10,y=90)


age.mainloop()