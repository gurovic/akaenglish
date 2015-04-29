from tkinter import *
root = Tk()
root.title('Задания по строкам')
root.geometry('500x500+450+100')
root.resizable(False, False)

ts = open('tasks_for_correcting.txt', 'r')
tasks = ts.read()
tasks_parts = tasks.count('----------') + 1
tasks_list = list(map(str, tasks.split('----------'))) 

corrected_texts = [0] * tasks_parts

def end_task(exit_window):
    exit_window.destroy()

def excercise_room_plus():
    global exercise_number
    if exercise_number < tasks_parts:
        exercise_number += 1
        button_ready["bg"] = 'white'
    else:
        exit_window = Tk()
        exit_window.title('Выход')
        exit_window.geometry('250x100+575+210')
        exit_window.resizable(False, False)
        quit_question = Label(exit_window, text = "Вы хотите закончить упражнение?", font = 'tahoma 11')
        quit_yes = Button(exit_window, text = 'Да', width = 5, height = 1, font = 'tahoma 14', command = lambda: end_task(exit_window), fg = 'green')
        quit_no = Button(exit_window, text = 'Нет', width = 5, height = 1, font = 'tahoma 14', command = lambda: end_task(exit_window), fg = 'red')
        quit_question.place(x = 1, y = 5)
        quit_yes.place(x = 55, y = 40)
        quit_no.place(x = 130, y = 40)
        exit_window.mainloop()
        
    room["text"] = exercise_number
    tasks_text.delete('1.0', END)
    tasks_text.insert(1.0, tasks_list[exercise_number - 1])

    
def excercise_room_minus():
    global exercise_number
    if exercise_number > 1:
        exercise_number -= 1
        button_ready["bg"] = 'white'

    room["text"] = exercise_number
    tasks_text.delete('1.0', END)
    tasks_text.insert(1.0, tasks_list[exercise_number - 1])
    
def copy_when_ready():
   button_ready["bg"] = 'grey'
   corrected_text = tasks_text.get('1.0', END)
   corrected_texts[exercise_number - 1] = corrected_text
     
exercise_number = 1
title = Label(root, text = "Задание №", font = 'tahoma 14')
room = Label(root, text = exercise_number, font = 'tahoma 18')
tasks_parts_title = Label(root, text = "из", font = 'tahoma 14')
tasks_parts_label = Label(root, text = tasks_parts, font = 'tahoma 18')

task = Label(root, text = "Исправьте ошибки в программе и,", font = 'tahoma 14')
task_line = Label(root, text = "если нужно, имена переменных.", font = 'tahoma 14')

tasks_text = Text(root, height = 8,width = 53, font = 'Arial 12', wrap = WORD)
tasks_text.insert(1.0, tasks_list[exercise_number - 1])

button_ready = Button(root, text = 'Исправлено!', width = 17, height = 3, font = 'tahoma 14', command = copy_when_ready, bg = 'white')

button_previous = Button(root, text = '<- Предыдущее', width = 14, height = 1, font = 'tahoma 14', command = excercise_room_minus, state = NORMAL)
button_next = Button(root, text = 'Следующее ->', width = 13, height = 1, font = 'tahoma 14', command = excercise_room_plus, state = NORMAL)

title.place(x = 170, y = 15)
room.place(x = 280, y = 11)
tasks_parts_title.place(x = 300, y = 15)
tasks_parts_label.place(x = 330, y = 11)

task.place(x = 90, y = 55)
task_line.place(x = 100, y = 85)
tasks_text.place(x = 8, y = 130)

button_ready.place(x = 160, y = 315)
button_previous.place(x = 50, y = 440)
button_next.place(x = 300, y = 440)

root.mainloop()