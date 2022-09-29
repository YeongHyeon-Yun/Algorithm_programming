def isGroupString(str):
    save_word = []
    result = True
    before_word = ''

    for ch in str:
        if not ch.isalpha():
            continue
                
        isExist = False
        for word in save_word:
            if ch == word:
                isExist = True
                break
                
        if not isExist:
            save_word.append(ch)
        else:
            if before_word == ch:
                continue
            else:
                result = False
                break
        before_word = ch

    return result

number = int(input())

input_word = []
count = 0
for words in range(number):
    input_str = str(input())
    if isGroupString(input_str):
        count += 1
print(count)