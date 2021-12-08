def output(main_list):
    output_list = []
    bun_numb = 0
    numb_litters = list(range(0,len(main_list)))
    for i in numb_litters:
        temp_list = []
        numb_buns = list(range(0,len(main_list[i])))
        for k in numb_buns:
            bun_phen = main_list[i][k][1]
            bun_parents = main_list[i][k][2]
            bun_id = main_list[i][k][3]
            bun_output = [bun_id, bun_parents, bun_phen]
            temp_list.append(bun_output)
            bun_numb = bun_numb + 1
        output_list.append(temp_list)
    
    return output_list
