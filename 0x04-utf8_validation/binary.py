def binary(dec):
    remainders = []
    while True:
        if int(dec / 2) == 0:
            remainders.append(1)
            break
        
        remainders.append(int(dec % 2))
        dec = dec / 2

    string = ""
    for item in remainders[::-1]:
        string += str(item)

    if len(string) < 8:
        string = '0' + string
    
    print(string)
    return len(string)

print(binary(197))
