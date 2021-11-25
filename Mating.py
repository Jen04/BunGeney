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
            off_temp[0][k] = mother[rand[0]][k]
            off_temp[1][k] = father[rand[1]][k]
            #off_list[i][0][k] = off_temp[0][k]
            #off_list[i][1][k] = off_temp[1][k]
        #print(i, off_temp)
        off_list[i] = off_temp
        #print("list = ", i, off_list)
    #print(off_list)
    return off_list

mom = [["X", "C", "b", "d", "E", "Xpt"], ["X", "c", "B", "d", "e", "X+"]]
dad = [["X", "C", "b", "d", "e", "Xpt"], ["Y", "c", "b", "D", "e", "N/A"]]
offspring = mate(mom, dad, 4)
print(offspring)
