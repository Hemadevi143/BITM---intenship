def check_number(n):
    if (n % 2 != 0):
        print("Weird")
    else:
        if n in range(2, 6):
            print("Not Weird")
        elif n in range(6, 21):
            print("Weird")
        else:
            print("Not Weird")

num = int(input("Enter an integer: "))
check_number(num)
