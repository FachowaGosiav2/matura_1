with open('mecz.txt', 'r') as f:
    contents = f.read()
    passa, i, ilosc, passa_max, a, b, win = 1, 0, 0, 0, 0, 0, ''
    
    while i < len(contents) - 1:

        if contents[i] == contents[i + 1]:
            passa += 1

        if passa >= 10 and passa_max < passa:
            win = contents[i]
            passa_max = passa
        
        if contents[i] != contents[i + 1] and passa >= 10:
            ilosc += 1

        if contents[i] != contents[i + 1]:
            passa = 1

        i += 1
    
print(ilosc, win, passa_max)