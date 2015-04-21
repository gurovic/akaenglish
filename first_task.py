from tkinter import *
root=Tk()
root.title('Упражнение 1')
root.geometry('500x500+450+100')
root.resizable(False, False)

def excercise_room_plus():
    global exercise_number
    exercise_number += 1
    room["text"] = exercise_number

    
def excercise_room_minus():
    global exercise_number
    if exercise_number > 1:
        exercise_number -= 1
    else:
        print('error')
    room["text"] = exercise_number
     

exercise_number = 1
title = Label(root, text = "Задание №", font = 'tahoma 14')
room = Label(root, text = exercise_number, font = 'tahoma 18')

button_previous = Button(root, text = '<- Предыдущее', width = 14, height = 1, font = 'tahoma 14', command = excercise_room_minus)
button_next = Button(root, text = 'Следующее ->', width = 13, height = 1, font = 'tahoma 14', command = excercise_room_plus)

title.place(x = 200, y = 15)
room.place(x = 310, y = 11)
button_previous.place(x = 50, y = 440)
button_next.place(x = 300, y = 440)


root.mainloop()
