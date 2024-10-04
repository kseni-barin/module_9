#Задача "Вызов разом"

def apply_all_func(int_list, *functions):
    results = {}
    if all(isinstance(element, int) for element in int_list):
        for function in functions:
            results[function.__name__] = function(int_list)
    else:
        print('передайте список из целых чисел')
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
