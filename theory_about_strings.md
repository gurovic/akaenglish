1. Строки в Python задаются кавычками или апострофами с двух сторон. Сначала пишется имя строки (любое слово(а) на английском через “_” c маленькой буквы), а потом ее значение

Пример:
first_string = “Hello,”
second = ‘world!’

2. Чтобы ввести и вывести строки, нужно использовать команды input() и print() соответственно.

Пример:
first_string = input()	#вводите строку, например один два три
second_string = “123”
print(second_string)
print(first_string, second_string)
Программа выведет:
123
один два три 123

3. Так же строки можно складывать и умножать на какое-то число.

Пример:
first_string = “qwerty”
letter = “A”
new_string = first_string + letter
print(letter * 5, new_string)
Программа выведет:
AAAAA qwertyA

4. Длина строки считается командой len().

Пример:
first_string = “qwerty”
print(len(first_string))
Программа выведет:
6

5. У каждого символа строки есть свой номер (индекс). Благодаря этому можно выводить как и отдельные элементы, так и части строки (срезы).
	s[0]	s[1]	s[2]	s[3]	s[4]	s[5]	s[6]	s[7]	s[8]
s	  q	    w	    e	    r	    t	    y	    u	    i	    o
	s[-9]	s[-8]	s[-7]	s[-6]	s[-5]	s[-4]	s[-3]	s[-2]	s[-1]

Пример:
s = “qwertyuio”
print(s[1], s[-5])
print(s[0:5])
Программа выведет:
w t
qwert		#элементы c 0 по 5, т.е фактически с 1 по 4

6. Методы find, count, replace.
find(‘’) – находит данный элемент в строке и выводит его индекс.
count(‘’) – выводит количество данных элементов в строке.
replace(‘’, ‘’) – заменяет все первые элементы на вторые.

Пример:
string = “Python language”
print(string.find(‘l’), string.find(‘p’))
print(string.count(‘n’)
print(string.replace(‘Python’, ‘*’))
print(string.replace(‘’, ‘$’)

Программа выведет:
7 -1	#-1 т.к. символов “p” нет в этой строке
2
* language
$P$y$t$h$o$n$ $l$a$n$g$u$a$g$e$









