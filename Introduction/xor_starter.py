text = 'label'

number = 13

def xor(text,key):
    result = ''
    for char in text:
        result += chr(ord(char) ^ key)
    return result

xor = xor('label',13)
print(f"crypto{{{xor}}}")
