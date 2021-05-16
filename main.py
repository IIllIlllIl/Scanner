#
# wang.tr@outlook.com
#

import io_file
import scanner_func

# global var
error = ()

# the position of the newest error
line = 0
# no error exist
err = 1



if __name__ == '__main__':
    #path = input()
    path = "./tests/test.pas"
    p_err = path[0:len(path)-3] + "err"
    buf = "  \n a "
    # have problem in eof
    while scanner_func.getnbc(buf) == 0:
        if scanner_func.letter() > 0:
            while (scanner_func.letter() > 0) or (scanner_func.digit() > 0):
                scanner_func.concat()
                scanner_func.getchar(buf)
            scanner_func.retract()
            id =  scanner_func.reserve()
            if id > 0:
                scanner_func.dyd_return(id, 0)
            else:
                scanner_func.dyd_return(10, str(scanner_func.symbol()))

    print(scanner_func.dyd)




