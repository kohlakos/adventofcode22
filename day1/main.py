elf_number = 0
max_cal = 0
with open("input.txt") as cal_file:
    
    test = 0
    for cal in cal_file.readlines():
        
        if cal == "\n":
            print(test)
        else:
            test += int(cal.rstrip())

