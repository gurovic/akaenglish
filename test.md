 1. Cтроки.
    1. Что выведет код ?
     
     s = "Harry!"
     print("Hello, "+(s)+"!")
       1. Hello, Harry!
       2. Hello, Harry!!                                    +
       3. Hello, "Harry!"!
       4. Hello, "Harry!"
       
     2. Что выведет код ?
    
     s = "Harry and Dima!"
     print(s.replace('', ' ')[1:-1])
    
       1. H a r r y   a n d   D i m a !                     +
       2. H a r r y a n d D i m a !
       3. H a r r y  a n d  D i m a !
       
     3. Что выведет код ?
     
     s = Dima!
     print(n.find(' '))
     
       1. ошибка оформления кода                            +
       2. -1
       
  2. Цикл while.
  
     1. Что выведет код ?
     
     n = 2
     b = 0
     for i in range(2, n + 1):
         a = n % i
         if a == 0 and b == 0:
             print(i)
             b = 1
             
       1. 0                                             
       2. 1
       3. 2                                                    +

     2. Что выведет код ?
     
     n = 7
     for i in range(1, n + 1):
         a = n % i
         if a == 0 :
             print(i)
             
       1. 1 7                                                  +
       2. 1
       3. 7
       
     3. Что выведет код ?  
     
     n = 15
     for i in range(1, n):
         a = i * i
         if a <= n:
             print(a)        
     if n == 1:
         print(1)
        
       1. 1
          4                                                     +
          9
       2. 1 4 9
       
  3. Cписки.
       
     1. Что выведет код ? 
     
     входные данные :
     2 2 2 2 2 2 2 2 2 5
      
     a = list(map(int, input().split()))
     summa = a[0] + a[1] + a[2] + a[3] + a[4] + a[5] + a[6] + a[7] + a[8] + a[9]
     l = 10
     for i in range(9):
         if a[i] == 2 and a[i + 1] != 2:
             summa = summa - a[i]
             l = l - 1
     print(summa // l)
     
       1. 2                                                                      +
       2. 5
       3. 22
       4. 25
       
  4.  for element in (list).
    
     1. Что выведет код ? 
    
     входные данные :
     1 2 2 3 3 3 4
    
     A = list(map(int, input().split()))
     for i in range(len(A)):
         if A[i] % 2 == 0:
             print(A[i], end = " " )
            
       1. 2 4
       2. 224
       3. 2 2 4                                                                   +
       4. ошибка офомления кода
       
     2. Что выведет код ?  
     
     входные данные :
     1 -2 3 -4 5
     
     A = list(map(int, input().split()))
     n = 0
     for i in range(len(A)):
         if A[i] > 0:
             n = n + 1
     print(n)
     
       1. 5
       2. 1
       3. 3                                                                        +
       4. 2
       
     3.  Что выведет код ?
     
     входные данные:
     5 -4 3 -2 1

     A = list(map(int, input().split()))
     min = 1001
     for i in range(len(A)):
         if A[i] < min and A[i] > 0:
             min = A[i]
     print(min)
     
       1. 1                                                          +
       2. -4
       3. 0 
       4. ошибка офомления кода
       
  5. for ... in range(...).
  
     1. Что выведет код ?
     
     входные данные :
     1 2 3 4 5

     A = list(map(int, input().split()))
     n = 0
     for i in range(1,len(A) - 1):
         if A[i] > A[i - 1] and A[i] > A[i + 1]:
             n = n + 1
     print(n)
       1. 1
       2. 2
       3. 0                                                +
       
     2. Что выведет код ?
    
     a = 6
     minimum = (a + 1) // 2
     for i in range(minimum, a + 1):
         print(i, end = " ")
     
         1. 3456  
         2. 3 4 5 6                                                  +
         3. ошибка оформления кода
         
  6. Двумерный массив.
  
     1. Что выведет код ?
     
     n = 2
     for i in range(n):
         print("0 " *(n - 1 - i) + "1 " + "2 " * i)
         
         1. 01
            12
         2. 1 2
            2 3
         3. 0 1                                                       +
            1 2                
       
  7. Квадратичные сортировки.
  
     1. Что выведет код ?
     
     входные данные :
     5
     5 4 3 2 1
     
     a = int(input())
     s = list(map(int, input().split()))
     for j in range(a - 1):
         for i in range(a - j - 1):
             if s[i] > s[i + 1]:
                 s[i], s[i + 1] = s[i + 1], s[i]
     for i in range(a):
         print(s[i], end = " ")

         1. 5 4 3 2 1
         2. 12345 
         3. 1 2 3 4 5                                                              +
         
  8.  Рекуррентные последовательности.
  
     1. Что выведет код ?
      
     n = 5
     a = [None] * (n + 5)
     a[0] = 1
     a[1] = 1
     for i in range (2, n + 1):
         a[i] = a[i - 1] + a[i - 2]
     print(a[n - 1])
     
         1. 5                                                                    +
         2. 0
         3. ошибка оформления кода
         4. ничего не выведет
         
     2. Что выведет код ?
      
     n = 4
     a = [None] * (n + 5)
     a[0] = 1
     a[1] = 1
     for i in range (2, n + 1):
         a[i] = (a[i - 1] + a[i - 2]) % 10
     print(a[n])
     
         1. 4
         2. 5                                                 +
         3. ошибка оформления кода
         
  9. Одномерное динамическое программирование.
  
     1. Что выведет код ?
     
     n = 1
     a = [None] * (n + 5)
     a[0] = 1
     a[1] = 2
     for i in range (2, n + 1):
         a[i] = a[i - 1] + a[i - 2]
     print(a[n])
     
         1.0
         2. 1
         3. 2                                                         +
         
     2. Что выведет код ?
     
     n = 3
     a = [None] * (n + 5)
     a[0] = 1
     a[1] = 2
     a[2] = 4
     for i in range (3, n + 1):
         a[i] = a[i - 1] + a[i - 2] + a[i - 3]
     print(a[n])
     
         1. 2
         2. 7                                                                        +
         3. 8
         4. ошибка оформления кода
         
  10. Двумерное динамическое программирование.      
  
     1. Что выведет код ?
     
     N, M = 3 3
     arrey = [[0] * (M + 2)]
     for i in range(N):
         arrey.append([0] + [1] * M + [0])
     arrey.append([0] * (M + 2))
     for i in range(1, min(N, M) + 1):
         for j in range(i, M + 1):
             if i*j != 1:
                 if arrey[i][j] == 1:
                     arrey[i][j] = arrey[i - 1][j] + arrey[i][j - 1]
         for j in range(i + 1, N + 1):
             if arrey[j][i] == 1:
                 arrey[j][i] = arrey[j - 1][i] + arrey[j][i - 1]
     print(arrey[N][M])
     
         1. ошибка оформления кода
         2. 3
         3. 4
         4. 6                                                                       +
         
  11. Геометрия.
  
     1. Что ищет программа ?
     
     входные данные :
     1 1 2 4 3 2
     
     class Point:
   
         def __init__(self, x, y):
             self.x = x
             self.y = y
     class Vector:
   
         def __init__(self, first, second):
             if type(first) == Point:
                 self.x = second.x - first.x
                 self.y = second.y - first.y
             else:
                 self.x = first
                 self.y = second
           
         def __pow__(self, other):
             return self.x * other.y - other.x * self.y
       
     def square(self, second, third):
          return abs(Vector (first, second) ** Vector(first, third)) / 2
 
     first = Point(0, 0)
     second = Point(0, 0)
     third = Point(0, 0)
     first.x, first.y, second.x, second.y, third.x, third.y = map(int,input().split())
 
     print(square(first, second, third))

         1. Площадь
         2. Точку пересечения медиан
         3. Точку пересечения высот
         4. площадь иногоугольника

    


      
             
       
