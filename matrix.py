class matrix(object):
    def __init__(self, m):
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

    def delete_line(self, n):
        i=0
        m2=('x '*(self.l-2)+'x').split(' ')
        while i<self.l-1:
            if i<n:
                m2[i]=self.matrix[i]
            else:
                m2[i]=self.matrix[i+1]
            i+=1
        return matrix(m2)

    def delelete_hight(self, k):
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
        if self.h==self.l:
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
    def sumL(self, n, m, k):
        H=self.h
        mas=self.matrix
        while H > 0:
            H -= 1
            mas[n][H] = k*mas[m][H]+mas[n][H]
        return matrix(mas)
    def triangularH(self):
        if self.h==1 and self.l>1:
            l=1
            m=[[self.matrix[0][0]]]
            while l<self.l:
                m.append([0])
                l+=1
            return matrix(m)
        else:
            l = 0
            mas = self.matrix
            a = 0
            if self.l==1:
                return(self)
            else:
                while a == 0 and l < self.l:
                    a = mas[l][0]
                    l += 1
                if l == self.l and a==0:
                    print('показатель матрицы = 0')
                    z = matrix(mas).delete_line(0).delelete_hight(0).triangularH().matrix
                else:
                    if l!=1:
                        mas = matrix(mas).sumL(0, l-1, 1).matrix
                    l = 1
                    while l < self.l:
                        r = (-1)*(mas[l][0])/mas[0][0]
                        mas = matrix(mas).sumL(l, 0, r).matrix
                        l += 1
                    z = matrix(mas).delete_line(0).delelete_hight(0).triangularH().matrix
                L = 0
                while L < self.l-1:
                    H = 0
                    while H < self.h-1:
                        mas[L+1][H+1] = z[L][H]
                        H += 1
                    L += 1
                return matrix(mas)
    def stabilizator(self):
        l=self.l
        m=self.matrix
        while l>1:
            l-=1
            h=l
            while h>0:
                h-=1
                if m[l][l]!=0:
                    m = matrix(m).sumL(h, l, (-1) * (m[h][l]) / m[l][l]).matrix
        return  matrix(m)
    def Gaus(self):
        if self.l==self.h:
            m=self
            return m.triangularH().stabilizator()

    def print(self):
        l = 0
        while l < self.l:
            print('\t'.join(list(map(str, (self.matrix[l])))))
            l += 1
    def GausPokazatel(self):
        if self.h==self.l:
            ma=self.Gaus().matrix
            l=0
            sum=1
            while l<self.l:
                sum=sum*ma[l][l]
                l+=1
            return sum
    def plus(self, mat): #сложение матриц
        l=0
        m=mat.matrix
        d=[]
        if self.l==len(m) and self.h==len(m[0]):
            while l<self.l:
                 h=0
                 d.append([])
                 while h<self.h:
                     d[l].append(m[l][h]+self.matrix[l][h])
                     h=1+h
                 l+=1
            return matrix(d)
        else:
            print('Ошибка')
            return matrix([[]])
    def multi(self, k): #умножение на число
        l=0
        while l<self.l:
            h=0
            while h<self.h:
                self.matrix[l][h]=self.matrix[l][h]*k
                h=1+h
            l+=1
        return self
    def T(self): #транспонирование
        tmatrix=[]
        l=0
        while l<self.l:
            h=0
            while h<self.h:
                tmatrix.append([])
                tmatrix[h].append(self.matrix[l][h])
                h=1+h
            l+=1
        return matrix(tmatrix)
    def multy(self, mat): #перемножение матриц
        m=mat.matrix
        M=self.matrix
        l = 0
        E=[]
        if self.h == mat.l:
            while l < self.l:
                h = 0
                E.append([])
                while h < mat.h:
                    r=0
                    s=0
                    while r<self.h:
                        s+=M[l][r]*m[r][h]
                        r+=1
                    E[l].append(s)
                    h = 1 + h
                l += 1
            return matrix(E)
        else:
            print('Ошибка')
            return matrix([[]])
    def stepen(self, n): #быстрое возведение в степень
        m=[[1, self.matrix]]
        while n!=m[-1][0]:
            l=len(m)
            if n>2*m[-1][0]:
                m.append([2*m[l-1][0], matrix(m[-1][1]).multy(matrix(m[l-1][1])).matrix])
            else:
                m.append([m[l-1][0]+m[l-2][0], matrix(m[-1][1]).multy(matrix(m[l-2][1])).matrix])
        return matrix(m[-1][1])

if __name__=="__main__":
    mas=[]
    masi=[]
    print('-=-=-=-=-=-=-=-')
    print('введите матрицу. Пример:')
    print('-1 9 4')
    print('7 0 99')
    print('')
    print('-=-=-=-=-=-=-=-')
    print('P.S. после того, как вели матрицу сделайте пустую строку')
    print('-=-=-=-=-=-=-=-')
    while True:
        a=str(input())
        if a=='':
            break
        else:
            mas.append(list(map(float, a.split())))
            if len(mas[0])!=len(mas[-1]):
                mas=[]
                print('ошибка вывода')
                break
    print('введите 2 матрицу')
    print('-=-=-=-=-=-=-=-')
    print('P.S. после того, как вели матрицу сделайте пустую строку')
    print('-=-=-=-=-=-=-=-')
    while True:
        a = str(input())
        if a == '':
            break
        else:
            masi.append(list(map(float, a.split())))
            if len(masi[0]) != len(masi[-1]):
                masi = []
                print('ошибка вывода')
                break
    ma=matrix(mas)
    print('-=-=-=-=-=-=-=-')
    mat = ma.plus(matrix(masi))
    print('их сумма')
    mat.print()
    print('их произведение')
    mat = ma.multy(matrix(masi))
    mat.print()
    print('------')
    print('транспонированная 1 матрица')
    ma.T().print()
    print('------')
    print('верхнеступенчатая матрица:')
    ma = ma.triangularH().print()
    print('-=-=-=-=-=-=-=-')
    print('показатель:')
    print(matrix(mas).pokazatel())
    print('')
    print(matrix(mas).GausPokazatel())
    print('-=-=-=-=-=-=-=-')
