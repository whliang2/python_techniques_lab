sample_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for key in sample_dict:
    print(key)

print("==================")
for key in sample_dict:
    print(sample_dict[key])

print("==================")
for item_pair_tuple in sample_dict.items():
    print(item_pair_tuple)

print("==================")
all_dict_key = sample_dict.keys()
print(all_dict_key)


print("==================")
all_dict_vales = sample_dict.values()
print(all_dict_vales)

print("==================")
for index, key in enumerate(sample_dict):
    print(index,key)

print("==================")
