# Execute e analise a saída do seguinte código

nomes = ['Maria', 'Julieta', 'Fernando', 'Cristiano', 'Julieta', 'Maria', 'Fernando', 'Cláudio']

qtd_letras = {}

for nome in nomes:
    qtd_letras[nome] = len(nome)
    
print(qtd_letras)