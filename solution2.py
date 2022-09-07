# Write code for algorithm 2 below

def two(n, i=1):

    if i == n:
        return f"{i}"

    return f"{i} " + two(n, i+1)


print(two(10))
