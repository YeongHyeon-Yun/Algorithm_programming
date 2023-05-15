n, g = input().split()
guess = []
guess = list(map(int,input().split()))
for i in range(len(guess)):
    print(guess[i] - int(n)*int(g), end=' ')