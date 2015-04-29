from tkinter import *
root=Tk()
root.title('Упражнение 1')
root.geometry('500x500+450+100')
root.resizable(False, False)

th = open('theory_about_strings.txt', 'r')
theory = th.read()
theory_parts = theory.count('----------') + 1
theory_list = list(map(str, theory.split('----------'))) 

def end_task(exit_window):
    exit_window.destroy()
    
def open_tasks(exit_window):
    exit_window.destroy()
    root.destroy()
    import correcting_programm
    execfile('correcting_programm.py')

def excercise_room_plus():
    global exercise_number
    if exercise_number < theory_parts:
        exercise_number += 1
    
    else:
        exit_window = Tk()
        exit_window.title('Выход')
        exit_window.geometry('250x100+575+210')
        exit_window.resizable(False, False)
        quit_question = Label(exit_window, text = "Вы хотите выполнить упражнения", font = 'tahoma 11')
        quit_question_line = Label(exit_window, text = "по изученной теории?", font = 'tahoma 11')
        quit_yes = Button(exit_window, text = 'Да', width = 5, height = 1, font = 'tahoma 14', command = lambda: open_tasks(exit_window), fg = 'green')
        quit_no = Button(exit_window, text = 'Нет', width = 5, height = 1, font = 'tahoma 14', command = lambda: end_task(exit_window), fg = 'red')
        quit_question.place(x = 1, y = 5)
        quit_question_line.place(x = 43, y = 25)
        quit_yes.place(x = 55, y = 50)
        quit_no.place(x = 130, y = 50)
        exit_window.mainloop()
        
    room["text"] = exercise_number
    theory_text.delete('1.0', END)
    theory_text.insert(1.0, theory_list[exercise_number - 1])

    
def excercise_room_minus():
    global exercise_number
    if exercise_number > 1:
        exercise_number -= 1
    room["text"] = exercise_number
    theory_text.delete('1.0', END)
    theory_text.insert(1.0, theory_list[exercise_number - 1])
     

exercise_number = 1
title = Label(root, text = "Теория №", font = 'tahoma 14')
room = Label(root, text = exercise_number, font = 'tahoma 18')
theory_parts_title = Label(root, text = "из", font = 'tahoma 14')
theory_parts_label = Label(root, text = theory_parts, font = 'tahoma 18')

theory_text = Text(root, height = 15,width = 53, font = 'Arial 12', wrap = WORD)
theory_text.insert(1.0, theory_list[exercise_number - 1])

button_previous = Button(root, text = '<- Предыдущее', width = 14, height = 1, font = 'tahoma 14', command = excercise_room_minus)
button_next = Button(root, text = 'Следующее ->', width = 13, height = 1, font = 'tahoma 14', command = excercise_room_plus)

title.place(x = 175, y = 15)
room.place(x = 275, y = 11)
theory_parts_title.place(x = 295, y = 15)
theory_parts_label.place(x = 325, y = 11)

theory_text.place(x = 8, y = 50)
button_previous.place(x = 50, y = 440)
button_next.place(x = 300, y = 440)


root.mainloop()