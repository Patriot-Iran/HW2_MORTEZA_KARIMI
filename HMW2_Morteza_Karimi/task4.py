def fact(n):
    t=1
    if (n==0):
        return 1
    else:
        while n>0 :
         t=t*n
         n=n-1
    
    return t


def ex(p,x):
    EX=1.0
    for i in range (1,p):
       
    
        EX=EX+(x**i/fact(i))
    return round(EX,3)



x=float(input (f'enter the value of x:\n'))
p=int (input (f'enter the series item:\n'))


print (ex(p,x))