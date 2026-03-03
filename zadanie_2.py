# TODO Найдите количество книг, которое можно разместить на дискете
V_all_MB = 1.44
Cnt_page = 100
Cnt_str = 50
Cnt_sinbl = 25
V_simbl_Bait = 4

V_one_MB = Cnt_str * Cnt_sinbl * Cnt_page * V_simbl_Bait / (1024*1024)
Cnt_all = V_all_MB // V_one_MB

print("Количество книг, помещающихся на дискету:", int(Cnt_all))
