# build a set
chars = {'a', 'b', 'c', 'd', 'f'}
print('c' in chars)

letters = set('hello')
letters = set('abcf')
print(letters)

print(letters.intersection(chars))

chars.add('e')
print(chars)