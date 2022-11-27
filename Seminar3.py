# На вход принимает число n, и выводит все числа от -n до n.

print('Введите число n')
a = int(input())

for i in range(-a, a+1):
    print(i, end=" ")