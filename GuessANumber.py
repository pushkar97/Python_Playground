import random

def get_hint(answer, user_guess):
    rand_choice = random.randrange(1,4,1)
    if rand_choice == 1:
        if (answer <=user_guess):
            return f"number is less than or equal to {user_guess}"
        else:
            return f"number is greater than {user_guess}"
    elif rand_choice == 2:
        # rand_hint = random.randrange(3,5,1)
        if(answer % user_guess):
            return f"number is not divisible by {user_guess}"
        else:
            return f"number is divisible by {user_guess}"
    elif rand_choice == 3:
        # rand_hint = random.randrange(2,4,1)
        if(user_guess % answer):
            return f"{user_guess} is not a multiple of this number"
        else:
            return f"{user_guess} is a multiple of this number"


def guess_a_number():

    random.seed()
    level = int(input("Select level (1 to 10) : "))
    if not(1 <= level <=10):
        return "Error : Invalid level, please select level between 1 and 10"
    range = level*20
    answer = random.randrange(1,range+1,1)
    while(True):
        user_guess = int(input(f"Make a guess! (1 : {range}): "))
        
        if(user_guess == answer):
            print("You are correct!")
            break
        print("Hint : " + get_hint(answer, user_guess))


if(__name__ == "__main__"):
    guess_a_number()