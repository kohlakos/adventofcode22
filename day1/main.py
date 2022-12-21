max_cal = 0
with open("input.txt") as cal_file:
    
    current_calorie = 0
    for cal in cal_file.readlines():
        
        if cal == "\n":
            if max_cal < current_calorie:
                max_cal = current_calorie  
            current_calorie = 0
        else:    
            current_calorie += int(cal.rstrip())

print(max_cal)