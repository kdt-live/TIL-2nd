f = open('hello.txt', 'r', encoding='UTF8')
text = f.readline()
print(text)
text = f.readline()
print(text)
text = f.readline()
print(text)
f.close()


with open('hello.txt', 'r', encoding='UTF8') as f:
    print(type(f))
    text = f.readline()
    print(text)
    text = f.readline()
    print(text)
    text = f.readline()
    print(text)