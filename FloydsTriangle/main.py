rows = int(input("Enter number of rows: "))
num = 1
print("Floyds triangle")
for i in range (1, rows + 1):
    for j in range (1, i+1):
        print(num, end = " ")
        num = num + 1
    print()

