chess = list(map(int, input().split()))
correct = [1, 1, 2, 2, 2, 8]
for i in range(len(chess)): print(correct[i] - chess[i], end=' ')