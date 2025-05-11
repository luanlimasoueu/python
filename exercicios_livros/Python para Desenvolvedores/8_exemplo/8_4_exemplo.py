class Mat(object):
    """
    Matriz esparsa
    """
    def __init__(self):
        """
        Inicia a matriz
        """
        self.itens = []
        self.default = 0
    
    def __getitem__(self, xy):
        """
        Retorna o item para X e Y ou default caso contrário
        """
        i = self.index(xy)
        if i is None:
            return self.default
        return self.itens[i][-1]
    
    def __setitem__(self, xy, data=0):
        """
        Cria novo item na matriz
        """
        i = self.index(xy)
        if not i is None:
            self.itens.pop(i)
            self.itens.append((xy, data))

    def __delitem__(self, xy):
        """
        Remove um item da matriz
        """
        i = self.index(xy)
        if i is None:
            return self.default
        return self.itens.pop(i)
    
    def __getslice__(self, x1, x2):
        """
        Seleciona linhas da matriz
        """
        r = []
        for x in range(x1, x2 + 1):
            r.append(self.row(x))
        return r
    def index(self, xy):
        i = 0
        for item in self.itens:
            if xy == item[0]:
                return i
            i += 1
        else:
            return None
    def dim(self):
        """
        Retorna as dimensões atuais da matriz
        """
        x = y = 0
        for xy, data in self.itens:
            if xy[0] > x: x = xy[0]
            if xy[1] > y: y = xy[1]
        return x, y
    def keys(self):
        """
        Retorna as coordenadas preenchidas
        """
        return [xy for xy, data in self.itens]
    def values(self):
        """
        Retorna os valores preenchidos
        """
        return [data for xy, data in self.itens]
    def row(self, x):
        """
        Retorna a linha especificada
        """
        X, Y = self.dim()
        r = []
        for y in range(1, Y + 1):
            r.append(self[x,y])
        return r
    def col(self, y):
        """
        Retorna a coluna especificada
        """
        X, Y = self.dim()
        r = []
        for x in range(1, X + 1):
            r.append(self[x,y])
        return r
    def sum(self):
        """
        Calcula o somatório
        """
        return sum(self.values())
    def avg(self):
        """
        Calcula a média
        """
        X, Y = self.dim()
        return self.sum() / (X * Y)
    def __repr__(self):
        """
        Retorna uma representação do objeto como texto
        """
        r = 'Dim: %s\n' % repr(self.dim())
        X, Y = self.dim()
        for x in range(1, X + 1):
            for y in range(1, Y + 1):
                r += ' %s = %3.1f' % (repr((x, y)),
                      float(self.__getitem__((x, y))))
                r += '\n'
        return r
if __name__ == '__main__':
    mat = Mat()
    print ('2 itens preenchidos:')
mat[1, 2] = 3.14
mat[3, 4] = 4.5
print (mat)
print ('Troca e remoção:')
del mat[3, 4]
mat[1, 2] = 5.4
print (mat)
print ('Preenchendo a 3ª coluna:')
for i in range(1, 4):
    mat[i + 1, 3] = i
print (mat)
print ('3ª coluna:', mat.col(3))
print ('Fatia com 2ª a 3ª linha', mat[2:3])
print ('Somatório:', mat.sum(), 'Média', mat.avg())
