# На вход принимает 5 чисел и находит максимальное из них.

list = [1, 2, 8, 4, 6]
max = list[0]

for i in range(1, len(list)):
    if list[i]>max:
        max=list[i]

print(max)
 
 


