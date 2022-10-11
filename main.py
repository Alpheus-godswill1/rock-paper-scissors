import random 

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors:\n ").lower()
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return 'It\'s a tie'
    
    # In this game you know that r>s, s>p , p>r
    
    if who_wins(user, computer):
        return 'You won!'
    
    return 'You lost!'

def who_wins(player, opponent):
    #return true if the player wins
    # In this game you know that r>s, s>p , p>r
    
    if (player == 'r' and opponent ==  's') or (player == 's' and opponent == 'p') or \
        (player == 'p' and opponent == 'r'):
            return True

print(play())