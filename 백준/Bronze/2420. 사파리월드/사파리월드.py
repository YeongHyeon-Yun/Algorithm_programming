A, B = map(int, input().split(' '))
C = A - B
if C < 0:
    print(0 - C)
else:
    print(C)