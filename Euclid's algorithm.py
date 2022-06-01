# Euclid's algorithm

positive_numbers = []
m = int(input("Input a positive number:"))
n = int(input("Input another positive number:"))

positive_numbers.append(m)
positive_numbers.append(n)

# Ensure m >= n
for i in range(2):
    i = 0
    for j in range(2):
        j = i + 1
        if positive_numbers[j] > positive_numbers[i]:
            vac = positive_numbers[i]
            positive_numbers[i] = positive_numbers[j]
            positive_numbers[j] = vac

print("Number List:", positive_numbers)
print("m is:", positive_numbers[0])
print("n is:", positive_numbers[1])

key = positive_numbers[0] / positive_numbers[1]
r = positive_numbers[0] % positive_numbers[1]
positive_numbers.append(r)
print(positive_numbers)

# Find Greatest common divisor

if positive_numbers[2] == 0:
    print("The Greatest common divisor is:", positive_numbers[1])
else:
    while positive_numbers[2] != 0:
        positive_numbers[0] = positive_numbers[1]
        positive_numbers[1] = positive_numbers[2]

        key = positive_numbers[0] / positive_numbers[1]
        positive_numbers[2] = positive_numbers[0] % positive_numbers[1]
        print(positive_numbers)

        if positive_numbers[2] == 0:
            break
    print("The Greatest common divisor is:", positive_numbers[1])
