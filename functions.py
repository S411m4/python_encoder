# complete it later, currently it only translate hex to base64, and {ASCII, hex} to binary
# consider adding more options, like binary can be an array or a string
# remover extra nulls at the end, test by 'Burning 'em, if you ain't quick and nimble', this is due to extra 0s in ASCII

import itertools

NULL_hex = 'A282B2F20'
ASCII_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ASCII_lower = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
ASCII_all = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

url_codes = { '~backspace':'%08', '    ':'%09', '~linefeed~':'%0A', '~carriagereturn~':'%0D', ' ':'%20','^': '%5E',
              'w': '%77', 'a': '%61', 'M': '%4D', '=': '%3D', 'e': '%65', 'B': '%42', 'A': '%41', '-': '%2D', 'r': '%72',
              '4': '%34', 'S': '%53', '.': '%2E', 'R': '%52', '@': '%40', 'c': '%63', '\\': '%5C', 'p': '%70', '5': '%35',
              ']': '%5D', 'V': '%56', 'l': '%6C', 'x': '%78', 'o': '%6F', 'Y': '%59', 'T': '%54', 'C': '%43', '0': '%30',
              'h': '%68', '6': '%36', '"': '%22', 'y': '%79', '}': '%7D', 'f': '%66', 'O': '%4F', '9': '%39', '$': '%24',
              'E': '%45', 'D': '%44', '?': '%3F', 'J': '%4A', ';': '%3B', 'v': '%76', '|': '%7C', 'b': '%62', ':': '%3A',
              'F': '%46', 'j': '%6A', "'": '%27', 'g': '%67', '3': '%33', '*': '%2A', 'k': '%6B', '8': '%38', 's': '%73',
              '+': '%2B', '<': '%3C', 'q': '%71', 'U': '%55', '%': '%25', '/': '%2F', ',': '%2C', 'I': '%49', 'P': '%50',
              '1': '%31', 'm': '%6D', 'X': '%58', '>': '%3E', 'W': '%57', 't': '%74', '(': '%28', 'n': '%6E', 'K': '%4B',
              'Z': '%5A', '_': '%5F', 'Q': '%51', '7': '%37', 'L': '%4C', '!': '%21', '{': '%7B', '#': '%23', 'G': '%47',
              '2': '%32', 'z': '%7A', ')': '%29', 'u': '%75', 'H': '%48', 'd': '%64', 'N': '%4E', '`': '%60', '&': '%26',
              'i': '%69'}

base_64_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L',
                12: 'M', 13: 'N',
                14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y',
                25: 'Z', 26: 'a',
                27: 'b', 28: 'c', 29: 'd', 30: 'e', 31: 'f', 32: 'g', 33: 'h', 34: 'i', 35: 'j', 36: 'k', 37: 'l',
                38: 'm', 39: 'n',
                40: 'o', 41: 'p', 42: 'q', 43: 'r', 44: 's', 45: 't', 46: 'u', 47: 'v', 48: 'w', 49: 'x', 50: 'y',
                51: 'z', 52: '0',
                53: '1', 54: '2', 55: '3', 56: '4', 57: '5', 58: '6', 59: '7', 60: '8', 61: '9', 62: '+', 63: '/'
                }

base_64_binary_dict = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13,
                       'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25,
                       'a':26, 'b':27, 'c':28, 'd':29, 'e':30, 'f':31, 'g':32, 'h':33, 'i':34, 'j':35, 'k':36, 'l':37,
                       'm':38, 'n':39, 'o':40, 'p':41, 'q':42, 'r':43, 's':44, 't':45, 'u':46, 'v':47, 'w':48, 'x':49,
                       'y':50, 'z':51, '0':52, '1':53, '2':54, '3':55, '4':56, '5':57, '6':58, '7':59, '8':60, '9':61,
                       '+':62, '/':63, '=':000000
}

hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
            'D': 13, 'E': 14, 'F': 15}
hex_bin_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
                12: 'C', 13: 'D', 14: 'E', 15: 'F'}

