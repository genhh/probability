import numpy as np
import matplotlib.pyplot as plt

def plot_res(w,b,x,y,iter):
    xi=np.linspace(0,4.5)
    yi = -(w[0]*xi+b)/w[1]
    plt.plot(xi,yi)
    for i in range(len(y)):
        if y[i]==1:
            plt.plot(x[i,0],x[i,1],'r*')
        else:
            plt.plot(x[i,0],x[i,1],'b.')
    plt.xlim(0,4.5)
    plt.ylim(-2,3.5)
    plt.text(3,0,'iter'+str(iter)+':w='+str(w)+',b='+str(b))
    plt.savefig("image"+str(iter)+".jpg")
    plt.show()

def percepetron(x,y,eta=1):
    m,n = x.shape
    w= np.zeros(n)
    b = 0
    iter = 0
    while True:
        flag2 = True
        for i in range(m):
            if y[i]*((w*x[i,:]).sum()+b) <= 0:
                iter = iter + 1
                w = w+eta*y[i]*x[i]
                b = b+eta*y[i]
                flag2 = flag2 and False
                print("iter",iter,":w=",w," , b=",b)
                plot_res(w,b,x,y,iter)
                
        if flag2:
            break
    return w,b

if __name__ == '__main__':
    x = np.array([[3,3],[4,3],[1,1]])
    y = np.array([1,1,-1])
    w,b = percepetron(x,y)
    
    print(w,b)