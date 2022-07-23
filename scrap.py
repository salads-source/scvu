import string
s = "Odie is a very good doggo. But Garfield abuses him. I have $3."
list = s.split(' ')
p_list = ['?', '!', '.', ',', ':']
new_list = []

for word in list:
    for letter in word:
        if letter in p_list:
            word = word.replace(letter, "")
    new_list.append(word.lower())


print(list)
print(new_list)


