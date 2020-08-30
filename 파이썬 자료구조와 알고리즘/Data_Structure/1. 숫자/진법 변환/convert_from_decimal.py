def convert_from_decimal (number, base) :
    num_list = []
    num_temp = number
    while num_temp > 0 :
        num_list = [str(num_temp % base)] + num_list
        num_temp = num_temp // base
    return int(''.join(num_list))

def test_convert_from_decimal() :
    number, base = 10, 3
    assert(convert_from_decimal(number, base) == 101)
    print('테스트 통과!')

test_convert_from_decimal()