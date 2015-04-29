from tkinter import *

class Tests:
    def __init__(self, questions, variants, right_variants):
        self.tests = questions
        self.variants = variants 
        self.right_variants = right_variants
        self.i = 0
    
    def has_next(self):
        if self.i < len(self.tests):
            return True
        return False
    
    
    def get_next(self):
        data = (self.tests[self.i], self.variants[self.i])
        self.i += 1
        return data
    
    def num_of_rights(self, answers):
        num = 0
        for i in range(self.length()):
            if answers.answer(i) == self.right_variants[i]:
                num += 1
        return num 
    
    def show_results(self, answers):
        Label(root, text = 'Результаты', font = 'arial 14' ).place(x = 600, y = 50)
        y_pos = 100
        for i in range(self.length()):
            if answers.answer(i) == self.right_variants[i]:
                Label(root, text = str(i + 1) + " +", font = 'arial 10').place(x = 600, y = y_pos)
            else:
                Label(root, text = str(i + 1) + " -", font = 'arial 10').place(x = 600, y = y_pos)
            y_pos += 20    
    
    def length(self):
        return len(self.tests)
    
    def num_of_question(self):
        return self.i
    
class Answers:
    def __init__(self):
        self.ans = []
        
    def add(self, a):
        self.ans += [a]
            
    def answer(self, i):
        return self.ans[i]
        
   



    
class Wizard:
    def __init__( self, root, tests, answers):
        self.root = root
        self.tests = tests
        self.answers = answers
        win_len = 1000
        win_hi = 600
        win_x = 300
        win_y = 200
        root.title('Тест Python')
        root.geometry('1000x600+300+200')
        root.resizable(False, False)
    
    def next_question(self, answer):
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
        if answer != -1:
            self.answers.add(answer)
        #print(answer)     
        
        if self.tests.has_next():
            data = self.tests.get_next()
            self.show_question(data[0], data[1])
        else:
            self.show_last_window()    
    
    def show_question(self, question, variants):
        self.pretty_text(question) 
        
        btn1 = Button(self.root, text = 'Далее!', width = 10, height = 2, font = 'arial 10',  bg="red", command = lambda: self.next_question(v.get()), state=DISABLED)
        btn1.place(x = 450, y = 500)        
        
        v = IntVar()
        
        for i in range(len(variants)):
            rbutton = Radiobutton(root, text = variants[i], variable = v, value = i + 1, command = lambda: btn1.config(state='normal',  bg="green"))
            rbutton.place(x = 180, y = 300 + i * 20)  
            
        Label(self.root, text = str(self.tests.num_of_question()) + " / " + str(self.tests.length()), font = 'arial 14').place(x = 900, y = 10)    
            
            
        
    def pretty_text(self, pattern):
        y_position = 0  
        string = 0     
        for i in range(len(pattern)):
            if pattern[i] == '&':
                Label(root, text = pattern[string : i], font = 'arial 10').place(x = 180, y = y_position)
                y_position += 20
                string = i + 1
   
    def show_greeting(self):

        w = Label(self.root, text = "Здравствуй! Ты попал на тест по основам программы Python.", font = 'arial 14')
        w1 = Label(self.root, text = "Ответь на заданные вопросы одним словом (или числом) или выбери правильный вариант.", font = 'arial 14')
        btn = Button(self.root, text = 'Начать!', width = 35, height = 5, font = 'arial 25', command = lambda: self.next_question(-1) )
        w.place(x = 180, y = 60)
        w1.place(x = 140, y = 100)
        btn.place(x = 200, y = 300)
        self.root.mainloop()

    
    def show_last_window(self):
        Label(self.root, text = "Тест закончен!", font = 'arial 14').place(x = 180, y = 60)
        num_of_right = self.tests.num_of_rights(self.answers)
        Label(self.root, text = "Верно " + str(num_of_right) + " из " + str(self.tests.length()), font = 'arial 14').place(x = 180, y = 150)
        self.tests.show_results(self.answers)
        Label(self.root, text = 'Cпасибо за внимание!', font = 'arial 14').place(x = 180, y = 240)
        
