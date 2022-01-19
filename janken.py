import random as r

outcomes = {
    'R':3,
    'S':2,
    'P':1
    }

wins = 0
loss = 0
games = 0
names = ['Paper','Scissor','Rock']

def game():
    global wins
    global loss
    global games
    print("R for Rock, P for Paper or S for Scissor")
    n = True
    while n:
        try:
            x = outcomes[input("Enter: ").upper()]
            n = False
        except:
            print("Invalid value!")
    c = r.randint(1,3)
    print(" Player: ",names[x-1],'\n',"CPU   : ",names[c-1])
    if x == c:
        print("Draw")
    elif((x-c)%3 == 1):
        print("You Win")
        wins += 1
    else:
        print("You Lose")
        loss += 1
    games += 1

try:
    n = int(input("No. of Rounds: "))
except:
    print("I don't wanna play with you.")
    quit()
while(n):
    game()
    n -= 1
if games:
    print("Result:")
    print(" Won: ",wins,'\n',"Lost: ",loss)
    print("Wins: ",f'{(wins/games)*100:.2f}','%')
