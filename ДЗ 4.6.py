#Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#Использовать функцию count() и cycle() модуля itertools.


from itertools import count


for i in count(3):
    if i > 10:
      break
    else:
      print(i, end = ' ' )


from itertools import cycle

c = 0
for el in cycle(input('Введите элемент ')):
    if c > 10:
      break
    print(el)
    c += 1
