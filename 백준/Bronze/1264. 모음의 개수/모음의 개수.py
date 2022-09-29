stop = ''
answer = []

while stop != '#':
    count = 0
    string = input()
    for c in string:
        if c == 'a' or c == 'e'or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E'or c == 'I' or c == 'O' or c == 'U':
            count += 1
        elif c == '#':
            stop = '#'
    if stop != '#':
        answer.append(count)

for c in answer:
    print(c)