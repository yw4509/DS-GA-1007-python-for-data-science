import sys

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(1, len(sys.argv)):
    arg = sys.argv[i]
    num = int(arg)
    
    print("fib of", num, " = ", fib(num))
    