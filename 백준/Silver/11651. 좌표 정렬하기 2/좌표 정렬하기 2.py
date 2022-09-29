n = int(input())

sort_list = []
for _ in range(n):
    xy = list(map(int, input().split()))
    sort_list.append([xy[1], xy[0]])
    
sort_list.sort()

for i in sort_list:
    print(i[1], i[0])