number = int(input("Please enter a number between 1 and 100 to count to: "))

for count in range(1, number+1):
    if count % 3 == 0 and count % 5 == 0:
        print("fizzbuzz")
    elif count % 3 == 0:
        print("fizz")
    elif count % 5 == 0:
        print("buzz")
    else:
        print(count)








