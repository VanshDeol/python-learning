def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range (1,number+1):
        decimal = str(i)
        binary = bin(i)[2:]
        octal = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        print(f"{decimal.rjust(width)} {octal.rjust(width)} {hexa.rjust(width)} {binary.rjust(width)} ")
        

