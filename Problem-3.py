a = int(input("Enter a number: "))
count = a if a % 2 != 0 else a - 1

for i in range(1, count + 1):
    print(2 * i - 1, end=", " if i < count else "\n")
