class matrix(object):
    def __init__(self, m): #матрица - двухмерный массив (подмасивы имеет равную величину)
        self.matrix=m
        self.l=len(m)
        self.h=len(m[0])

    def elemet(self, n, k):
        return int(self.matrix[n][k])

    def replace_l(self, n, z):
        self.matrix[n]=z
        return matrix(self.matrix)

    def replace_e(self, n, k, Z):
        self.matrix[n][k]=Z
        return matrix(self.matrix)

    def delete_line(self, n): #удаление строки матрицы
        i=0
        m2=('x '*(self.l-2)+'x').split(' ')
        while i<self.l-1:
            if i<n:
                m2[i]=self.matrix[i]
            else:
                m2[i]=self.matrix[i+1]
            i+=1
        return matrix(m2)

    def delelete_hight(self, k): #удаление столбца
        i=0
        H=self.h
        m1 =[]
        while i<self.l:
            m2 = ('x ' * (H - 2) + 'x').split(' ')
            j=0
            while j<H-1:
                if j<k:
                    m2[j]=self.matrix[i][j]
                else:
                    m2[j]=self.matrix[i][j+1]
                j+=1
            m1.append(m2)
            i += 1
        return matrix(m1)

    def pokazatel(self):
        sum=0
        if self.l==1:
            return (self.matrix[0][0])
        else:
            n = 0
            while n < self.h:
                e = int(self.matrix[0][n])
                k=((self.delelete_hight(n)).delete_line(0)).pokazatel()
                sum += ((-1)**(n+2))*e*(k)
                n+=1
        return sum


if __name__=="__main__":
    print('введите размеры матрицы. пример ввода:')
    print('2 3')
    print('__________')
    a=str(input()).split()
    n=int(a[0])
    m=int(a[1])
    mas=[]
    l=0
    print('введите матрицу. Пример:')
    print('-1 9 4')
    print('7 0 99')
    print('----------')
    while n>l:
        mas.append(list(map(int, str(input()).split())))
        l+=1
    ma=matrix(mas)
    if m==n:
        print('показатель: '+str(ma.pokazatel()))
    else:
        print('невозможно посчитать показатель')