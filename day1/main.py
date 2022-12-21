max_cal = 0
with open("input.txt") as cal_file:
    
    temp = 0
    for cal in cal_file.readlines():
        
        if cal == "\n":
            if max_cal<temp:
                max_cal = temp
                print(max_cal)
            temp = 0
        else:    
            temp += int(cal.rstrip())

