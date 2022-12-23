totalpoints = 0
with open("input.txt") as gamefile:

    roundpoint = 0
    for index, game in enumerate(gamefile.readlines()):
        opponent = game[0]
        outcome = game[2]
        me = ""
        
        #finding what I go with
        if opponent == "A" and outcome == "X":
            me = "Z"
        if opponent == "A" and outcome == "Y":
            me = "X"
        if opponent == "A" and outcome == "Z":
            me = "Y"

        if opponent == "B" and outcome == "X":
            me = "X"
        if opponent == "B" and outcome == "Y":
            me = "Y"
        if opponent == "B" and outcome == "Z":
            me = "Z"

        if opponent == "C" and outcome == "X":
            me = "Y"
        if opponent == "C" and outcome == "Y":
            me = "Z"
        if opponent == "C" and outcome == "Z":
            me = "X"

        #extra points
        if me == "X":
            roundpoint += 1
        if me == "Y":
            roundpoint += 2
        if me == "Z":
            roundpoint += 3

        #draw
        if outcome == "Y":
            roundpoint += 3

        #win
        if outcome == "Z":
            roundpoint += 6

        totalpoints += roundpoint
        roundpoint = 0

print(totalpoints)