printable_ASCII = {'k', 'W', '6', 'R', 'M', 'I', 's', 'F', 'C', '8', 'D', 'X', 'O', 'Y', 'r', 'B', 'c', 'g', 'y', 'l',
                   'Z', 'x', '4', 'f', 'T', 'V', 'Q', 'L', 'v', 't', 'z', '5', 'n', 'o', '3', 'S', 'A', 'H', 'U', 'j',
                   'm', '0', '2', 'N', 'q', 'K', 'w', 'd', 'G', '1', 'J', '7', 'p', '9', 'u', 'i', 'a', 'h', 'E', 'b',
                   'e', 'P', ' ', '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';',
                   '<', '=', '>', '?', '@', '\\', ']', '^', '_', '{', ']', '}', '|', '    ', '`'}

simple_readable_ASCII = {'k', 'W', '6', 'R', 'M', 'I', 's', 'F', 'C', '8', 'D', 'X', 'O', 'Y', 'r', 'B', 'c', 'g', 'y',
                         'l', 'Z', 'x', '4', 'f', 'T', 'V', 'Q', 'L', 'v', 't', 'z', '5', 'n', 'o', '3', 'S', 'A', 'H',
                         'U', 'j', 'm', '0', '2', 'N', 'q', 'K', 'w', 'd', 'G', '1', 'J', '7', 'p', '9', 'u', 'i', 'a',
                         'h', 'E', 'b', 'e', 'P', ' ', '\'', '"'}

ASCII_dict = {32: ' ', 33: '!', 34: '"', 35: '#', 36: '$', 37: '%', 38: '&', 39: '\'', 40: '(', 41: ')', 42: '*',
              43: '+', 44: ',',
              45: '-', 46: '.', 47: '/', 48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7',
              56: '8', 57: '9', 58: ':', 59: ';',
              60: '<', 61: '=', 62: '>', 63: '?', 64: '@', 65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F',
              71: 'G', 72: 'H', 73: 'I',
              74: 'J', 75: 'K', 76: 'L', 77: 'M', 78: 'N', 79: 'O', 80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T',
              85: 'U', 86: 'V', 87: 'W', 88: 'X',
              89: 'Y', 90: 'Z', 91: '[', 92: '\\', 93: ']', 94: '^', 95: '_', 96: '`', 97: 'a', 98: 'b', 99: 'c',
              100: 'd', 101: 'e', 102: 'f', 103: 'g',
              104: 'h', 105: 'i', 106: 'j', 107: 'k', 108: 'l', 109: 'm', 110: 'n', 111: 'o', 112: 'p', 113: 'q',
              114: 'r', 115: 's', 116: 't', 117: 'u',
              118: 'v', 119: 'w', 120: 'x', 121: 'y', 122: 'z', 123: '{', 124: '|', 125: '}', 126: '~', 0: '~NULL~',
              1: '~START OF HEADING~',
              2: '~START OF TEXT~', 3: '~END OF TEXT~', 4: '~END OF TRANSMISSION~', 5: '~ENQUIRY~', 6: '~ACKNOWLEDGE~',
              7: '~BELL~',
              8: '~BACKSPACE~', 9: '    ', 10: '~NEW LINE~', 11: '~VERTICAL TAB~', 12: '~NEW PAG~',
              13: '~CARRIAGE RETURN~',
              14: '~SHIFT OUT~', 15: '~SHIFT IN~', 16: '~DATA LINK ESCAPE~', 17: '~DEVICE CONTROL 1~',
              18: '~DEVICE CONTROL 2~',
              19: '~DEVICE CONTROL 3~', 20: '~DEVICE CONTROL 4~', 21: '~NEGATIVE ACKNOLWLEDGE~',
              22: '~SYNCHRONOUS IDLE~',
              23: '~END OF TRANS. BLOCK~', 24: '~CANCEL~', 25: '~END OF MEDIUM~', 26: '~SUBSTITUTE~', 27: '~ESCAPE~',
              28: '~FILE SEPARATOR~', 29: '~GROUP SEPARATOR~', 30: '~RECORD SEPARATOR~', 31: '~UNIT SEPARATOR~',
              127: '~DEL~'}


def binary_to_decimal(binary):
    decimal = int(str(binary), base=2)  # convert binary to equivalent decimal by mutliplying by corresponding (2**n)
    return decimal


def no_to_binary(no):
    # converts a single no to binary, and return 8 bit string value of number binary
    b = str(bin(no))[2:]  # to remove '0b' at the beginning
    return b


