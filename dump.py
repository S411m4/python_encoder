# to convert string to binary, format(ord(string), 'b'), where 'b' refers to bytes
# to convert string to binary, format(binary, 'c'), where 'c' refers to unicoding
# int(binary no, base=2). refers to the binary not decimal number

import string #jsut for the my algorithm

def str_to_binary(str):
    #converts a string(string) to binary(array)
    arr_bytes = []
    for i in str:
        char = format(ord(i), 'b')
        while len(char) < 8:
            char = '0' + char
        arr_bytes.append(char)
    return arr_bytes #returns an array

def XOR_operation(b1, b2):
    #performs XOR operation between two equal bytes (8 bits/1 character), result is a string
    result =''
    for i in range(0,8):
        if b1[i] != b2[i]:
            bit = '1'
        else:
            bit = '0'
        result = result + bit
    return result # returns a string

def binary_to_str(b_str):
    #converts string () to binary(string)
    b_string = ''
    # is instance(object, type), evaluate boolean according to type
    if isinstance(b_str, list):
        for i in b_str:
            char = format(int(i, base=2), 'c')
            print(i)
            b_string = b_string + char
    #didn't use else, because we wan't these two types specifically
    elif isinstance(b_str, str):
        b_string = format(int(b_str, base=2), 'c')

    return b_string # returns a string

def decrypt_message(cipher, key):
    b_cipher = str_to_binary(cipher)
    b_key = str_to_binary(key)
    b_text = []
    for bit in range(len(b_cipher)):
        char = XOR_operation(b_cipher[bit], b_key[bit])
        b_text.append(char)
    text = binary_to_str(b_text)
    return text





if __name__ == '__main__':

    text1 = str_to_binary('1c0111001f010100061a024b53535009181c')
    text2 = str_to_binary('686974207468652062756c6c277320657965')
    string = ''
    for i in range(len(text1)):
        char = XOR_operation(text1[i], text2[i])
        string += char
    print(binary_to_str(string))


    #simple algorithm to encode a message by using only uppercase ASCII letters as a key, and the cipher consists of only uppercase
    '''didn't work :(, you cannot convert using an uppercase key and result is uppercase, however:
    you can in case of using ascii-digits'''
'''
    key = string.ascii_letters + string.digits
    text = input('enter the text to encode: ')
    encoded_text = str_to_binary(text)
    key_bin_arr = []
    counter = 0'''

''''
    #converts every uppercase ascii to binary
    for char in key:
        key_bin = ''.join(str_to_binary(char))
        key_bin_arr.append(key_bin)

    for t in encoded_text:
        counter += 1
        for k in key_bin_arr:
            result = XOR_operation(t, k)
            cipher = binary_to_str(result)

            if cipher in key:
                print('key_char used: ', binary_to_str(k))
                print('character ' + str(counter) + ' option: ' + cipher)
            else:
                continue'''


