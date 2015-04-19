from tkinter import *

class Questions:
    def __init__(self, q, v, r_v):
        self.q = q
        self.v = v 
        self.r_v = r_v
        self.i = 0
    
    def has_next(self):
        if self.i < len(self.q):
            return True
        return False
    
    
    def get_next(self):
        data = (self.q[self.i], self.v[self.i])
        self.i += 1
        return data

    
class Answers:
    def __init__(self):
        self.ans = []
        
    def add(self, a):
        self.ans += [a]



    
class Gui:
    def __init__( self, root, q):
            self.root = root
            self.q = q
            win_len = 1000
            win_hi = 600
            win_x = 300
            win_y = 200
            root.title('Тест Python')
            root.geometry('1000x600+300+200')
            root.resizable(False, False)
    
    def next_question(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
        if self.q.has_next():
            data = self.q.get_next()
            self.show_question(data[0], data[1])
        else:
            self.show_last_window()    
    
    def show_question(self, question, variants):
         
        btn1 = Button(self.root,text='Далее!',width=10, height=2, font='arial 10', command = self.next_question )
        btn1.place(x = 450, y = 500)
        w = Label(root, text= self.pretty_text(question))
        var=IntVar()
        for i in range(len(variants)):
            rbutton=Radiobutton(root,text=variants[i],variable=var,value=i)
            rbutton.place(x = 180, y = 100 + i * 20)
        #rbutton2=Radiobutton(root,text=variants[1],variable=var,value=2)
        #rbutton3=Radiobutton(root,text=variants[2],variable=var,value=3)
        #rbutton4=Radiobutton(root,text=variants[3],variable=var,value=4)
        
        #rbutton2.place(x = 180, y = 120)
        #rbutton3.place(x = 180, y = 140)
        #rbutton4.place(x = 180, y = 160)
        w.place()
        a.add(var)
        
    def pretty_text(self, pattern):
        y_ = 0  
        j = 0     
        for i in range(len(pattern)):
            if pattern[i] == '&':
                Label(root, text=pattern[j:i], font = 'arial 10').place(x = 180, y = y_)
                y_ += 20
                j = i + 1
   
    def show_greeting(self):

        w = Label(self.root, text="Здравствуй! Ты попал на тест по основам программы Python.", font = 'arial 14')
        w1 = Label(self.root, text="Ответь на заданные вопросы одним словом (или числом) или выбери правильный вариант.", font = 'arial 14')
        btn = Button(self.root,text='Начать!',width=35, height=5, font='arial 25', command = self.next_question )
        w.place(x = 180, y = 60)
        w1.place(x = 140, y = 100)
        btn.place(x = 200, y = 300)
        self.root.mainloop()

    
    def show_last_window(self):
        w = Label(self.root, text="досвидос", font = 'arial 14')
        #result = ''.join(a)
       # w1 = Label(self.root, text=result, font = 'arial 14')
        
        w.place(x = 180, y = 60)
        #w1.place(x = 180, y =200)

if __name__=='__main__':
    questions = [['1. Что выведет код ?&s = "Harry"!&print("Hello, "+(s)+"!")]&'], ['2. Что выведет код ?&s = "Harry and Dima!"&print(s.replace('', ' ')[1:-1])&']]
    variants = [['1. Hello, Harry!', '2. Hello, Harry!!', '3. Hello, "Harry!"!', '4. Hello, "Harry!"'], ['1. H a r r y   a n d   D i m a !', '2. H a r r y a n d D i m a !', '3. H a r r y  a n d  D i m a !']]
    right_answers = [2, 1, 1, 3, 1, 1, 1, 3, 3, 1, 3, 2, 3, 3, 1, 2, 3, 2, 4]
    user_answers = []
    q = Questions(questions, variants, right_answers)
    a = Answers()
    root = Tk()
    gui = Gui( root, q)
    gui.show_greeting()
    

    
    
    
    
    
    
