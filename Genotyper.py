def genotype(sex, albino, color, spotting, tremor):
    import random
    sex_gen = ["X", "Y"]
    albino_gen = [["C", "C"], ["C", "c"], ["c","C"], ["c", "c"]]
    col_gen = [["B", "B"], ["B", "b"], ["b","B"], ["b", "b"]]
    den_gen = [["D", "D"], ["D", "d"], ["d","D"], ["d", "d"]]
    spot_gen = [["E", "E"], ["E", "e"], ["e","E"], ["e", "e"]]
    trem_gen = [["X+", "X+"], ["X+", "Xpt"], ["Xpt","X+"], ["Xpt", "Xpt"]]

    bun_temp = [["sex 1", "albino 1", "col 1", "den 1", "spot 1", "trem 1"], ["sex 2", "albino 2", "col 2", "den 2", "spot 2", "trem 2"]]
    #print("bun_temp[1][1] = ", bun_temp[1][1]) #TS
    bun_sex = ["N/A"]*2
    bun_albino = ["N/A"]*2
    bun_col = ["N/A"]*2
    bun_den = ["N/A"]*2
    bun_spot = ["N/A"]*2
    bun_trem = ["N/A"]*2

    rand = [random.randint(0,1), random.randint(0,1), random.randint(0,2)]
    if albino == True:
        bun_albino =  albino_gen[3]
        color = ["Black", "Chocolate", "Gray", "Lilac"]
        color = color[random.randint(0,3)]
        #print(color)
        spotting = ["Broken", "Charlie", "Solid"]
        spotting = spotting[random.randint(0,2)]
    if albino == False: bun_albino = albino_gen[rand[2]]
    #print("Albino = ", bun_albino) #TS

    if sex == "Female":
        bun_sex = [sex_gen[0], sex_gen[0]]
        rand = [random.randint(0,1), random.randint(0,1), random.randint(0,2)]
        if tremor == True: 
            bun_trem = trem_gen[3]
        if tremor == False: 
            bun_trem = trem_gen[rand[2]]
        #print("Sex = ", bun_sex, "\nTremor = ",  bun_trem) #TS
    if sex == "Male":
        bun_sex = [sex_gen[0], sex_gen[1]]
        rand = [random.randint(0,1), random.randint(1,2), random.randint(0,2)]
        if tremor == True: 
            bun_trem[0] = "Xpt"
        if tremor == False: 
            bun_trem[0] = "X+"
        bun_trem[1] = "N/A"
        #print("Sex = ", bun_sex, "\nTremor = ",  bun_trem) #TS

    rand = [random.randint(0,2), random.randint(1,2), random.randint(0,2)]
    if color == "Black": 
            bun_col = col_gen[rand[0]]
            bun_den = den_gen[rand[2]]
    if color == "Gray":
            bun_col = col_gen[rand[0]]
            bun_den = den_gen[3]
    if color == "Chocolate":
            bun_col = col_gen[3]
            bun_den = den_gen[rand[2]]
    if color == "Lilac":
            bun_col = col_gen[3]
            bun_den = den_gen[3]
    #print("Color = ", bun_col, "\nDensity = ", bun_den) #TS
    rand = [random.randint(0,2), random.randint(1,2), random.randint(0,2)]
    if spotting == "Broken": bun_spot = spot_gen[rand[1]]
    if spotting == "Charlie": bun_spot = spot_gen[0]
    if spotting == "Solid": bun_spot = spot_gen[3]
    #print("Spotting = ", bun_spot) #TS

    #print("bun_sex[0] = ", bun_sex[0]) #TS
    bun_temp[0][0] = bun_sex[0]
    bun_temp[0][1] = bun_albino[0]
    bun_temp[0][2] = bun_col[0]
    bun_temp[0][3] = bun_den[0]
    bun_temp[0][4] = bun_spot[0]
    bun_temp[0][5] = bun_trem[0]

    #print("bun_sex[1] = ", bun_sex[1]) #TS
    bun_temp[1][0] = bun_sex[1]
    bun_temp[1][1] = bun_albino[1]
    bun_temp[1][2] = bun_col[1]
    bun_temp[1][3] = bun_den[1]
    bun_temp[1][4] = bun_spot[1]
    bun_temp[1][5] = bun_trem[1]

    return bun_temp
