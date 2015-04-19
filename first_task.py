from tkinter import *
root=Tk()
root.title('Упражнение 1')
root.geometry('500x500+500+200')
root.resizable(False, False)

w = Label(root, text="Задание №", font = 'arial 14')


button_previous = Button(root,text='<- Предыдущее',width=12, height=2, font='arial 15', command = w.destroy )
button_next = Button(root,text='Следующее ->',width=12, height=2, font='arial 15', command = w.destroy )

w.place(x = 200, y = 30)


button_previous.place(x = 50, y = 400)
button_next.place(x = 300, y = 400)


root.mainloop()
