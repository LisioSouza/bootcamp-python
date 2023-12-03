#Crie um código declarando as seguintes variáveis do tipo string:

# variáveis do tipo string

nome = 'João da Silva'
cidade = 'São Paulo'
cpf = '123.456.789-00'

# Transforme todos os caracteres das variáveis em maiúsculo

print('Conversão para maiúsculo:')

nome = nome.upper()
cidade = cidade.upper()
print(nome)
print(cidade)
print('')

# Transforme todos os caracteres das variáveis em minúsculo

print('Conversão para minúsculo:')

nome = nome.lower()
cidade = cidade.lower()
print(nome)
print(cidade)
print('')

# Exiba a posição do caractere ã, se presente, em cada uma das variáveis

print(f'A posição da letra "ã" nas palavras é:')
posicao_nome = nome.find('ã')
posicao_cid = cidade.find('ã')
print(f"A letra 'ã' na palavra {nome} está na posição {posicao_nome}")
print(f"A letra 'ã' na palavra {cidade} está na posição {posicao_cid}")
print('')

# Exiba o número de caracteres de cada variável

print('O número de caracteres de cada palavra é:')
nome_caracteres = len(nome)
cidade_caracteres = len(cidade)
print(f'A palavra {nome} tem {nome_caracteres} caracteres')
print(f'A palavra {cidade} tem {cidade_caracteres} caracteres')
print('')

# Remova os pontos (.) e o hífen (–) da variável cpf

cpf = cpf.replace('.', '')
cpf = cpf.replace('-','')
print(f'CPF:{cpf}')
