def information(name, surname, date_of_birth, city, e_mail, telephone):
    print("Имя: ", name, ", фамилия: ", surname, ", дата рождения: ", date_of_birth, ", город проживания: ", city, ", e-mail: ", e_mail, ", номер телефона: ", telephone)

information(name = input("Введите ваше имя: "), surname = input("Введите вашу фамилию: "), date_of_birth=input("Введите вашу дату рождения: "), city = input("Введите ваш город проживания: "), e_mail=input("Введите ваш e-mail: "), telephone=input("Введите ваш номер телефона: "))