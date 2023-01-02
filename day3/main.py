from collections import Counter
import string

def load_points():
    alphabet_lowercase = list(string.ascii_lowercase)
    alphabet_uppercase = list(string.ascii_uppercase)
    alphabet = alphabet_lowercase + alphabet_uppercase

    point_dict = {}

    for index, letter  in enumerate(alphabet):
        new_key = letter
        new_value = index + 1
 
        point_dict[new_key] = new_value

    return point_dict


def load_input():
    with open('test.txt', mode='r') as file:
        content = file.readlines()
        return content

def find_dup_char(input):

    WC = Counter(input)

    for letter, count in WC.items():
        
        if (count > 1):

            length = int(len(input))
            divider = int(len(input)/2)
            first_comp = input[0:divider]
            second_comp = input[divider:length]

            lst = []
            for pos,char in enumerate(input):
                if(char == letter):
                    lst.append(pos)
            print(lst)

if __name__ == "__main__":
    points = load_points()
    input = load_input()
    
    for lines in input:
        find_dup_char(lines)