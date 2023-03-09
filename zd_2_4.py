with open ('pary.txt', 'r') as f:
    content = f.read()
    con = content.split()
    lewa = []
    prawa = []
    i = 0
    j = 0
    dobre_part = []

    while i < len(con) - 1:
        lewa.append(con[i])
        prawa.append(con[i+1])
        i += 2

    while(j < len(prawa)-1):

        prawa1 = int(prawa[j])
        lewa1 = int(lewa[j])

        while(True):
            if(prawa1 % 2 != 0):
                prawa1 - 1
            prawa1 = prawa1 / 2
            if(lewa1 % 2 != 0):
                lewa1 - 1
            lewa1 = lewa1 / 2
            if(prawa1 == lewa1 ):
                dobre_part.append((lewa1, prawa1))
                break

        print(prawa1, lewa1)


        j += 1

    print(dobre_part)