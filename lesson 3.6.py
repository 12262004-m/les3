def int_func1():
    a = input("Введите слово: ")
    for i in a:
        if ord(i) >=97 and ord(i) <=122:
            print(a.title())
            return
        else:
            print("Вы ввели слово не латинскими буквами или использовали заглавные буквы!")
            break



int_func1()



def int_func2():
    for i in input("Введите строчку из слов: ").split():
        k = 0
        for j in i:
            if ord(j) >=97 and ord(j) <=122:
                k+=1
                print(i.title() if k==len(i) else "Вы ввели слово не латинскими буквами или использовали заглавные буквы!")



int_func2()

