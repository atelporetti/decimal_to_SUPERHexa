import sys

SEPARATOR = ','

def deco_to_hexaplus(string_num):
    n = str(string_num)
    num_list = n.split(SEPARATOR)
    final_hexaplus = ''
    
    for num in num_list:
        original_num = num
        num = int(num)

        # array to store hexadecimal number
        hexaplus_num = ['0'] * 100

        # counter for hexadecimal number array
        i = 0
        while(num != 0):

            # temporary variable to store remainder
            temp = 0

            # storing remainder in temp variable.
            temp = num % 32

            # check if temp < 10
            if(temp < 10):
                hexaplus_num[i] = chr(temp + 48)
                i = i + 1
            else:
                hexaplus_num[i] = chr(temp + 55)
                i = i + 1
            num = int(num / 32)

        concat = ''
        converted_num = ''
        j = i - 1

        # printing hexadecimal number array in reverse order
        while(j >= 0):
            converted_num += concat.join(hexaplus_num[j])
            j = j - 1
        
        final_hexaplus += concat.join(converted_num)
        if not original_num == num_list[-1]:
            final_hexaplus += ','
            
    return print(final_hexaplus)


deco_to_hexaplus(sys.argv[1])