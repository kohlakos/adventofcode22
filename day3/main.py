with open("test.txt") as itemlist:

    first_comp = ""
    second_comp = ""
    for rucksack in itemlist:
        length = int(len(rucksack))
        divider = int(len(rucksack)/2)
        first_comp = rucksack[0:divider]
        second_comp = rucksack[divider:length]

        
        print(rucksack,first_comp,second_comp, length, divider)