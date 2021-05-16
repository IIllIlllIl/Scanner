#
# wang.tr@outlook.com
#

def read_file(path):
    file = open(path, "r")
    buf = file.read()
    file.close()
    return buf


def write_file(path, msg):
    file = open(path, "a")
    file.write(msg)
    file.close()