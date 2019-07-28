'''Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock'''

scoreP1 = 0
scoreP2 = 0

nameP1 = input("Player 1 name:")
nameP2 = input("Player 2 name:")


while scoreP1 or scoreP2 < 3:
    p1Choice = int(input(nameP1 + ", Please choose (1) Rock, (2) Paper or (3) Scissors:"))
    p2Choice = int(input(nameP2 + ", Please choose (1) Rock, (2) Paper or (3) Scissors:"))
    if p1Choice == p2Choice:
        print("Player1 score:" + str(scoreP1) + ", Player 2 score:" + str(scoreP2))
    elif p1Choice < p2Choice:
        scoreP1 += 1
    else:
        scoreP2 += 1
            
print(scoreP1)
        
