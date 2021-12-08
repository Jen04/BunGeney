
from Genotyper import genotype 
from Mating import mate 
from Phenotyper import phenotype 
from Outputer import output
import random 

#seedset = random.randint(0,100000)
seedset = 18710
random.seed(seedset)

TS = True
if TS:
    print("\nCurrent seed is ", seedset)

main_list = [[]]
litter_numb = 0
bun_count = 0

def new_parent(sex, albino, color, spotting, tremor):
    global bun_count
    bun_gen = genotype(sex, albino, color, spotting, tremor)
    bun_phen = phenotype(bun_gen)
    parents = "Unknown"
    bun_count = bun_count + 1
    new_bun = [bun_gen, bun_phen, parents, bun_count]
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
    return pot_dad_list

def new_litter(mother, father, numb_os, msex, malbino, mcolor, mspotting, mtremor, dsex, dalbino, dcolor, dspotting, dtremor):
    global litter_numb
    global bun_count
    if TS:
        print("\nPre- append:\nmother = ", mother, "\nfather = ", father, "\nlitter_numb = ", litter_numb)
        print("len(main_list) = ", len(main_list))
    if mother == "new" or father == "new":
        if litter_numb > 0:
            litter_numb = litter_numb + 1
            main_list.append([])
    if TS:
        print("\nmother = ", mother, "\nfather = ", father, "\nlitter_numb = ", litter_numb)
        print("len(main_list) = ", len(main_list))
    if mother == "new":
        mother = new_parent(msex, malbino, mcolor, mspotting, mtremor)
        main_list[litter_numb].append(mother)
    else:
        mother = int(mother)
        bun_numb = 0
        #print("len(main_list) = ", len(main_list))
        numb_litters = list(range(0,len(main_list)))
        for i in numb_litters:
            numb_buns = list(range(0,len(main_list[i])))
            #print("numb_buns in litter ", i, " = ", numb_buns)
            for k in numb_buns:
                bun_id = main_list[i][k][3]
                if bun_id == mother:
                    mother = main_list[i][k]
                bun_numb = bun_numb + 1
    
    if father == "new":
        father = new_parent(dsex, dalbino, dcolor, dspotting, dtremor)
        main_list[litter_numb].append(father)
    else: 
        father = int(father)
        bun_numb = 0
        #print("len(main_list) = ", len(main_list))
        numb_litters = list(range(0,len(main_list)))
        for i in numb_litters:
            numb_buns = list(range(0,len(main_list[i])))
            #print("numb_buns in litter ", i, " = ", numb_buns)
            for k in numb_buns:
                bun_id = main_list[i][k][3]
                if bun_id == father:
                    father = main_list[i][k]
                bun_numb = bun_numb + 1

    if TS:
        print("\nmain_list before offspring = \n", main_list)
    parents = [mother[3], father[3]]
    range_os = list(range(0,numb_os))
    litter_x = mate(mother, father, numb_os)
    litter_numb = litter_numb + 1
    main_list.append([])
    if TS:
        print("\nlitter_numb before offspring = ", litter_numb)
        print("len(main_list) = ", len(main_list))
    for i in range_os:
        bun_gen = litter_x[i]
        bun_phen = phenotype(litter_x[i])
        bun_count = bun_count + 1
        new_bun = [bun_gen, bun_phen, parents, bun_count]
        if TS:
            print("\nlitter_numb at i = ", i, " is ", litter_numb)
            print("len(main_list) = ", len(main_list), "\n")
            print("main_list[litter_numb] = \n", main_list[litter_numb])
        main_list[litter_numb].append(new_bun)
    if TS:
        print("main_list after offspring = \n", main_list)
    return main_list  

def total(mother, father, numb_os, msex, malbino, mcolor, mspotting, mtremor, dsex, dalbino, dcolor, dspotting, dtremor):
    main_list = new_litter(mother, father, int(numb_os), msex, malbino, mcolor, mspotting, mtremor, dsex, dalbino, dcolor, dspotting, dtremor)
    mom_list = pot_mothers()
    dad_list = pot_fathers()
    
    if TS:
        print("Potential Mothers = ", mom_list)
        print("Potential Fathers = ", dad_list)
    return main_list
