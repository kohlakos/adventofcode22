from collections import Counter

def load_input():
    with open('test.txt', mode='r') as file:
        content = file.readlines()
        return content

    first_comp = ""
    second_comp = ""
    for rucksack in itemlist:
        length = int(len(rucksack))
        divider = int(len(rucksack)/2)
        first_comp = rucksack[0:divider]
        second_comp = rucksack[divider:length]

        for letter, count in itemlist.items():
            if (count > 1):
                print(letter)


if __name__ == "__main__":
    input = load_input()
    for lines in input:
        find_dup_char(lines)