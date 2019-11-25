# build and display a reversed generator
def reversed_chars(new_str):
    full_length = len(new_str)
    for x in range(full_length -1, -1, -1):
        yield new_str[x]
        
# reversed loop
for char in reversed_chars("Python!"):
    print(char)