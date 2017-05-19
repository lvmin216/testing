def fib(x):
    a=[1,1]
    n=32
    while n<x:
        n=1
        print (a)
        a[n]=a[n]+a[n-1]
        n=n+1

    return "finished"

