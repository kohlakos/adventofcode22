# A for Rock, B for Paper, and C for Scissors.
# X for Rock, Y for Paper, and Z for Scissors.
# Additional points: 1 for Rock, 2 for Paper, and 3 for Scissors.
# Draw is 3 win is 6.

totalpoints = 0
with open("input.txt") as gamefile:

    roundpoint = 0
    for index, game in enumerate(gamefile.readlines()):
        opponent = game[0]
        me = game[2]

        if opponent == "A" and me == "X":
            #draw
            roundpoint += 3
        if opponent == "B" and me == "Y":
            #draw
            roundpoint += 3
        if opponent == "C" and me == "Z":
            #draw
            roundpoint += 3
        
        if opponent == "A" and me == "Y":
            roundpoint += 6
        if opponent == "B" and me == "Z":
            roundpoint += 6
        if opponent == "C" and me == "X":
            roundpoint += 6

        if me == "X":
            roundpoint += 1
        if me == "Y":
            roundpoint += 2
        if me == "Z":
            roundpoint += 3

        if index % 3 == 0 :
            #end of every round
            totalpoints += roundpoint
            roundpoint = 0

print(totalpoints)
