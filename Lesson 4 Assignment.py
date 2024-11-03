import random

def user_weapon():
    print('Select Your Weapon (1-3)')
    print('------------------------')
    print('1. Rock')
    print('2. Paper')
    print('3.Scissors')
    user_weapon = int(input('Enter Your Weapon: '))
    return user_weapon

def opponent_weapon():
    random_weapon = random.randrange(1,4)
    print('Opponent Weapon Is:' ,random_weapon)
    return random_weapon

def winner(user,opponent):
    if user == opponent:
        print("It's a Tie!")

    elif user == 1 and opponent == 3:
        print('You Win! Rock Crushes Scissors!')
    elif user == 1 and opponent == 2:
        print('You Lose! Paper Covers Rock!')
    
    elif user == 2 and opponent == 1:
        print('You Win! Paper Covers Rock!')
    elif user == 2 and opponent == 3:
        print('You Lose! Scissors Cuts Paper!')

    elif user == 3 and opponent == 1:
        print('You Lose! Rock Crushes Scissors!')
    elif user == 3 and opponent ==2:
        print('You Win! Scissors Cuts Paper!')


def main():
    choice = 'y'
    while choice.lower() == 'y':
        user = user_weapon()
        opponent = opponent_weapon()
        winner(user,opponent)
        choice = input('Do You Want To Play Again? (y/n)')
if __name__ == '__main__':
    main()

print()
print()
print('Completed by, Cody Hobbs')
        
