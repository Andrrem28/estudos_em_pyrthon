'''
Introdução ao desempacotamento + tuples (tuplas)
'''

# item1, item2, item3 = ['Arroz', 'Feijão', 'Macarrão']
#  item1, *_ = ['Arroz', 'Feijão', 'Macarrão']
_, item2, *_ = ['Arroz', 'Feijão', 'Macarrão']
_, _, item3, *_ = ['Arroz', 'Feijão', 'Macarrão']

# print(item1, item2, item3)
# print(item1, _)
# print(item2, _)
print(item3, _)
