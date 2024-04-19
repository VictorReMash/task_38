from logger import input_data, print_data, search_contact


def interface(welcome_message=True):
    message = "Выберите команду: \n"
    if welcome_message:
        message = (
            "Добрый день! Вы попали на специальный бот справочник от Geekbrains!\n"
        )
    print(
        f" {message}"
        f" 1 - Запись данных \n"
        f" 2 - Вывод данных \n"
        f" 3 - Поиск и редактироввание данных \n"
        f" 4 - Выход"
    )
    welcome_message = False
    command = input("Введите номер команды ")
    count_iter = 0
    while command not in ("1", "2", "3", "4"):
        print("Неправильный ввод")
        command = input("Введите номер команды: ")
        count_iter += 1
        if count_iter == 2:
            print("Исчерпан лимин попыток ввода данных. Программа завершена.")
            return

    match command:
        case "1":
            input_data()
            interface(welcome_message)
        case "2":
            print_data()
            interface(welcome_message)
        case "3":
            search_contact()
            interface(welcome_message)
        case "4":
            print("До свидания!")
            return
