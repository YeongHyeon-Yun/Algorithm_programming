dwarf = []
for i in range(9):
    dwarf.append(int(input()))

# dwarf = [20, 7, 23, 19, 10, 15, 25, 8, 13]

target1 = 0
target2 = 0
flag = False
for i in range(9):
    target1 = dwarf[i]
    for j in range(9):
        if j != i:
            target2 = dwarf[j]
            if sum(dwarf) - (target1 + target2) == 100:
                flag = True
                dwarf.remove(target1)
                dwarf.remove(target2)
                break
    if flag == True:
        break
    # if sum(dwarf) - target1 - target2 == 0:
    #     break
# print(sum(dwarf))
# print(target1, target2)
# print(target1 + target2)

# # k = dwarf.remove(target1)
# # k = dwarf.remove(target2)
# print(dwarf)
dwarf.sort()
for i in dwarf:
    print(i)