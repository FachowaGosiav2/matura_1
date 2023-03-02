with open('mecz.txt', 'r') as f:
    contents = f.read()
    i = 0
    ilosc = 0
    print(len(contents))
    while i < len(contents) - 1:
        
        if contents[i] != contents[i + 1]:
            ilosc += 1
        i += 1
    
    if contents[len(contents)-1] == '\n':
        ilosc -= 1

    print(ilosc)