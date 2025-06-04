print("введите числа ", end ='')
mas = list(map(str, input().split()))
summa= 0
while True:
    k = 0
    for i in range(len(mas)):
        if '-' in mas[i]:
            mas[i]= mas[i].replace('-', '') 
            if mas[i].isdigit() == True:
                summa += -(int(mas[i]))
                k += 1
        elif mas[i].isdigit() == True:
            summa += int(mas[i])
            k += 1
        else:
            break
    if k < len(mas):
        mas = []
        print("введите числа еще раз ", end ='')
        mas = list(map(str, input()))
    else:
        print(summa)
        break
