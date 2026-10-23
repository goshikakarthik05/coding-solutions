n = int(input())
m = int(input())

if n < m:
    print("less", end='')
elif n == m:
    print("equal", end='')
else:
    print("greater", end='')