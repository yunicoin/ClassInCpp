import math
class vector(object):
    def __init__(self, mas):
        self.vector=mas
        self.meger=len(mas)
    def plus(self, a):
        l=0
        m=[]
        while l<(self.meger) and self.meger==len(a):
            m.append(self.vector[l]+a.vector[l])
            l+=1
        return vector(m)
    def  minus(self, a):
        l = 0
        m = []
        while l < (self.meger) and self.meger == len(a):
            m.append(self.vector[l] + a.vector[l])
            l += 1
        return vector(m)
    def proizvedenie(self, n):
        l=0
        m=[]
        while l<self.meger:
            m.append(n*self.vector[l])
            l+=1
        return vector(m)
    def umnojenie(self, a):
        l = 0
        m = 0
        while l < (self.meger) and self.meger == a.meger:
            m+=(self.vector[l] * a.vector[l])
            l += 1
        return float(m)
    def dlina(self):
        l=0
        d=0
        while l<self.meger:
            d+=self.vector[l]**2
            l+=1
        d=math.sqrt(d)
        return d
    def cos(self, a):
        x=self.umnojenie(a)
        k=(self.dlina()*a.dlina())
        return x/k
    def ugol(self, a):
        return math.acos(self.cos(a))
    def ravn(self, a):
        if a.meger==self.meger:
            return (False)
        else:
            l=0
            while l<self.meger:
                if a.vector[l]!=self.vector[l]:
                    return False
                else:
                    if l==self.meger-1:
                        return True
                l+=1
    def print(self):
        print('\t'.join(list(map(str, self.vector))))

if __name__=="__main__":
    v=list(map(float, str(input()).split()))
    v=vector(v)
    v.print()
    print(v.dlina())
    m = list(map(float, str(input()).split()))
    m = vector(m)
    print(m.ugol(v))
    print(m.umnojenie(v))
