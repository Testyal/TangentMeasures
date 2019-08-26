import numpy as np
import matplotlib.pyplot as plt

def dyadicFamily(k):
    return [i/(2**k) for i in range(2**k - 1)]

def leftEndpoint(binarySequence):
    l = 0.0
    for k,i in enumerate(binarySequence):
        if i == 1.0 or i == 0.0:
            l += i*1/(2**(k+1))
        else:
            print("Error: binary sequence doesn't include 1s and 0s")
    return l 

class BinarySequence:
    def __init__(self,i):
        self.list = i
        self.leftEndpoint = leftEndpoint(i)
        self.parent = i[:-1]
        if len(i) >= 2:
            self.parity = (i[-1] + i[-2]) % 2

def enumerateBinarySequences(k):
    l = []
    for i in range(2**k):
        i = [int(j) for j in str(bin(i))[2:]]
        for x in range(k - len(i)):
            i = [0] + i
        l.append(BinarySequence(i))

    return l

def unmute(keys):
    return [repr(key) for key in keys]

#def s(y,k,i : BinarySequence):
#    if abs(y) < epsilon(k):

def g(k,epsilon):
    binSeqk = enumerateBinarySequences(k)
    gk = {repr(i.list) : 1 for i in binSeqk}
    if k == 1:
        pass
    else:
        gprior = g(k-1,epsilon)
        n = 0
        for i in binSeqk:
            if abs(gprior[repr(i.parent)]) < epsilon:
                gk[repr(i.list)] = gprior[repr(i.parent)]
            else:
                gk[repr(i.list)] = (1 + ((-1)**i.parity)*epsilon)*gprior[repr(i.parent)]

            if gk[repr(i.list)] == 0:
                print("bad thing happen :)")

            if gprior[repr(i.parent)] > epsilon or gprior[repr(i.parent)] < 1:
                n += 1
        print(n)
        if n/2**k < epsilon:
            epsilon = epsilon/2
    return gk

g(15,0.5)

#def gfunc(x,k):
#    for i in enumerateBinarySequences(k):
#        if i.leftEndpoint <= x < i.leftEndpoint + 1/(2**k):
#            return g(k)[repr(i.list)]
#    return 0

def plotg(k,epsilon,c,l):
    gk = g(k,epsilon)
    #print(gk)
    xx = np.linspace(0.0, 1.0, 2**k + 1)
    print(xx)
    ii = enumerateBinarySequences(k)
    plt.step(xx, [gk[repr(i.list)] for i in ii] + [gk[repr(ii[-1].list)]], where='post', color=c, linewidth=0.3, label=l)

#epsilon = float(input("Enter epsilon: "))
#k = int(input("Enter k:"))

def plotParity(k,c='black'):
    ii = enumerateBinarySequences(k)
    plt.hlines([i.parity for i in ii] + [ii[-1].parity], np.linspace(0, 1.0 - 1/2**k, 2**k), np.linspace(1/2**k, 1.0, 2**k), color=c)

plotg(20,0.1,'lavender','k=20')
plotg(10,0.1,'lightblue','k=10')
plotg(7,0.1,'gold','k=7')
plotg(5,0.1,'red','k=5')
plotg(2,0.1,'green','k=2')

#plotParity(2)
#plotParity(5,'red')
#plotParity(5)
#plotParity(10,'lightblue')



plt.legend()
plt.show()
