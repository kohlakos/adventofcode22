# A for Rock, B for Paper, and C for Scissors.
# X for Rock, Y for Paper, and Z for Scissors.
# Additional points: 1 for Rock, 2 for Paper, and 3 for Scissors.
# Draw is 3 win is 6.

totalpoints = 0
with open("test.txt") as gamefile:

    my_points = 0
    opp_points = 0
    for index, game in enumerate(gamefile.readlines(), 1):
        opponent = game[0]
        me = game[2]
        
        if opponent == "A" and me == "X":
            #draw
            my_points += 3
            opp_points += 3
        
        if opponent == "A" and me == "Y":
            my_points += 6
        if opponent == "B" and me == "Z":
            my_points += 6
        if opponent == "C" and me == "X":
            my_points += 6

        if me == "X":
            roundpoint += 1
        if me == "Y":
            roundpoint += 2
        if me == "Z":
            roundpoint += 3

        if index % 3 == 0 :
            #end of every round
            if 
            totalpoints += roundpoint
            roundpoint = 0

print(totalpoints)
