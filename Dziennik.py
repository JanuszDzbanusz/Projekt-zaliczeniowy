import os
import random

print('''Welcome to Student Management System App!
Options:
[1]: Show the list of students
[2]: Add new student
[3]: Searching for student
[4]: Deleting student
[5]: Change student information
[6]: Quit''')

with open("Dziennik.txt", "r+") as file:
    while True:
        option_num = input("Select desired option by entering its number(1-6): ")
        file.seek(0)  # byc moze niepotrzbne
        if os.path.getsize("Dziennik.txt") != 0:  # puste linie w pliku to tez zawartosc. Usun problem pustej linii
            ID_list = [line[-6:-1] for line in file]

        match option_num:
            case '1':
                print("\nList of added students: ")
                file.seek(0)
                for index, line in enumerate(file, 1):
                    line = line.split()
                    print(f"{index}. {' '.join([line[0], line[1]])}:\n"
                          f"Class: {line[2]}\n"
                          f"Phone number: {line[3]}\n"
                          f"ID: {line[4]}")
            case '2':
                Name = input("Enter name: ")
                Surname = input("Enter Surname: ")
                Class = input("Enter Class: ")
                Ph_Number = input("Enter phone number: ")
                ID = str(random.randint(10000, 99999))
                while ID in ID_list:
                    ID = str(random.randint(10000, 99999))
                file.write('\n' + ' '.join([Name, Surname, Class, Ph_Number, ID]))
                ID_list.append(ID)
            case '3':
                ID_to_find = input("Enter ID: ")
                file.seek(0)
                for line in file:
                    if ID_to_find in line:
                        line = line.split()
                        print(f"{' '.join([line[0], line[1]])}:\n"
                              f"Class: {line[2]}\n"
                              f"Phone number: {line[3]}\n"
                              f"ID: {line[4]}")
                        break
            case '4':
                ID_to_find = input("Enter ID: ")
                file.seek(0)
                line_list = [line for line in file]
                file.seek(0)
                file.truncate(0)
                for line in line_list:
                    if ID_to_find not in line:
                        file.write(line)
            case '5':
                ID_to_find = input("Enter ID: ")
                file.seek(0)
                line_list = []
                for line in file:
                    if ID_to_find in line:
                        option = int(input('''Which information would u like to change?:
[1] Name
[2] Surname
[3] Class
[4] Phone number
Input: '''))
                        change = input("Enter new information: ")
                        line = line.split()
                        line[-1] += '\n'
                        line[option - 1] = change
                        line = " ".join(line)
                    line_list.append(line)

                file.seek(0)
                file.truncate(0)
                for line in line_list:
                    file.write(line)
            case '6':
                break
            case _:
                print("Your choice does not match any of available options. Please try again")
                continue
