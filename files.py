with open('text.txt', 'w') as f:
    f.write('hello\nGena')
    f.close()

with open('text.txt', 'r') as f:
    for line in f:
        print(line)

    #result = f.read()
    #print(result)
