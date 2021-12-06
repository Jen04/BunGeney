def phenotype(bun):
    bun_sex = [bun[0][0], bun[1][0]]
    #print("bun_sex = ", bun_sex)
    bun_albino = [bun[0][1], bun[1][1]]
    #print("bun_albino = ", bun_albino)
    bun_col = [bun[0][2], bun[1][2]]
    #print("bun_col = ", bun_col)
    bun_den = [bun[0][3], bun[1][3]]
    #print("bun_den = ", bun_den)
    bun_spot = [bun[0][4], bun[1][4]]
    #print("bun_spot = ", bun_spot)
    bun_trem = [bun[0][5], bun[1][5]]
    #print("bun_trem = ", bun_trem)

    if bun_sex == ["X", "X"]: bun_sex = "Female"
    if bun_sex == ["X", "Y"]: bun_sex = "Male"

    if bun_trem == ["X+", "X+"] or bun_trem == ["X+", "Xpt"] or bun_trem == ["Xpt", "X+"] or bun_trem == ["X+", "N/A"]: bun_trem = "Healthy"
    if bun_trem == ["Xpt", "Xpt"] or bun_trem == ["Xpt", "N/A"]: bun_trem = "Tremor"

    if bun_albino == ["c", "c"]: 
        bun_albino = "Albino"
        bun_col = "Unknown"
        bun_spot = "Unknown"
        

    if bun_albino == ["C", "C"] or bun_albino == ["C", "c"] or bun_albino == ["c", "C"]: 
        bun_albino = "Not Albino"
        if bun_den == ["D", "D"] or bun_den == ["D", "d"] or bun_den == ["d", "D"]: 
            if bun_col == ["B", "B"] or bun_col == ["B", "b"] or bun_col == ["b", "B"]: bun_col = "Black"
            if bun_col == ["b", "b"]: bun_col = "Chocolate"
        if bun_den == ["d", "d"]: 
            if bun_col == ["B", "B"] or bun_col == ["B", "b"] or bun_col == ["b", "B"]: bun_col = "Gray"
            if bun_col == ["b", "b"]: bun_col = "Lilac"
        if bun_spot == ["E", "E"]: bun_spot = "Broken"
        if bun_spot == ["e", "e"]: bun_spot = "Solid"
        if bun_spot == ["E", "e"] or bun_spot == ["e", "E"]: bun_spot = "Charlie"
        

    output = [bun_sex, bun_albino, bun_col, bun_spot, bun_trem]

    return output

