from functools import partial
from task2 import parse_input

def rotate_matrix(matrix):
    """Поворачивает матрицу на 90 градусов против часовой стрелки."""
    return [list(reversed(col)) for col in zip(*matrix)]

def task3():
    """Выполняет задание 3: Поворот матрицы."""
    print("\nЗадание 3: Поворот матрицы")

    while True:
        try:
            rows = input("Введите количество строк матрицы: ")
            if rows.lower() == 'exit':
                break
            rows = int(rows)

            cols = int(input("Введите количество столбцов матрицы: "))

            matrix = [parse_input(f"Введите элементы строки {i + 1} через пробел: ") for i in range(rows)]
            direction = input("Введите направление поворота (по часовой стрелке/против часовой стрелки): ")

            rotate_function = partial(rotate_matrix, matrix)

            if direction.lower() == "против часовой стрелки":
                matrix = rotate_function()
                matrix = rotate_function()
                matrix = rotate_function()
            elif direction.lower() == "по часовой стрелке":
                matrix = rotate_function()
            else:
                print("Неверное направление поворота.")
                continue

            print("Повернутая матрица:")
            for row in matrix:
                print(" ".join(map(str, row)))

        except ValueError:
            print("Ошибка ввода. Убедитесь, что введены только числа и не оставлено пустых значений.")