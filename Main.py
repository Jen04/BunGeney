
from Genotyper import genotype 
from Mating import mate 
from Phenotyper import phenotype 

main_list = [[]]
litter_numb = 0

def new_parent(sex, albino, color, spotting, tremor):
    bun_gen = genotype(sex, albino, color, spotting, tremor)
    bun_phen = phenotype(bun_gen)
    parents = "Unknown"
    new_bun = [bun_gen, bun_phen, parents]
    return new_bun #stored as main_list[litter0][litter_buns]

def pot_mothers():
    pot_mom_list = []
    bun_numb = 0
    #print("len(main_list) = ", len(main_list))
    numb_litters = list(range(0,len(main_list)))
    for i in numb_litters:
        numb_buns = list(range(0,len(main_list[i])))
        #print("numb_buns in litter ", i, " = ", numb_buns)
        for k in numb_buns:
            sex_bun = main_list[i][k][1][0]
            if sex_bun == "Female":
                pot_mom_list.append(bun_numb)
            bun_numb = bun_numb + 1
        #print(pot_mom_list)
    return pot_mom_list
            
                
def pot_fathers():
    pot_dad_list = []
    bun_numb = 0
    numb_litters = list(range(0,len(main_list)))
    for i in numb_litters:
        numb_buns = list(range(0,len(main_list[i])))
        for k in numb_buns:
            sex_bun = main_list[i][k][1][0]
            if sex_bun == "Male":
                pot_dad_list.append(bun_numb)
            bun_numb = bun_numb + 1
        #print(pot_dad_list)
    return pot_dad_list

def new_litter(mother, father, numb_os, msex, malbino, mcolor, mspotting, mtremor, dsex, dalbino, dcolor, dspotting, dtremor):
    global litter_numb  
    if mother == "new":
        mother = new_parent(msex, malbino, mcolor, mspotting, mtremor)
        main_list[litter_numb].append(mother)
        bun_numb = 0
        numb_litters = list(range(0,len(main_list)))
        for i in numb_litters:
            numb_buns = list(range(0,len(main_list[i])))
            for k in numb_buns:
                bun_numb = bun_numb + 1
            mother_numb = bun_numb - 1
            if litter_numb >= 1:
                litter_numb = litter_numb + 1
    else:
        mother = int(mother)
        mother_numb = mother
    
    if father == "new":
        father = new_parent(dsex, dalbino, dcolor, dspotting, dtremor)
        main_list[litter_numb].append(father)
        bun_numb = 0
        numb_litters = list(range(0,len(main_list)))
        for i in numb_litters:
            numb_buns = list(range(0,len(main_list[i])))
            for k in numb_buns:
                bun_numb = bun_numb + 1
            father_numb = bun_numb - 1
            if litter_numb >= 1:
                litter_numb = litter_numb + 1
    else: 
        father = int(father)
        father_numb = father

    #print(main_list)
    parents = [mother_numb, father_numb]
    range_os = list(range(0,numb_os))
    litter_x = mate(mother, father, numb_os)
    litter_numb = litter_numb + 1
    #print(litter_numb)
    main_list.append([])
    #print(main_list, "\n")
    for i in range_os:
        bun_gen = litter_x[i]
        bun_phen = phenotype(litter_x[i])
        new_bun = [bun_gen, bun_phen, parents]
        main_list[litter_numb].append(new_bun)
    return main_list

def total(mother, father, numb_os, msex, malbino, mcolor, mspotting, mtremor, dsex, dalbino, dcolor, dspotting, dtremor):
    main_list = new_litter(mother, father, numb_os, msex, malbino, mcolor, mspotting, mtremor, dsex, dalbino, dcolor, dspotting, dtremor)
    mom_list = pot_mothers()
    dad_list = pot_fathers()

    #print("Potential Mothers = ", mom_list)
    #print("Potential Fathers = ", dad_list)
    return main_list
