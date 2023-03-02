with open('mecz_przyklad.txt', 'r') as f:
    contents = f.read()
    passa, i, ilosc, passa_max = 0, 0, 0, 0
    
    while i < len(contents) - 1:

        if contents[i] == contents[i + 1]:
            passa += 1

        if contents[i] != contents[i + 1] and passa:
            passa_max = passa
            passa = 0
        i += 1
    
print(passa_max)