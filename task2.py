from functools import partial
from itertools import starmap


def parse_input(prompt):
    """Парсинг пользовательского ввода в список чисел."""
    return list(map(int, input(prompt).split()))


def check_sums(arr1, arr2, arr3):
    """Проверка условия суммы массивов."""
    return (arr1 + arr2 == arr3) * ((arr1 + arr2 + arr3) ** min(arr1, arr2, arr3))


def task2():
    """Меню второго задания."""
    print("\nЗадание 2: Проверка сумм трёх массивов")

    while True:
        array_input_1 = input("Введите элементы первого массива через пробел: ")
        if array_input_1.lower() == 'exit':
            break

        try:
            arr1 = parse_input("Введите элементы второго массива через пробел: ")
            arr2 = parse_input("Введите элементы третьего массива через пробел: ")

            arrays = list(map(parse_input, [array_input_1, array_input_2, array_input_3]))

            if any(len(arr) != len(arrays[0]) for arr in arrays):
                print("Все массивы должны быть одинакового размера.")
                continue

            results = list(filter(None, starmap(check_sums, zip(*arrays))))

            print("Результаты:", results)

        except ValueError:
            print("Ошибка ввода. Убедитесь, что введены только числа.")

