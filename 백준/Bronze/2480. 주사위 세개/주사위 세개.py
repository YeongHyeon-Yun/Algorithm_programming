hey = list(map(int, input().split()))
a = hey[0]
b = hey[1]
c = hey[2]

if a == b and a == c:
    print(10000 + a * 1000)
elif a == b and a != c and b != c:
    print(1000 + a * 100)
elif b == c and a != c and b != a:
    print(1000 + b * 100)
elif a == c and a != b and c != b:
    print(1000 + a * 100)
else:
    print(max(hey) * 100)