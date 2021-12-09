def count(litter):
    #count males
    numb_male = 0
    numb_malb = 0
    numb_malb = 0
    numb_mblack = 0
    numb_mgray = 0
    numb_mchoc = 0
    numb_mlilac = 0
    numb_mbrok = 0
    numb_mchar = 0
    numb_msolid = 0
    numb_mtrem = 0
    numb_mhealthy = 0
    for k in litter:
        sex_bun = litter[k][1][0]
        alb_bun = litter[k][1][1]
        col_bun = litter[k][1][2]
        pat_bun = litter[k][1][3]
        trem_bun = litter[k][1][4]
        if sex_bun == "Male":
            numb_male = numb_male + 1
            if alb_bun == "Albino":
                numb_malb = numb_malb + 1
            elif alb_bun == "Not Albino":
                numb_mxalb = numb_mxalb + 1
            else: print("Albino Counter Broke")
            
            # count male colors
            if col_bun == "Black":
                numb_mblack = numb_mblack + 1
            elif col_bun == "Gray":
                numb_mgray = numb_mgray + 1
            elif col_bun == "Chocolate":
                numb_mchoc = numb_mchoc + 1
            elif col_bun == "Lilac":
                numb_mlilac = numb_mlilac + 1
            else: print("Color Count broke")
            
            # count male patterns
            if pat_bun == "Broken":
                numb_mbrok = numb_mbrok + 1
            elif pat_bun == "Charlie":
                numb_mchar = numb_mchar + 1
            elif pat_bun == "Solid":
                numb_msolid = numb_msolid + 1
            else: print("Pattern Counter broke")

            # count male tremors
            if trem_bun == "Tremor":
                numb_mtrem = numb_mtrem + 1
            elif trem_bun == "Healthy":
                numb_mhealthy = numb_mhealthy + 1
            else: print("Tremor Counter broke")

    #count females
    numb_female = 0
    numb_falb = 0
    numb_falb = 0
    numb_fblack = 0
    numb_fgray = 0
    numb_fchoc = 0
    numb_flilac = 0
    numb_fbrok = 0
    numb_fchar = 0
    numb_fsolid = 0
    numb_ftrem = 0
    numb_fhealthy = 0
    for k in litter:
        sex_bun = litter[k][1][0]
        alb_bun = litter[k][1][1]
        col_bun = litter[k][1][2]
        pat_bun = litter[k][1][3]
        trem_bun = litter[k][1][4]
        if sex_bun == "Female":
            numb_female = numb_female + 1
            if alb_bun == "Albino":
                numb_falb = numb_falb + 1
            elif alb_bun == "Not Albino":
                numb_fxalb = numb_fxalb + 1
            else: print("Albino Counter Broke")
            
            # count female colors
            if col_bun == "Black":
                numb_fblack = numb_fblack + 1
            elif col_bun == "Gray":
                numb_fgray = numb_fgray + 1
            elif col_bun == "Chocolate":
                numb_fchoc = numb_fchoc + 1
            elif col_bun == "Lilac":
                numb_flilac = numb_flilac + 1
            else: print("Color Count broke")
            
            # count female patterns
            if pat_bun == "Broken":
                numb_fbrok = numb_fbrok + 1
            elif pat_bun == "Charlie":
                numb_fchar = numb_fchar + 1
            elif pat_bun == "Solid":
                numb_fsolid = numb_fsolid + 1
            else: print("Pattern Counter broke")

            # count female tremors
            if trem_bun == "Tremor":
                numb_ftrem = numb_ftrem + 1
            elif trem_bun == "Healthy":
                numb_fhealthy = numb_fhealthy + 1
            else: print("Tremor Counter broke")

    sex_tot = numb_male + numb_female
    sex_count = [numb_male, numb_female, sex_tot]


    alb_tot = numb_malb + numb_falb
    alb_count = [numb_malb, numb_falb, alb_tot]

    xalb_tot = numb_mxalb + numb_fxalb
    xalb_count = [numb_mxalb, numb_fxalb, xalb_tot]

    tot_alb_count = [[alb_count],[xalb_count]]


    black_tot = numb_mblack + numb_fblack
    black_count = [numb_mblack, numb_fblack, black_tot]

    gray_tot = numb_mgray + numb_fgray
    gray_count = [numb_mgray, numb_fgray, gray_tot]

    choc_tot = numb_mchoc + numb_fchoc
    choc_count = [numb_mchoc, numb_fchoc, choc_tot]

    lilac_tot = numb_mlilac + numb_flilac
    lilac_count = [numb_mlilac, numb_flilac, lilac_tot]

    col_count = [[black_count], [gray_count], [choc_count], [lilac_count]]


    brok_tot = numb_mbrok + numb_fbrok
    brok_count = [numb_mbrok, numb_fbrok, brok_tot]

    char_tot = numb_mchar + numb_fchar
    char_count = [numb_mchar, numb_fchar, char_tot]

    solid_tot = numb_msolid + numb_fsolid
    solid_count = [numb_msolid, numb_fsolid, solid_tot]

    pat_count = [[brok_count], [char_count], [solid_count]]


    trem_tot = numb_mtrem + numb_ftrem
    trem_count = [numb_mtrem, numb_ftrem, trem_tot]

    healthy_tot = numb_mhealthy + numb_fhealthy
    healthy_count = [numb_mhealthy, numb_fhealthy, healthy_tot]

    tot_trem_count = [[trem_count], [healthy_count]]


    count_table = [[sex_count], [tot_alb_count], [col_count], [pat_count], [tot_trem_count]]

    return count_table
