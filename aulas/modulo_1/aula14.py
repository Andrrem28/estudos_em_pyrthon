# Formatações, usando a função format()
num_1 = 1
num_2 = 2
num_3 = 3
# Exemplo criado para mostrar de forma sequêncial, de acordo com os argumentos
# declarados na função format. Caso não use nenhum íncide, ele irá exibir os resultados
# de acordo com a sequência dos argumentos da função.
string_1 = 'Número 1 = {}, Número 2 = {}, Número 3 = {}'
formato = string_1.format(num_1, num_2, num_3)
print('Exemplo sem informar os índices')
print(formato)
# Exemplo criado para mostrar de forma não sequêncial, onde pode se pegar
# o valor da variável pelo índice. Pois a função format(), quando aplicada,
# ela cria indices para cada valor do argumento, assim podendo pegar o valor
# desejado pelo índice. Obs: Caso inicie as consultas por índice, é obrigatório
# colocar o restante, pois assim irá quebrar o codiogo.
print('Exemplo informando os índices.')
string_2 = 'Número 2 = {1}, Número 1 = {0}, Número 3 = {2}'
formato = string_2.format(num_1, num_2, num_3)
print(formato)
# Exemplo criado para mostrar como funciona agora, não por argumento, mas sim
# por parâmetro. Obs: Caso inicie a declaração de parâmetros, deve-se terminar
# declrando até o último, pois já foi iniciado desta forma, mas o contrário é
# permitido. Se caso você iniciou com p1 = value, p2 = value, p3 = value, na função format() deve 
# ir até o final desta forma, porém, se for p1, p2, p3 = value um valor no último, é 
# permitido pela linguagem, pois não tem mais nenhum parâmetro a frente do último. 
print('Exemplo usando parâmetros.')
string_3 = 'Parâmetro 3 = {parametro_1}, Parâmetro 1 = {parametro_2}, Parâmetro 3 = {parametro_3}'
formato = string_3.format(
            parametro_1 = 3,
            parametro_2 = 2,
            parametro_3 = 1
        )
print(formato)
# Obs: Caso queira formatar os valores do tipo float ou int, pode usar desta forma com ou sem informar
# nenhum tipo de índice ou parâmetro, desta forma :.2f, que irá funcionar.