if __name__=='__main__':
    questions = ['1. Что выведет код ?&s = "Harry"!&print("Hello, "+(s)+"!")&',
                 '2. Что выведет код ?&s = "Harry and Dima!"&print(s.replace("", " ")[1:-1])&',
                 '3. Что выведет код ?&s = Dima!&print(n.find(' '))&',
                 '4. Что выведет код ?&n = 2&b = 0&for i in range(2, n + 1):&   a = n % i&   if a == 0 and b == 0:&      print(i)&      b = 1&',
                 '5. Что выведет код ?&n = 7&for i in range(1, n + 1):&   a = n % i&   if a == 0 :&      print(i)&',
                 '6. Что выведет код ?&n = 15&for i in range(1, n):&   a = i * i&   if a <= n:&      print(a)        &   if n == 1:&      print(1)&',
                 '7. Что выведет код ?&входные данные :&2 2 2 2 2 2 2 2 2 5&a = list(map(int, input().split()))&summa = a[0] + a[1] + a[2] + a[3] + a[4] + a[5] + a[6] + a[7] + a[8] + a[9]&l = 10&for i in range(9):&   if a[i] == 2 and a[i + 1] != 2:&      summa = summa - a[i]&      l = l - 1&print(summa // l)&',
                 '8. Что выведет код ?&входные данные :&1 2 2 3 3 3 4&A = list(map(int, input().split()))&for i in range(len(A)):&   if A[i] % 2 == 0:&      print(A[i], end = " " )&',
                 '9. Что выведет код ?&входные данные :&1 -2 3 -4 5&A = list(map(int, input().split()))&n = 0&for i in range(len(A)):&   if A[i] > 0:&      n = n + 1&print(n)&',
                 '10.  Что выведет код ?&входные данные:&5 -4 3 -2 1&A = list(map(int, input().split()))&min = 1001&for i in range(len(A)):&   if A[i] < min and A[i] > 0:&      min = A[i]&print(min)&',
                 '11. Что выведет код ?&входные данные :&1 2 3 4 5&A = list(map(int, input().split()))&n = 0&for i in range(1,len(A) - 1):&   if A[i] > A[i - 1] and A[i] > A[i + 1]:&      n = n + 1&print(n)&',
                 '12. Что выведет код ?&a = 6&minimum = (a + 1) // 2&for i in range(minimum, a + 1):&   print(i, end = " ")&',
                 '13. Что выведет код ?&входные данные :&5&5 4 3 2 1&a = int(input())&s = list(map(int, input().split()))&for j in range(a - 1):&   for i in range(a - j - 1):&      if s[i] > s[i + 1]:&         s[i], s[i + 1] = s[i + 1], s[i]&for i in range(a):&   print(s[i], end = " ")&',
                 '14. Что выведет код ?&n = 5&a = [None] * (n + 5)&a[0] = 1&a[1] = 1&for i in range (2, n + 1):&   a[i] = a[i - 1] + a[i - 2]&print(a[n - 1])&',
                 '15. Что выведет код ?&n = 4&a = [None] * (n + 5)&a[0] = 1&a[1] = 1&for i in range (2, n + 1):&   a[i] = (a[i - 1] + a[i - 2]) % 10&print(a[n])&',
                 '16. Что выведет код ?&n = 1&a = [None] * (n + 5)&a[0] = 1&a[1] = 2&for i in range (2, n + 1):&   a[i] = a[i - 1] + a[i - 2]&print(a[n])&',
                 '17. Что выведет код ?&n = 3&a = [None] * (n + 5)&a[0] = 1&a[1] = 2&a[2] = 4&for i in range (3, n + 1):&   a[i] = a[i - 1] + a[i - 2] + a[i - 3]&print(a[n])&',
                 '18. Что выведет код ?&N, M = 3 3&arrey = [[0] * (M + 2)]&for i in range(N):&   arrey.append([0] + [1] * M + [0])&arrey.append([0] * (M + 2))&for i in range(1, min(N, M) + 1):&   for j in range(i, M + 1):&      if i*j != 1:&         if arrey[i][j] == 1:&            arrey[i][j] = arrey[i - 1][j] + arrey[i][j - 1]&   for j in range(i + 1, N + 1):&      if arrey[j][i] == 1:&         arrey[j][i] = arrey[j - 1][i] + arrey[j][i - 1]&print(arrey[N][M])&'                 
                 
                 ]
    
    
    
    variants = [['1) Hello, Harry!', '2) Hello, Harry!!', '3) Hello, "Harry!"!', '4) Hello, "Harry!"'],
                ['1) H a r r y   a n d   D i m a !', '2) H a r r y a n d D i m a !', '3) H a r r y  a n d  D i m a !'], 
                ['1) ошибка оформления кода', '2) -1'], 
                ['1) 0', '2) 1', '3) 2'], 
                ['1) 1 7', '2) 1', '3) 7'],
                ['1) 149', '2) 1 4 9', '3) нет правильного варианта'],
                ['1) 2', '2) 5', '3) 22', '4) 25'],
                ['1) 2 4', '2) 224', '3) 2 2 4', '4) ошибка офомления кода'],
                ['1) 5', '2) 1', '3) 3', '4) 2'],
                ['1) 1', '2) -4', '3) 0', '4) ошибка офомления кода'],
                ['1) 1', '2) 2', '3) 0'],
                ['1) 3456', '2) 3 4 5 6', '3) ошибка оформления кода'],
                ['1) 5 4 3 2 1', '2) 12345', '3) 1 2 3 4 5 '],
                ['1) 5', '2) 0', '3) ошибка оформления кода', '4) ничего не выведет'],
                ['1) 4', '2) 5', '3) ошибка оформления кода'],
                ['1) 0', '2) 1', '3) 2'],
                ['1) 2', '2) 7', '3) 8', '4) ошибка оформления кода'],
                ['1) ошибка оформления кода', '2) 3', '3) 4', '4) 6']
                ]
                
    
    
    right_answers = [2, 1, 1, 3, 1, 3, 1, 3, 3, 1, 3, 2, 3, 1, 2, 3, 2, 4]
    user_answers = []
    tests = Tests(questions, variants, right_answers)
    answers = Answers()
    root = Tk()
    gui = Wizard(root, tests, answers)
    gui.show_greeting()
    

    
    
    
    
    
    