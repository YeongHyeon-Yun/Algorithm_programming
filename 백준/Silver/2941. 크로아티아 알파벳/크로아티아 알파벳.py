croatias = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
count = 0

for croatia in croatias:
    if croatia in word:
        count += word.count(croatia)

result = len(word) - count*2+count

print(result)