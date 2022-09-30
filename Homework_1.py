import random

print("Введите n: ")
n = int(input())
number = str(random.randint(1,n))
print("Число загадано! Попробуйте угадать!")

while True:
    print("Введите число: ")
    inp = input()
    my_list = []
    my_list = inp.split(" ")
    
    if "Exit" in my_list:
        break
    if number in my_list:
        print("Вы угадали число! Ответ: ", number)
        break
    else:
        print("Вы не угадали. Попробуйте ещё раз!")
