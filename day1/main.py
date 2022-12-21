elf_number = 0
max_cal = 0
with open("input.txt") as cal_file:
    
    test = 0
    for cal in cal_file.readlines():
        test += int(cal.rstrip())
        if cal == "\n":
            print(test)

