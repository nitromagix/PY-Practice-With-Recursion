# Write code for algorithm 1 below

def one(n):
    if n == 0:
        return n
    print(n)
    one(n-1)


one(7)
