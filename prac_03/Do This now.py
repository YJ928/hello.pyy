def main():
    age = 0
    valid_input = False
    while not valid_input:
        try:
            age = int(input("Enter your age: "))
            if age <= 0:
                print("Age must be >0!")
            else:
                valid_input = True
        except ValueError:
            print("Please enter valid age!")

    if is_even(age):
        print("Your age is {}, it is an even number.".format(age))
    else:
        print("Your age is {}, it is an odd number.".format(age))

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

main()
