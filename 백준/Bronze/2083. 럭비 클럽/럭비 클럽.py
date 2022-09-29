while True:
    string = input()
    if string == '# 0 0':
        break
    name, age, weight = string.split(' ')
    age = int(age)
    weight = int(weight)

    if age > 17 or weight >= 80:
        print(name, 'Senior')
    else:
        print(name, 'Junior')