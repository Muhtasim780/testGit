weigt = int(input('your weight: '))
unit = input('(L)bs or (K)gs: ')
if unit.upper() == 'L':
    converted = weigt*0.45
    print(f"your weight {converted}")
else:
    converted = weigt/0.45
    print(f"your weight {converted}")
