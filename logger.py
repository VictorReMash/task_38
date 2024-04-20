from data_create import name_data, surname_data, phone_data, address_data
import csv


def input_data():
    list_contacts = [
        name_data().title(),
        surname_data().title(),
        address_data().title(),
    ]

    phone = phone_data()

    if not all(list_contacts):
        print(
            "Ошибка ввода! \n" " 1 - Повторить ввод\n" " 2 - Перейти в главное меню\n"
        )
        commad = input(
            "Выберите действие: ",
        )
        if commad == "2":
            return
        input_data()

    name = list_contacts[0]
    surname = list_contacts[1]
    address = list_contacts[2]

    var = int(
        input(
            f"\nВ каком формате записать данные \n\n"
            f" 1 - вариант: \n"
            f"{name}\n{surname}\n{phone}\n{address}\n\n"
            f" 2 - вариант: \n"
            f"{name} {surname}, {phone}, {address}\n\n"
            f" выберите вариант: "
        )
    )

    while var != 1 and var != 2:
        print("\nНеправильный ввод")
        var = int(input("\nВведите число"))
    if var == 1:
        with open("data_first_variant.csv", "a", encoding="utf-8") as file:
            file.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open("data_second_variant.csv", "a", encoding="utf-8") as file:
            file.write(f"{name};{surname};{phone};{address}\n\n")
        print(f"{name} {surname}, {phone}, {address}")


def print_data():
    print("\nВывод данные из 1 файла: \n")
    with open("data_first_variant.csv", "r", encoding="utf-8") as file:
        data_first = file.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == "\n" or i == len(data_first) - 1:
                data_first_list.append("".join(data_first[j : i + 1]))
                j = i
        print("".join(data_first_list))
    print("\nВывод данныеиз 2 файла: \n")
    with open("data_second_variant.csv", "r", encoding="utf-8") as file:
        data_second = file.readlines()
        print(*data_second)


def save_modified_contact(variant_file, file_name, index_row, index_value, new_value):
    rows = []
    with open(file_name, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        list_reader = list(reader)
        for row in list_reader:
            rows.append(row)
    if index_row < len(rows):
        if variant_file == 2:
            list_cont = rows[index_row][0].split(";")
            list_cont[index_value] = new_value
            rows[index_row][0] = ";".join(list_cont)
        else:
            rows[index_row][index_value] = new_value
        with open(file_name, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
            print("\nИзменения записаны.\n")
    else:
        print(f"Записm с индексом - {index_row}, ненайдена!")


def delete_data_entry(file_name, index_row):
    completion = True
    rows = []
    with open(file_name, "r", newline="", encoding="utf-8") as file:

        reader = csv.reader(file)
        list_reader = list(reader)
        for row in list_reader:
            rows.append(row)

        i = index_row
        while completion:
            if not rows[i]:
                del rows[i]
                completion = False
            else:
                del rows[i]

    with open(file_name, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
        print("\nЗапись удалена.\n")


def search_contact():
    print(
        "Выберите вариант поиска: \n"
        " 1 - Поиск по имени\n"
        " 2 - Поиск по фамилии\n"
        " 3 - Перейти в главное меню\n"
    )
    command = input("Введите номер пункта: ").title()

    count_iter = 1
    while command not in ("1", "2", "3"):
        print("\nНекорректный ввод данных")
        command = input("\nВведите номер пункта: ")

        count_iter += 1
        if count_iter == 2:
            print("\nИсчерпан лимин попыток ввода данных. Программа завершена.")
            return

    ind_var_srch = int(command) - 1
    val_srch = ""

    match command:
        case "1":
            val_srch = input("Введите имя: ").title()
        case "2":
            val_srch = input("Введите фамилию: ").title()
        case "3":
            return

    files = ["data_first_variant.csv", "data_second_variant.csv"]

    for var_file in range(len(files)):
        found = False
        filename = files[var_file]
        with open(files[var_file], "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)

            new_data = []
            data_list = []
            list_contact = []
            segment_step = 0

            if var_file == 1:
                data_list = list(reader)
            else:
                for row in reader:
                    j = reader.line_num
                    if row and row != []:
                        list_contact.append(row[0])
                    else:
                        if segment_step == 0:
                            segment_step = j - 1
                        new_data.extend(list_contact)
                        list_contact.clear()

                for i in range(0, len(new_data), segment_step):
                    data_list.append(new_data[i : i + segment_step])

            index_row = 0
            index_row_spl = 0
            for val in data_list:
                if val is not None and not val:
                    index_row += segment_step + 1
                    continue
                if var_file == 1:
                    val = val[index_row_spl].split(";")
                if val[ind_var_srch].lower() == val_srch.lower():
                    found = True
                    var_file += 1
                    break
                else:
                    index_row += segment_step + 1

        if not found:
            print(f"Ненайдена запись в файле: {filename}\n")
        else:
            print("\nНайдена запись в базе данных:\n")
            print(*val)
            print(
                "\nВыберите действие \n"
                " 1 - Изменить имя\n"
                " 2 - Изменить фамилию\n"
                " 3 - Изменить телефон\n"
                " 4 - Изменить адрес\n"
                " 5 - Удалить контакт\n"
                " 6 - Перейти в главное меню\n"
            )
            command = input(
                "\nВведите номер действия: ",
            )
            count_iter = 0
            index_val = 0
            while command not in ("1", "2", "3", "4", "5", "6"):
                print("\nНекорректный ввод данных")
                command = input("\nВведите номер действия ")
                count_iter += 1
                if count_iter == 2:
                    print("\nИсчерпан лимин попыток ввода данных. Программа завершена.")
                    return
            if int(command) > 1:
                index_val = int(command) - 1
            match command:
                case "1":
                    save_modified_contact(
                        var_file,
                        filename,
                        index_row,
                        index_val,
                        input("\nВведите новое имя: ").title(),
                    )
                case "2":
                    save_modified_contact(
                        var_file,
                        filename,
                        index_row + 1 if var_file == 1 else index_row,
                        index_val,
                        input("\nВведите новую фамилия: ").title(),
                    )
                case "3":
                    save_modified_contact(
                        var_file,
                        filename,
                        index_row + 2 if var_file == 1 else index_row,
                        index_val,
                        input("\nВведите новый номер телефона: "),
                    )
                case "4":
                    save_modified_contact(
                        var_file,
                        filename,
                        index_row + 3 if var_file == 1 else index_row,
                        index_val,
                        input("\nВведите новый адрес: "),
                    )
                case "5":
                    delete_data_entry(filename, index_row)
                    return
                case "6":
                    return
