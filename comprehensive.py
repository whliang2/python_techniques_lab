list_a = [1,2,3,4,5,6,7,8,9]
str_list_a = [ num for num in list_a]

# str_list_a = [ if num%3 == 0: else "Nope" num for num in list_a ]

str_list_b = [num if num%3 == 0 else "" for num in list_a]

print(str_list_b)