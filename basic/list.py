n = [1, 2, 3, 21, 5, 6, 11]
max = n[0]
for number in n:
    if number > max:
        max = number
print(max)
n.append(23)
print(n)
n.insert(4,9)
print(n)
n.pop(2)
n.reverse()
print(n)
n.remove(2)
print(n)
print(2 in n)
n.index(21)
print(n)
n.sort()
print(n)
n.reverse()
num = n.copy()
num.append(10)
print(num)