first = int(input(f'Введите первое число: '))
second = int(input(f'Введите второе число: '))
third = int(input(f'Введите третье число: '))

if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
