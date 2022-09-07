# Write code for algorithm 3 below

def fib(n, i=0):
    if i == 0:
        return f"{0}"
    if n == 1 or n == 2:
        return 1
    return f"{i} " + f"{fib(i+1) + fib(i+2)} "

print(fib(8))