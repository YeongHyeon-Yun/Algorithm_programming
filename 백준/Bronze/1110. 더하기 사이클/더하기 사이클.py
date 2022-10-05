num = input()
new = ''
result = num
count = 0
while True:
    if int(num) > 9:
        new = str(int(num[0]) + int(num[1]))
        if len(new) == 2:
            num = num[1] + new[1]
        else:
            num = num[1] + new[0]
    else:
        if len(num) == 2:
            pass
        else:
            num = '0' + num
        new = str(int(num[0]) + int(num[1]))
        if len(new) == 2:
            num = num[1] + new[1]
        else:
            num = num[1] + new[0]
            
    count += 1
    if int(num) == int(result):
        break
print(count)