'''
Variáveis são usadas para salvar algo na memória do computador.
PEP8: inicie váriaveis com letras minúsculas, pode usar números e underline _.
O sinal de = é o operador de atribuição. Ele é usado para atribuir (inserir) um 
valor a um nome (variável)
Uso: nome_variavel = expressao
Obs: Variáveis não pode conter símbolos e nem espaços, apenas caractares,
pode ser usar números também, porém, no meio e no final do nome da variável
mas não no começo.
'''
nome = 'André'
idade = 36
maior_de_idade = idade >= 18

print('Nome:', nome, 'Idade:', idade)
print('É de maior?', maior_de_idade)

if maior_de_idade:
    print(nome, 'é de maior.')
else:
    print(nome, 'é de menor.')