def hex_to_binary(hex):
    hex_b = []
    hex_list = list(hex.upper())
    for i in range(len(hex_list)):
        hex_list[i] = hex_dict[hex_list[i]]
    for j in hex_list:
        b = no_to_binary(int(j))
        while len(b) < 4:
            b = '0' + b
        hex_b.append(b)
    return hex_b  # array


def ASCII_to_binary(str):
    # converts a string(string) to binary(array)
    arr_bytes = []  # arr
    for i in str:
        char = format(ord(i), 'b')
        while len(char) < 8:
            char = '0' + char
        arr_bytes.append(char)
    return arr_bytes  # array





def binary_to_base64(binary):
    binary = ''.join(binary)
    base64_list = []

    # range(start, end, step)

    while len(binary) % 6 != 0:
        binary = binary + '0'

    for i in range(0, len(binary), 6):
        n = 6
        bb = binary[i:i + 6]
        base64_list.append(bb)

    for j in range(len(base64_list)):
        bj = base64_list[j]
        base64_list[j] = int(bj, base=2)

    for k in range(len(base64_list)):
        base64_list[k] = base_64_dict[base64_list[k]]

    result = ''.join(base64_list)
    l = len(binary) // 6
    while l % 4 != 0:
        result = result + '='
        l += 1

    return result  # string


def binary_to_hex(binary):
    binary = ''.join(binary)
    hex_list = []

    # range(start, end, step)
    for i in range(0, len(binary), 4):
        n = 4
        bb = binary[i: i + 4]
        hex_list.append(bb)

    while len(binary) % 4 != 0:
        binary = binary + '0'

    for j in range(len(hex_list)):
        bj = hex_list[j]
        hex_list[j] = int(bj, base=2)

    for k in range(len(hex_list)):
        hex_list[k] = hex_bin_dict[hex_list[k]]

    return ''.join(hex_list)  # string


def binary_to_ASCII(binary):
    # ASCII uses 8-bits
    binary = ''.join(binary)
    ASCII_list = []

    # range(start, end, step)
    for i in range(0, len(binary), 8):
        n = 8
        bb = binary[i: i + 8]
        ASCII_list.append(bb)

    while len(binary) % 8 != 0:
        binary = '0' + binary

    for j in range(len(ASCII_list)):
        bj = ASCII_list[j]
        # convert binary to decimal
        ASCII_list[j] = int(bj, base=2)

    for k in range(len(ASCII_list)):
        try:
            ASCII_list[k] = ASCII_dict[ASCII_list[k]]
        except:
            ASCII_list[k] = ''
    return ''.join(ASCII_list)

def base64_to_binary(b64):
    b64 = list(b64)
    bt = b64[0: len(b64)-3]

    for i in b64[-3:]:
        if i != '=':
            bt.append(i)
        else:
            continue

    for j in range(len(bt)):
        bt[j] = base_64_binary_dict[bt[j]]


    for k in range(len(bt)): #must use range(len()), to modify the list elements
        bt[k] = no_to_binary(bt[k])

    for b in range(len(bt)):
        while len(bt[b]) < 6:
            bt[b] = '0' + bt[b]

    return bt


def url_encode(str):
    #url coding of characters are % + hex decoded character
    code = ''
    for i in str:
        bi = ASCII_to_binary(i)
        r = '%' + binary_to_hex(bi)
        code = code + r
    return code

def url_decode(code):
    #takes url code only, not a full url
    code_list = []
    string = ''
    for i in range(0, len(code), 3):
        code_list.append(code[i+1:i+3]) #to get the hex value only without '%'

    for j in code_list:
        char = binary_to_ASCII(hex_to_binary(j))
        string += char
    return string







def XOR_operation(b1, b2):
    # takes an binary string as input
    b1 = ''.join(b1)
    b2 = ''.join(b2)
    result = ''
    for (i, j) in zip(b1, b2):
        if i == j:
            bit = '0'
        else:
            bit = '1'
        result = result + bit
    return result  # returns a string


def hamming_distance(b1, b2):
    #take two strings or arrays of binary
    x = XOR_operation(b1, b2)
    x = list(x)
    for i in range(len(x)):
        x[i] = int(x[i])
    return sum(x)
