def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if 1 >= len(str_number):
        return first
    elif str_number.endswith('0'):
        return get_multiplied_digits(int(str_number[0:-1]))
    else:
        return first * get_multiplied_digits(int(str_number[1:]))
result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)
