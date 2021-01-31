def sum():
    result = 0
    while True:
        a = input("Введите в строчку числа для сложения. Или 000 для отмены: ").split()
        for i in a:
            if i != "000":
                result+=int(i)
            else:
                print("Error")
                return
        print("Результат равен ", result)

sum()



