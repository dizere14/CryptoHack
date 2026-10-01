def gcf(a,b):
    while b != 0:
        a,b = b ,a % b
    return abs(a)

print(gcf(11,17))