import random
from functools import reduce

def input_large_number_array(prompt):
    """Ввод массива чисел вручную."""
    return list(map(int, input(prompt).split()))

def generate_large_number_array(size):
    """Генерация случайного массива чисел."""
    return [random.randint(0, 9) for _ in range(size)]

def pad_arrays(array1, array2, fill_value=0):
    """Выравнивает длину массивов путем добавления fill_value (по умолчанию 0)."""
    max_length = max(len(array1), len(array2))
    padded1 = array1 + [fill_value] * (max_length - len(array1))
    padded2 = array2 + [fill_value] * (max_length - len(array2))
    return padded1, padded2

def array_operation(array1, array2, operation):
    """Выполняет сложение или вычитание массивов на основе переданной операции."""
    padded1, padded2 = pad_arrays(array1, array2)
    return list(map(operation, padded1, padded2))

def task1_operations(array1, array2, operation_sign):
    """Выполняет операцию сложения или вычитания массивов."""
    operation = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b
    }
    result = array_operation(array1, array2, operation[operation_sign])
    return result

def task1():
    """Меню первого задания."""
    while True:
        print("\nЗадание 1: Сумма двух массивов")
        print("Введите массивы вручную или введите 'exit' для выхода.")

        arr1_input = input("Введите элементы первого массива через пробел: ")
        if arr1_input.lower() == 'exit':
            break
        arr2_input = input("Введите элементы второго массива через пробел: ")

        arr1, arr2 = map(lambda x: list(map(int, x.split())), [arr1_input, arr2_input])

        if len(arr1) != len(arr2):
            print("Массивы должны быть одинакового размера.")
            continue

        arr1.sort(reverse=True)
        arr2.sort()

        result = list(
            map(
                lambda pair: 0 if pair[0] == pair[1] else pair[0] + pair[1],
                zip(arr1, arr2)
            )
        )

        result.sort()
        print("Результат:", result)

def count_subarrays_with_sum(array, target_sum):
    """Подсчитывает количество подмассивов с заданной суммой."""
    subarray_counts = (1 for i in range(len(array)) for j in range(i + 1, len(array) + 1)
                       if sum(array[i:j]) == target_sum)
    return reduce(lambda acc, _: acc + 1, subarray_counts, 0)