num1 = int(input("Write where you want the program to start counting from: "))
num2 = int(input("Write the last number you want the program to end with: "))
prime = []

i = num1
while i <= num2:
    if (i % 2 != 0 or i == 2) and (i != 1) and (i % 3 != 0 or i == 3) and (i % 5 != 0 or i == 5) and (i % 7 != 0 or i == 7):
        prime.insert(i, i)
    i += 1
print(prime)
print("There are " + str(len(prime)) + " prime numbers between " + str(num1) + " and " + str(num2))
