elf_number = 0
max_cal = 0
with open("input.txt") as cal_file:
    
    temp = 0
    for cal in cal_file.readlines():
        
        if cal == "\n":
            max_cal = temp
            print(temp)
            temp = 0
        else:
            temp += int(cal.rstrip())

