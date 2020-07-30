n = [1, 2, 3, 3, 4, 4, 2, 5, 6, 6, 6, 8, 9]
uniques = []
for number in n:
    if number not in uniques:
        uniques.append(number)
print(uniques)
