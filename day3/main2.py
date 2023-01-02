from collections import Counter

def load_input():
    with open('test.txt', mode='r') as file:
        content = file.readlines()
        return content

def find_dup_char(input):

    WC = Counter(input)

    for letter, count in WC.items():
        if (count > 1):
            print(letter)
 
if __name__ == "__main__":
    input = load_input()
    for lines in input:
        find_dup_char(lines)
