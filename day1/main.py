max_cal = 0
calorielist = []
with open("input.txt") as cal_file:
    
    current_calorie = 0
    for cal in cal_file.readlines():
        
        if cal == "\n":
            calorielist.append(current_calorie)
            if max_cal < current_calorie:
                max_cal = current_calorie  
            current_calorie = 0
        else:    
            current_calorie += int(cal.rstrip())

print(max_cal)

calorielist.sort(reverse=True)
print(sum((calorielist)[0:3]))