def startup():
    while True:
        try:
            number = int(input("Please add a number for the Collatz sequence: "))
        except ValueError:
            print("Please only use positive numbers and try again.")
        else:
            return number

def collatz(number):
    if number % 2 == 0:
        answer = number // 2
        return answer
    else:
        answer = 3 * number + 1
        return answer

restart = "Y"
count = 0
while restart == "Y":
    number = startup()
    while collatz(number) != 1:
        collatz(number)
        number = collatz(number)
        print(number)
        count += 1
    else:
        print(1)
        print()
        print("The sequence took " + str(count) + " cycles to complete!")
        print()
        try:
            again = str(input("Do you want to try again? Y/N: "))
        except ValueError:
            print("Please only use Y/N and try again.")
        else:
            if again == "Y":
                continue
            else:
                exit()
