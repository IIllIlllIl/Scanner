#
# wang.tr@outlook.com
#

import io_file
import scanner_func

# error processor
error = []

if __name__ == '__main__':
    path = input()
    p_err = path[0:len(path)-3] + "err"
    p_dyd = path[0:len(path)-3] + "dyd"
    p_sc = path[0:len(path)-3] + "s_c"

    buf = io_file.read_file(path)

    end = 0
    while end == 0:
        single = 0
        end = scanner_func.getnbc(buf)
        # symbol or reserve
        if scanner_func.letter() > 0:
            single = 1
            while (scanner_func.letter() > 0) or (scanner_func.digit() > 0):
                if scanner_func.concat(error) < 0:
                    break
                if end == -1:
                    break
                end = scanner_func.getchar(buf)

            if end == 0:
                scanner_func.retract()
            id = scanner_func.reserve()
            if id > 0:
                scanner_func.dyd_return(id, "0")
            else:
                scanner_func.dyd_return(10, str(scanner_func.symbol()))

            if (end == -2) or (end == -3):
                scanner_func.dyd_return(24, "EOLN")
            scanner_func.reset_token()

        # constant
        elif scanner_func.digit() > 0:
            single = 2
            while scanner_func.digit() > 0:
                scanner_func.concat()
                if end == -1:
                    break
                end = scanner_func.getchar(buf)

            if end == 0:
                scanner_func.retract()
            scanner_func.dyd_return(11, str(scanner_func.constant()))

            if (end == -2) or (end == -3):
                scanner_func.dyd_return(24, "EOLN")
            scanner_func.reset_token()

        # double
        elif scanner_func.double() > 0 and end != -1:
            char = scanner_func.character

            scanner_func.concat()
            end = scanner_func.getchar(buf)
            scanner_func.concat()

            id = scanner_func.reserve()
            if id > 0:
                scanner_func.dyd_return(id, "0")
                single = 3
            elif end == 0:
                scanner_func.retract(char)

            scanner_func.reset_token()

        # single
        if single == 0:
            if scanner_func.single() < 0:
                # illegal characters
                if scanner_func.character == ":":
                    error.append("***LINE:" + str(scanner_func.line())
                                 + "  expect '=' after ':' ")
                else:
                    error.append("***LINE:" + str(scanner_func.line())
                             + "  illegal character: " + scanner_func.character)

        # end of file
        if end == -1:
            scanner_func.dyd_return(25, "EOF")
        else:
            end = 0

    if len(buf) != 0:
        io_file.write_file(p_dyd, scanner_func.dyd)
        io_file.write_file(p_sc, scanner_func.symbol_table)
        io_file.add_file(p_sc, scanner_func.constant_table)
        io_file.write_file(p_err, error)
        print("Scanner finished")
    else:
        print("File not found.")