#autodetect won't work because there is more than one possibility for certain values
def auto_detect_mode(value):
    #error: don't enter zeroes at the beginning
    #autodetects the type of value entered
    i = set(str(value))
    b_not_set = {'w', 'h', 'B', 'k', 'P', 'R', 'u', 'K', 'x', '4', '6', '2', 't', 'm', 'v', '5', 'z', 'O', 'r', 'f', 'N', 'l', 'C', 'Z', 'c', 'F', 'G', 'S', 'd', '3', 'X', 'U', 'a', 'T', 'E', 'b', 'e', 'Y', 's', 'H', 'V', '9', 'p', 'M', 'A', 'D', 'y', 'J', 'n', '7', 'j', 'Q', 'W', 'g', '8', 'i', 'o', 'L', 'q', 'I'}
    b_set = {'1', '0', ' '}
    hex_set = {' ', '8', '7', '9', 'A', '2', '5', 'D', 'F', '3', '1', 'B', '6', '0', '4', 'C', 'E'}
    hex_not_set = {'i', 'j', 'g', 'X', 'h', 'w', 'S', 'Q', 'N', 'o', 'R', 'G', 'U', 'a', 'k', 'P', 'Z', 'T', 'Y', 'd', 'K', 't', 'x', 'r', 'p', 's', 'O', 'W', 'J', 'l', 'I', 'H', 'L', 'u', 'n', 'm', 'c', 'z', 'v', 'q', 'y', 'f', 'V', 'e', 'M', 'b'}
    b64_set = {'K', 'V', '2', 'z', 'H', 'Z', 'f', 'o', '7', 'C', '=', 'R', 'X', 'A', 'P', 'D', 'J', 'c', '1', 'Y', 'Q', 'p', '9', 'E', 'h', '+', 't', 'm', 'L', 'W', '5', 'r', 'S', 'u', '/', 'n', 'a', 'i', 'q', 'x', 'e', 'T', 'w', '6', 'N', 'I', 'y', 'U', '0', 'j', '8', 'B', 'M', '4', ' ', 'l', 'g', 'v', 'F', 's', 'k', '3', 'O', 'd', 'b', 'G'}

    global type
    if i.issubset(b_set) and not i.issubset(b_not_set):
        type = 'binary'
    elif i.issubset(hex_set) and not i.issubset(hex_not_set):
        type = 'hex'
    elif i.issubset(b64_set):
        print('type either "base64" or "ASCII"')
        choice = input('choose which one you want: ')
        if choice =='base64':
            type = 'base64'
        elif choice.upper() == 'ASCII':
            type == 'ASCII'
        else:
            print('invalid option')
            exit()
    else:
        type = 'ASCII'

    print('autodetected type: ', type)

'''def converter(option = input('convert or XOR: '), from_ = input('convert from: ') , to = input('convert to: '), value = input('enter the value to be convereted to binary: ')):
    #converts any given value (hex, base64, ASCII, ...) to binary
    #users enters the value, and either determins its type or autodetect
    from_ = from_.strip().lower()
    if from_ in ['hex', 'hexadecimal', 'hexdecimal']:
        from_ = 'hex'
    elif from_ in ['ASCII', 'string', 'text']:
        from_ = 'ASCII'
    elif from_  == 'base64':
        from_ = 'base64'
    elif from_  == 'binary':
        form_ = 'binary'
    else:
        print('invalid option')
        exit()

    to = to.strip().lower()
    if to in ['hex', 'hexadecimal', 'hexdecimal']:
        pass
       # to = 'hex'
    elif to in ['ASCII', 'string', 'text']:
        pass
        #to = 'ASCII'
    elif to  == 'base64':
        to = 'base64'
    elif to  == 'binary':
        to = 'binary'
    else:
        print('invalid option')
        exit()

    if from_ == 'hex' and to == 'base64':
        b = hex_to_binary(value)
        result = binary_to_base64(b)

    elif from_ == 'hex' and to == 'binary':
        b_list = hex_to_binary(value)
        result = ''.join(b_list)

    return result
'''
#code to remove extra line breaks in a file
'''
with open ('code.txt') as c:
#output list where each index is a line
    line = c.readlines()
    print(line)
    counter = 0
    for i in line:
#remove the last 2 characters, which are the line break '\n'
        i = i[0:58]
        line[counter] = i
        counter += 1
    print(line)
'''
#repeat the key till the length of the text each letter successively
key_text = 'WORD'
key = key_text * (len(text)//len(key_text))
while len(key) < len(text):
    key = key + "WORD"
key = key[:len(text)]



#to separated a blob of characters according to printable ascii dictionary
for i in range(len(text)):
    if int(text[i:i+2]) < 100 and int(text[i:i+2]) > 31:
        list_text.append(text[i:i+2])
        i += 2
    elif int(text[i:i+3]) >= 100 and int(text[i:i+3]) < 127:
        list_text.append(text[i:i+3])
        i += 3

