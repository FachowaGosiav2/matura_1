with open('mecz.txt', 'r') as f:
    contents = f.read()
    i = 0
    a = 0
    b = 0
    while i < len(contents) - 1:
        if contents[i] == 'A':
            a += 1

        if contents[i] == 'B':
            b += 1

        if a >= 1000 or b >= 1000:

           if a > b and a - 3 >= b:
               break
            
           elif b > a and b - 3 >= a:
               break

        i += 1
    

    print((a, b))