totalpoints = 0
with open("input.txt") as gamefile:

    roundpoint = 0
    for index, game in enumerate(gamefile.readlines()):
        opponent = game[0]
        me = game[2]

        #draw
        if opponent == "A" and me == "X":
            roundpoint += 3
        if opponent == "B" and me == "Y":
            roundpoint += 3
        if opponent == "C" and me == "Z":
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
