# Принимает дробь, возвращает первую цифру

num = input('Введите число: ')
#if num == float(num):
for i in range(len(num)):
    if num[i]=='.':
        print(num[i+1])
        break


