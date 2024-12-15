from task1 import task1
from task2 import task2
from task3 import task3
import threading


def print_menu():
    """Выводит меню с доступными заданиями."""
    print("\nМеню:")
    print("1. Ввод исходных данных")
    print("2. Выполнение алгоритма")
    print("3. Вывод результата")
    print("4. Завершение работы программы")

def main():
    """Основная функция программы, которая управляет выбором задания пользователем."""

    def execute_task(task_function):
        thread = threading.Thread(target=task_function)
        thread.start()
        thread.join()

    tasks = {
        '1': task1,
        '2': task2,
        '3': task3,
    }

    while True:
        print_menu()
        choice = input("Выберите пункт меню: ")

        if choice in tasks:
            execute_task(tasks[choice])
        elif choice == '4':
            print("Завершение работы программы.")
            break
        else:
            print("Неверный выбор.")

        input("Нажмите Enter, чтобы продолжить...")

if __name__ == "__main__":
    main()