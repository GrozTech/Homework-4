#Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
#В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
#Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv

wage, hours_w, rate, rpize = argv

hours_w = int(hours_w)
rate = int(rate)
rpize = int(rpize)
print("Расчет заработной платы: ", wage)
print("Часов отработано: ", hours_w)
print("Ставка в час: ", rate)
print("Премия: ", rpize)
print("Вы заработали: ", (hours_w * rate) + rpize)