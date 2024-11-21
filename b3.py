def swap_dict_keys_values(input_dict):
    swapped_dict = {}
    
    for key, value in input_dict.items():
        if value in swapped_dict:
            return None  
        swapped_dict[value] = key
    
    return swapped_dict


input_dict = eval(input("Nhập một dictionary: "))
result = swap_dict_keys_values(input_dict)
if result is None:
    print(None)
else:
    print("Dictionary sau khi hoán đổi key và value:", result)
