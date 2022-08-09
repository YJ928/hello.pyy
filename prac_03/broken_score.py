'''
The intention is that the score must be between 0 and 100 inclusive;
90 or more is excellent; 50 or more is a pass; below 50 is bad.
'''

def main():
    score = float(input("Enter your score: "))
    print(determine_status(score))

def determine_status(score):
    if score < 0 or score > 100:
        return "Invalid score!"
    elif score >= 90:
        return "You are excellent!"
    elif score >= 50:
        return "You are pass!"
    else:
        return "Its bad, but I believe you will do better next time!"

main()

