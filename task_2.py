# TODO Найдите количество книг, которое можно разместить на дискете
i_v = 1.44
count_str = 100
count_string = 50
count_sym = 25
pamyat = 4

pam = pamyat*(count_sym *count_string *count_str)/(1024*1024)

ans = round(i_v/pam)
print("Количество книг, помещающихся на дискету:", ans)
