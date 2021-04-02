#Представлен список чисел. Необходимо вывести элементы исходного списка,
#значения которых больше предыдущего элемента.


original_l = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f"Исходный список: {original_l}")

new_l = [original_l[i] for i in range(1, len(original_l)) if original_l[i] > original_l[i-1]]
print(('Результат:'),new_l)