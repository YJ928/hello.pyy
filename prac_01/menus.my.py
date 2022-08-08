secret_alphabet1 = "H"
secret_alphabet2 = "G"
secret_alphabet3 = "Q"

name = input("Enter you name: ")
print('''
(H)ello
(G)oodbye
(Q)uit
''')
guess = input(">>>").upper()
while guess != "Q":
    if guess == "H":
        print("Hello", name)
    elif guess == "G":
        print("Goodbye", name)
    else:
        print("Invalid message.")
    guess = input(">>>").upper
print("Finished.")