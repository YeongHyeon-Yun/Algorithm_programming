hoy = list(map(int, input().split()))
sum = 0
for i in range(0, len(hoy)-1, 2):
    sum += hoy[i]*hoy[i+1]
print(sum)