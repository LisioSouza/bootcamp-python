# Crie um código que realize o somatório de todos os caracteres da string abaixo
# Utilize o laço de repetição for … in; para percorrer cada caractere da string
# Utilize a conversão do tipo string para o tipo inteiro (int(caractere)) para converter os caracteres em valores numéricos;
# Utilize uma variável auxiliar, soma, para acumular o somatório dos valores


numero = '127957' # A soma deverá ser 1 + 2 + 7 + 9 + 5 + 7 = 31

soma = 0


for i in numero:

    soma = sum(int(i) for i in numero)    

print(f'A soma de {" + ".join(numero)} = {soma}')



