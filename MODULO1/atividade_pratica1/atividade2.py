# Altere o código da atividade 1 para que ele exiba os números múltiplos de 2, 5 e 7 (simultaneamente) e que estejam dentro do intervalo entre 100 e 500 (incluindo o 100 e o 500).

inicio = 100
fim = 501

multiplos_2 = []
multiplos_5 = []
multiplos_7 = []

for numero in range (inicio, fim):
    if numero % 2 == 0:
        multiplos_2.append(numero)
    if numero % 5 == 0:
        multiplos_5.append(numero)
    if numero % 7 == 0:
        multiplos_7.append(numero)
    
print('Os múltiplos de 2 são:')

for num in multiplos_2:
    print(num)
print('-' * 50)

print('Os múltiplos de 5 são:')
for num in multiplos_5:
    print(num)
print('-' * 50)

print('Os múltiplos de 7 são:')
for num in multiplos_7:
    print(num)
print('-' * 50)
