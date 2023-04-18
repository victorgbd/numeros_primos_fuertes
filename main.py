num = int(input())

n_primo_mayor = 0
n_primo_menor = 0

cont = 0
for i in range(1, num + 1):
    if(num % i == 0):
        cont += 1
if(cont > 2):
    print("no es primo")
else:
    i = num + 1
    while True:
        cont = 0
        for j in range(1, i + 1):
            if(i % j == 0):
                cont += 1
        if(cont == 2):
            n_primo_mayor = i
            break
        i += 1
    i = num - 1
    while True:
        cont = 0
        for j in range(1, i + 1):
            if(i % j == 0):
                cont += 1
        if(cont == 2):
            n_primo_menor = i
            break
        i -= 1
    resul = (n_primo_menor + n_primo_mayor) / 2
    if (resul < num):
        print("es primo fuerte")
    else:
        print("no es primo fuerte")
