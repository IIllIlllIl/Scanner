#
# wang.tr@outlook.com
#

# newest input
character = ''

# read characters
token = ""

# buffer printer
ptr = 0

# reserve table
reserve_table = {"begin": 1, "end": 2, "integer": 3, "if": 4, "then": 5, "else": 6,
             "function": 7,"read": 8, "write": 9, "=": 12, "<>": 13, "<=": 14,
             "<": 15, ">=": 16, ">": 17, "-": 18, "*": 19, ":=": 20, "(": 21,
             ")": 22, ";": 23}

# symbol table
symbol_table = []

# constant table
constant_table = []

# output
dyd = []

# max length of var
length = 16


# read
def getchar(buf):
    global ptr
    global character
    global eoln

    character = buf[ptr]

    ptr += 1
    if ptr >= len(buf):
        if character == "\n":
            return -3
        return -1

    if character == "\n":
        return -2

    return 0


# read ignoring spaces
def getnbc(buf):
    global ptr
    global character

    if ptr >= len(buf):
        dyd_return("25", "EOF")
        return -1

    char = buf[ptr]

    # remove spaces
    while (char == " ") or (char == "\n") or (char == "\t") or (char == "\f"):
        if char == "\n":
            dyd_return("24", "EOLN")
        ptr += 1
        if ptr >= len(buf):
            return -1
        char = buf[ptr]

    # write character
    character = char
    ptr += 1
    if ptr >= len(buf):
        return -1

    return 0


# add to token
def concat(error = []):
    global token
    global character

    token += character

    if len(token) > length:
        # out of range
        error.append("***LINE:" + str(line()) +
                     "  length of variable：" + token + "...  out of range")
        return -1

    return 0


# is letter?
def letter():
    global character

    if (character >= "a") and (character <= "z"):
        return 1
    elif (character >= "A") and (character <= "Z"):
        return 2
    else:
        return -1


# is digit?
def digit():
    global character

    if (character >= "0") and (character <= "9"):
        return 1
    else:
        return -1


# roll back
def retract(reset = ''):
    global character
    global ptr

    character = reset
    ptr -= 1


# is reserve?
def reserve():
    if token in reserve_table:
        return reserve_table[token]
    else:
        return 0


# is symbol?
def symbol():
    if token not in symbol_table:
        symbol_table.append(token)
    return symbol_table.index(token)


# is constant?
def constant():
    const = float(token)
    if const not in constant_table:
        constant_table.append(const)
    return constant_table.index(const)


# add to dyd
def dyd_return(num, val):
    result = " " * (16 - len(val))
    result += val + " "
    if len(num) < 2:
        result += " "
    result += num
    dyd.append(result)

# reset token
def reset_token():
    global token

    token = ""


# deal with single symbols
def single():
    global character

    if character in reserve_table:
        dyd_return(str(reserve_table[character]), character)
        return 0

    return -1


# is double?
def double():
    global character

    if (character == ">") or (character == "<") or (character == ":"):
        return 1
    else:
        return 0


# get line
def line():
    return dyd.count("            EOLN 24") + 1