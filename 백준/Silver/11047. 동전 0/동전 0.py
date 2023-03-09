N, K = map(int, input().split())
num = []
count = 0
for _ in range(N):
    num.append(int(input()))

for i in range(N):
    if K // num[N-1 -i] == 0:
        pass
    else:
        count += (K // num[N-1 -i])
        K = K % num[N-1 -i]
print(count)