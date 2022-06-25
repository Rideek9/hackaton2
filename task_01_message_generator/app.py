import traceback

import message as msg


def take_a_file():
    name_file = input("Take me a file name\n---> ")
    file = f'{name_file}.csv'
    return file


def open_file(file):
        try:
            with open(file) as my_file:
                line = my_file.readlines()
                return line
        except FileNotFoundError:
            print("Błąd 8877: Taki plik nie istnieje")
            return 0
        except Exception as e:
            e = traceback.format_exc()
            print(e)
            return 0


def verification_list():
    while True:
        student = open_file(take_a_file())
        if student == 0:
            continue
        else:
            return student[1:]
            break


def create_list_student(students):
    student_list = []
    for student in students:
        element = student.rstrip('\n').split(';')
        student_list.append(element)
    return  student_list


def missing_data(student_list):
    missing_data = []
    for index, student in enumerate(student_list):
        try:
            firstname = student[1]
            lastname = student[2]
            missing_task = int(student[3])
            rating = int(student[4])
            email = student[5]
            # msg.message(firstname,lastname,missing_task,rating,email)
        except ValueError:
            missing_data.append(index)

    if len(missing_data)>0:
        with open('missing_data.csv', 'w') as md:
            print('''W pliku wsadowym są brakujące dane, sprawdź i uzupełnij dane\ndla ułatwienia w pliku missing_data.csv pokazane są indeksy z brakującymi danymi''')
            for date in missing_data:
                md.write(f'index nr: {str(date+2)}\n')

    return len(missing_data)


def send_message(missing,student_list):
    if missing == 0:
        for student in student_list:
            print('*'*100)
            firstname = student[1]
            lastname = student[2]
            missing_task = int(student[3])
            rating = int(student[4])
            email = student[5]
            msg.message(firstname,lastname,missing_task,rating,email)
        print('*'* 100)
        print('Wszystkie maile zostały wysłane'.center(100))
        print('*' * 100)


def main():
    students = verification_list()
    student_list = create_list_student(students)
    missing = missing_data(student_list)
    send_message(missing,student_list)


if __name__ == "__main__":
    main()






