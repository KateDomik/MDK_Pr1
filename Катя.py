from tkinter import *
import re

def check_triangle():
    x = int(entry1.get())
    y = int(entry2.get())
    z = int(entry3.get())

    if x != 0 and y != 0 and z !=0:
        result_label.config(text="Введите не нулевые значения")
        if x == y == z:
            result_label.config(text="Это равносторонний треугольник")
        if x < y+z or y < x+z or z < x+y:
            result_label.config(text="Треугольник не существует")
        if x == y or y == z or x == z:
            result_label.config(text="Это равнобедренный треугольник")
        else:
            result_label.config(text="Это разносторонний треугольник")
    else:
        result_label.config(text="Введите не нулевые значения")
def is_valid(newval):
    return re.match("^\d{0,4}$", newval) is not None

# Создаем окно
window = Tk()
window.geometry('550x320')
window['bg'] = '#00BFFF'

check = (window.register(is_valid), "%P")

label = Label(window, text="Введите длины сторон треугольника", font="TkHeadingFont 20", bg='#00BFFF', fg="white")
label.pack()
label = Label(window, text="Числа должны содержать до 4 знаков", font="TkHeadingFont 10", bg='#00BFFF', fg="white")
label.pack()
lab1 = Label(window, fg="#00BFFF", bg="#00BFFF")
lab1.pack()
# Создаем поля для ввода
entry1 = Entry(window, font="TkHeadingFont 15", fg="black", bg="white", validate="key", validatecommand=check)
entry1.pack()
lab1 = Label(window, fg="#00BFFF", bg="#00BFFF")
lab1.pack()
entry2 = Entry(window, font="TkHeadingFont 15", fg="black", bg="white", validate="key", validatecommand=check)
entry2.pack()
lab1 = Label(window, fg="#00BFFF", bg="#00BFFF")
lab1.pack()
entry3 = Entry(window, font="TkHeadingFont 15", fg="black", bg="white", validate="key", validatecommand=check)
entry3.pack()
lab1 = Label(window, fg="#00BFFF", bg="#00BFFF")
lab1.pack()
# Кнопка для проверки
check_button = Button(window, text="Проверить", fg="black", bg="#FFFF00", width=30, height=2, command=check_triangle)
check_button.pack()
lab1 = Label(window, fg="#00BFFF", bg="#00BFFF")
lab1.pack()
# Место для вывода результата
result_label = Label(window, text="", font="TkHeadingFont 12", fg="black", bg="#00BFFF")
result_label.pack()

# Запуск приложения
window.mainloop()