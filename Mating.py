def mate(mother, father, numb_os):
    off_list = [[["N/A"]*6, ["N/A"]*6]]*numb_os
    k = list(range(0,6))
    import random
    for i in range(0,numb_os):
        off_temp = [["N/A"]*6, ["N/A"]*6]
        for k in list(range(0, 6)):
            rand = [random.randint(0,1), random.randint(0,1)]
            if k == 5 and off_temp[1][0] == "Y":
                rand[1] = 1
            if k == 5 and off_temp[1][0] == "X":
                rand[1] = 0
            off_temp[0][k] = mother[0][rand[0]][k]
            off_temp[1][k] = father[0][rand[1]][k]
        off_list[i] = off_temp
    return off_list

