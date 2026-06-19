'''
Python Special Methods, Magic Methods ou Dunder Methods
Dunder = Double Underscore = __dunder__
__lt__(self, other) - self < other
__le__(self, other) - self <= other
__gt__(self, other) - self > other
__ge__(self, other) - self >= other
__eq__(self, other) - self == other
__ne__(self, other) - self != other
__add__(self, other) - self + other
__sub__(self, other) - self - other
__mul__(self, other) - self * other
__truediv__(self, other) - self / other
__neg__(self) - -self
__str__(self) - str
__repr__(self) - str
'''

class Ponto:
    # def __init__(self, x, y, z = 'String'):
    #     self.x = x
    #     self.y = y
    #     self.z = z
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __str__(self):
    #     return f'({self.x}, {self.y})'

    # def __repr__(self):
    #     # class_name = self.__class__.__name__
    #     class_name = type(self).__name__
    #     return f'{class_name} = (x = {self.x}, y = {self.y}, z = {self.z} )'
   
    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r})'

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        
        return Ponto(novo_x, novo_y)
    
    def __gt__(self, other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y

        return Ponto(resultado_self, resultado_other)

# ponto_1 = Ponto(4, 3)
# ponto_2 = Ponto(10, 20)

# print(ponto_1)
# print(repr(ponto_2))
# print(f'{ponto_2!r}')

if __name__ == '__main__':
    ponto_1 = Ponto(4, 3)
    ponto_2 = Ponto(10, 20)

    ponto_3 = ponto_1 + ponto_2

    print(ponto_3)

    print('Ponto 1 é maior que Ponto 2', ponto_1 > ponto_2)
    print('Ponto 2 é maior que Ponto 1', ponto_2 > ponto_1)