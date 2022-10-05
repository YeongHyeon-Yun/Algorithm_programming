string = input()
string = string.upper()
k = set(string)

max = string[0]
precount = 0
for i in k:
    count = 0
    for a in string:
        if i == a:
            count += 1
    if count > precount:
        max = i
        precount = count
    elif count == precount:
        max = '?'
print(max)