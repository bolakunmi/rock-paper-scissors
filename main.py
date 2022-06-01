import random

print ("""welcome to a game of rock-paper-scissors.
the rules are simple: 
R=rock
P=paper
S=scissors

Rock beats Scissors, Paper beats Rock, Scissors beats Paper.

Are you ready to be the champion?
Let the battle begin!""")


#choices to pick from
choices={'R':'Rock','P':'Paper','S':'Scissors'}

#CPU's random choice
CPU = random.choice(list(choices.keys()))

while True:
    #input your choice
    player1=input(str('pick one: R or P or S? ')).upper()

    #valid entry
    if player1 == 'R' or player1 =='P' or player1 =='S':
        #victory tests
        if (player1 == 'R' and CPU =='S') or (player1 == 'P' and CPU =='R') or (player1 == 'S' and CPU == 'P'):
            print('Player(', choices[player1], ') : CPU(', choices[CPU], ')')
            print('Player wins!')
        elif (CPU == 'R' and player1 =='S') or (CPU == 'P' and player1 =='R') or (CPU == 'S' and player1 == 'P'):
            print('Player(', choices[player1], ') : CPU(', choices[CPU], ')')
            print('CPU wins!')
        elif (CPU == player1):
            print('player(', choices[player1], ') : CPU(', choices[CPU], ')')
            print('its a tie!')
        break

    #invalid entry
    elif player1 != 'R' or player1 !='P' or player1 !='S': 
        print('invalid entry')
        continue