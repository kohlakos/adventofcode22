totalpoints = 0
with open("input.txt") as gamefile:

    for game, index in enumerate(gamefile.readlines()):
        print(index, game)
       
