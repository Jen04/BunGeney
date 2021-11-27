from Genotyper import genotype 
from Mating import mate 
from Phenotyper import phenotype 

main_list = []
sex = []
albino = []
color = []
spotting = []
tremor = []
litter0_buns = 0
litter_numb = 1

def new_parent(sex, albino, color, spotting, tremor):
    bun_gen = genotype(sex, albino, color, spotting, tremor)
    bun_phen = phenotype(bun_gen)
    parents = "Unknown"
    new_bun = [bun_gen, bun_phen, parents]
    return new_bun #stored as main_list[litter0][litter_buns]

def new_litter(mother, father, numb_os):
    from Main import litter0_buns 
    if mother == "new": #prompt user for new_parent values
        mother = new_parent(sex, albino, color, spotting, tremor)
        main_list[0][litter0_buns] = mother
        litter0_buns = litter0_buns + 1
    if father == "new": #prompt user for new_parent values
        father = new_parent(sex, albino, color, spotting, tremor)
        main_list[0][litter0_buns] = father
        litter0_buns = litter0_buns + 1

    range_os = numb_os = list(range(0,numb_os))
    litter_x = mate(mother, father, numb_os)
    for i in range_os:
        main_list[litter_numb][i][0] = litter_x[i]
    for i in range_os:
        litter_phen = phenotype(litter_x[i])
        main_list[litter_numb][i][1] = litter_phen[i]

    return main_list


