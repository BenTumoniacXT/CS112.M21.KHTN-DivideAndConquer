def length(a):
    z = 0
    while a != 0:
        z += 1
        a //= 10
    
    return z

def pw10(a):
    z = 1
    for i in range (a): z *= 10

    return z

def krsb_lite(x, y):
    if x == 0 or y == 0: return 0

    nx = max(length(x), length(y))
    if (nx < 4): return x * y
    
    nx = (nx // 2) + (nx % 2)
    nx2 = pw10(nx * 2)
    nx = pw10(nx)

    x1 = x // nx
    x0 = x - (x1 * nx) 
    y1 = y // nx
    y0 = y - (y1 * nx) 

    z0 = krsb_lite(x0, y0)
    z2 = krsb_lite(x1, y1)
    z1 = krsb_lite(x1 + x0, y1 + y0) - z2 - z0

    return z2 * nx2 + z1 * nx + z0

print("Type n and m: ", end = "")
n, m = map(int, input().split())

print("Answer:", krsb_lite(n, m))
