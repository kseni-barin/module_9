def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if any(result % j == 0 for j in range(2, result)):
            print('Составное')
        #elif result == 1: print('1 - не простое и не составное')
        else:
            print('Простое')
        return result
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(1, 6, 30)
print(result)
