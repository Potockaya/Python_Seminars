# 1. Напишите программу, удаляющую из текста
# все слова, содержащие ""абв"".

my_str = (input("Введите текст:\n"))
# создаем словарь со значениями и строку, которую будет изменять
replace_values = {"а": "", "б": "", "в": ""}
for i, j in replace_values.items():
    # меняем все my_str на подставляемое
    my_str = my_str.replace(i, j)
# изменяем и печатаем строку
print(my_str)